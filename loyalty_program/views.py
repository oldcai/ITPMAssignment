from django.contrib import messages
from django.db.models import F
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView, TemplateView

from loyalty_program.forms import OfferApplicationForm, PersonalInfoForm
from loyalty_program.models import Credit, Offer, UserOfferApplication


class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context.update({
            'offers': Offer.objects.filter(enabled=True)[:5],
        })
        return context


class ProfileView(FormView):
    template_name = 'profile.html'
    form_class = PersonalInfoForm

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'member_number': f'{user.id:08d}',
            'points': user.credit.points,
        })
        return context

    def form_valid(self, form):
        user = self.request.user
        user.email = form.cleaned_data['email']
        user.save()
        contact_info = user.contact_info
        contact_info.phone_number = form.cleaned_data['phone_number']
        contact_info.save()
        messages.add_message(self.request, messages.SUCCESS,
                             'Successfully updated')
        return redirect('profile')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING,
                             'Invalid input')
        return super(ProfileView, self).form_invalid(form)


class OfferDetailView(DetailView):
    template_name = 'offer_detail.html'
    model = Offer

    def get_context_data(self, **kwargs):
        context = super(OfferDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'member_number': f'{user.id:08d}',
            'points': user.credit.points,
        })
        return context


class ApplyOfferView(FormView):
    form_class = OfferApplicationForm

    def form_valid(self, form):
        offer = Offer.objects.filter(id=form.cleaned_data['offer_id']).first()
        if not offer:
            raise Http404('Not Found')
        user = self.request.user
        if offer.price_in_points <= user.credit.points:
            Credit.objects.filter(user=user).update(points=F('points') - offer.price_in_points)
            UserOfferApplication.objects.create(user=user, offer=offer)
            messages.add_message(self.request, messages.SUCCESS,
                                 f'Offer successfully applied. Credit points -{offer.price_in_points}')
        else:
            messages.add_message(self.request, messages.ERROR, 'Insufficient credit points for offer')

        return redirect('home')
