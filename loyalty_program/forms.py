from django import forms


class PersonalInfoForm(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)


class OfferApplicationForm(forms.Form):
    offer_id = forms.IntegerField(widget=forms.HiddenInput())
