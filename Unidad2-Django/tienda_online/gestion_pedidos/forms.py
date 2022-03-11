from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)
