from django import forms
from .models import Product, Attribute

class ProductAttributeForm(forms.ModelForm):
    attributes = forms.ModelMultipleChoiceField(
        queryset=Attribute.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Allows adding a product without attributes
    )

    class Meta:
        model = Product
        fields = ['attributes']
