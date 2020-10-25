from django import forms


class PersonalInfoForm(forms.Form):
    least_classes = forms.IntegerField(label='1', min_value=0)
