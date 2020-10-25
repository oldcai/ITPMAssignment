from django.views.generic import FormView

from loyalty_program.forms import PersonalInfoForm


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
