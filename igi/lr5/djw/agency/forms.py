from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Review

class AgencyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('address', 'phone', 'age', 'date', 'timezone')

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']

class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']

class BuyTripForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    promocode = forms.CharField(min_length=10, max_length=10, required=False)
    departure = forms.DateField(widget=forms.SelectDateWidget())