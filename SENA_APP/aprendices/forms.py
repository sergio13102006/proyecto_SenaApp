from django import forms
from .models import aprendiz


class AprendizForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar aprendices"""
    
    class Meta:
        model = aprendiz
        fields = [
            'documento_identidad',
            'nombre',
            'apellido',
            'email',
            'telefono',
            'direccion',
            'fecha_nacimiento',
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '3001234567'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

        }
        # Etiquetas personalizadas
        labels = {
            'documento_identidad': 'Documento de Identidad',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'direccion': 'Dirección',
            'fecha_nacimiento': 'Fecha de Nacimiento',

        }

    # # Validaciones personalizadas
    
    # def clean_documento_identidad(self):
    #     """Validar que el documento contenga solo números"""
    #     documento = self.cleaned_data.get('documento_identidad')
    #     if not documento.isdigit():
    #         raise forms.ValidationError("El documento debe contener solo números.")
    #     return documento

    # def clean_telefono(self):
    #     """Validar que el teléfono contenga solo números"""
    #     telefono = self.cleaned_data.get('telefono')
    #     if telefono and not telefono.isdigit():
    #         raise forms.ValidationError("El teléfono debe contener solo números.")
    #     if telefono and len(telefono) != 10:
    #         raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
    #     return telefono