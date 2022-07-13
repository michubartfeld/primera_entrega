from django.shortcuts import render
from mi_primera_app.models import Comprador, Stock, Vendedor
from mi_primera_app.forms import CompradorFormulario, StockFormulario, VendedorFormulario, CompradorBusquedaFormulario

# Create your views here.
def mostrar_index(request):
    return render(request, "mi_primera_app/index.html", {"mi_titulo":"Hola"})

def comprador_formulario(request):

    if request.method == "POST":
        mi_formulario = CompradorFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            comprador = Comprador(email = datos["email"], nombre = datos["nombre"], apellido = datos["apellido"])
            comprador.save()

            return render(request, "mi_primera_app/form_comprador.html", {"mensaje": "Comprador Registrado con exito!"})
            
    else:

        mi_formulario = CompradorFormulario()

        return render(request, "mi_primera_app/form_comprador.html", {"mi_formulario": mi_formulario})



def stock_formulario(request):

    if request.method == "POST":
        mi_formulario = StockFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            stock = Stock(marca = datos["marca"], color = datos["color"], cantidad = datos["cantidad"])
            stock.save()

            return render(request, "mi_primera_app/formulario_stock.html", {"mensaje": "Stock ingresado con exito!"})

    else:

        mi_formulario = StockFormulario()

        return render(request, "mi_primera_app/formulario_stock.html", {"mi_formulario": mi_formulario})

           
def vendedor_formulario(request):

    if request.method == "POST":
        mi_formulario = VendedorFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            vendedor = Vendedor(email = datos["email"], nombre = datos["nombre"], apellido = datos["apellido"])
            vendedor.save()

            return render(request, "mi_primera_app/form_vendedor.html", {"mensaje": "Vendedor registrado con exito!"})
            
    else:

        mi_formulario = VendedorFormulario()

        return render(request, "mi_primera_app/form_vendedor.html", {"mi_formulario": mi_formulario})








def formulario_busqueda(request):
    busqueda_formulario = CompradorBusquedaFormulario()

    if request.GET:
        compradores = Comprador.objects.filter(nombre=request.GET["criterio"]).all()

    else:
        compradores = []

    return render(request, "mi_primera_app/buscar_comprador.html", {"busqueda_formulario": busqueda_formulario, "compradores": compradores})



    

