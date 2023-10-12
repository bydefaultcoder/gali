from django import forms
from .models import ClientTransaction
from .models import Product

class ClientTransactionAdminForm(forms.ModelForm):
    class Meta:
        model = ClientTransaction
        fields = '__all__'  # Include all fields from the ClientTransaction model

