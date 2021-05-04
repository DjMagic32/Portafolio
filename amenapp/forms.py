from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    Nombre_y_Apellido = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"formulario"}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "id":"formulario"}))
    Telefono = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"formulario"}))
    Mensaje = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control" ,"id":"Mensaje"}))

    class Meta:
        model = Contacto
        fields = ["Nombre_y_Apellido","Email","Telefono","Mensaje"]
