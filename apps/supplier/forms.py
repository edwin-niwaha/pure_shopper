# forms.py
from django import forms
from .models import Supplier,  PurchaseOrder, PurchaseOrderItem


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "contact_name", "email", "phone", "address"]

    def clean(self):
        cleaned_data = super().clean()

        # Validate supplier name
        if not cleaned_data.get("name"):
            raise forms.ValidationError("Supplier name cannot be empty.")

        # Validate email address
        if not cleaned_data.get("email"):
            raise forms.ValidationError("Email address cannot be empty.")

        # Validate phone number
        phone = cleaned_data.get("phone")
        if phone:
            # Convert PhoneNumber object to string for validation
            phone_str = str(phone)
            if not phone_str.replace("+", "").isdigit():
                raise forms.ValidationError("Phone number must contain only digits.")

        return cleaned_data  # Don't forget to return cleaned_data!


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'status', 'notes']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PurchaseOrderItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = ['product', 'quantity']
        widgets = {
            'unit_price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'min': '1'}),
        }
