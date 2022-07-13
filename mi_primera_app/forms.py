from django import forms

class CompradorFormulario(forms.Form):
    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()

class StockFormulario(forms.Form):
    marca = forms.CharField()
    color = forms.CharField()
    cantidad = forms.IntegerField()

class VendedorFormulario(forms.Form):
    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()


class CompradorBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

 