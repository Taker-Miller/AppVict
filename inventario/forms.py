from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'imagen']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock'}),
            # Cambiar ClearableFileInput a FileInput
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'stock': 'Cantidad en Stock',
            'imagen': 'Imagen del Producto',
        }
