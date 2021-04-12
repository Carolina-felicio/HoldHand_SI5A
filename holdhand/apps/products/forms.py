from django import forms

from .models import ProductProfile


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductProfile
        exclude = ('slug', 'username', 'date_product', 'image_one', 'image_two', 'image_three',)

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control z-depth-1 border border-dark rounded'}),
            'segment': forms.TextInput(attrs={'class': 'form-control z-depth-1 border border-dark rounded'}),
            'store_name': forms.TextInput(attrs={'class': 'form-control z-depth-1 border border-dark rounded'}),
            'payment_method': forms.Select(attrs={'class': 'form-select z-depth-1 border border-dark rounded'}),
            'description': forms.Textarea(attrs={'class': 'form-control z-depth-1 border border-dark rounded'})
        }

        labels = {
            'product_name': 'Product name',
            'segment': 'Segment',
            'store_name': 'Store name',
            'payment_method': 'Payment method',
            'description': 'Description'
        }
