from django import forms


class LocationForm(forms.Form):
    firname = forms.CharField(max_length=100,
                              widget=forms.TextInput
                              (attrs={'placeholder': 'Choice 1'}))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput
                            (attrs={'placeholder': 'Enter your email'}))
