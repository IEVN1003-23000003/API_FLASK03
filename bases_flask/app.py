from flask import Flask, render_template, request

from flask import make_response, jsonify
import json

import forms

##para saber fecha
from datetime import datetime

app = Flask (__name__)

@app.route('/')
def home():
    return "Hello, World!"

#@app.route('/index')
#def index():
    #return "<h1>Welcome to the index page</h1>"
 #   return render_template('index.html')

@app.route('/index')
def index():
    titulo="IEVN1003 - PWA"
    listado=['Opera1','Opera2','Opera3','Opera4']
    return render_template('index.html', titulo=titulo, listado=listado)



#decorador:
@app.route('/about')
def about():
    return "<h1>This is about page.</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "Hola "+ user

@app.route("/numero/<int:n>")
def numero (n):
    return "Numero: {}".format(n)

@app.route("/suma/<float:n1>/<float:n2>")
def func (n1, n2):
    return "La suma es: {}".format(n1+n2)



@app.route("/prueba")
def prueba():
    return '''
    <h1>Prueba HTML</h1>
    <p>esto es un parrafo</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
    '''
@app.route('/operas', methods=['GET','POST'])
def operas():
    # PASO 1: Inicializar la variable 'resultado'
    resultado = None 

    if request.method == 'POST':
        n1_str = request.form.get('n1')
        n2_str = request.form.get('n2')
        if n1_str and n2_str:
                n1 = int(n1_str)
                n2 = int(n2_str)
                resultado = n1 + n2             
    return render_template('operas.html', resultado=resultado)


@app.route('/distancia')
def distancia():
    return render_template('distancia.html')







@app.route('/alumnos', methods=['GET', 'POST'] )
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    ##ARAY
    estudiantes =[]
    tem=[]
    ##Diccionario
    datos = {}
    alumnos_clase=forms.UserForm(request.form)
    if request.method=="POST":
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
        ##datos se guardan en diccionario
        datos = {"matricula":mat, "nombre":nom, "apellido":ape, "correo":em}

        datos_str=request.cookies.get('estudiante')
        if not datos_str:
            return "No hay cookie"
        
        ##Si no funciona podemos comentar estas 2: y luego descomentar, para forzar a que sea array
        tem=json.loads(datos_str)
        estudiantes=tem
        ##añadir elementos a una lista
        estudiantes=json.loads(datos_str)
        estudiantes.append(datos)

    response = make_response(render_template('alumnos.html', form=alumnos_clase, 
                                             mat=mat, nom=nom, ape=ape, em=em))
    
    ##cookie
    response.set_cookie('estudiante', json.dumps(estudiantes))
    
    return response

@app.route("/get_cookie")
def get_cookie():
    datos_str=request.cookies.get('estudiante')
    if not datos_str:
        return "No hay cookie"
    datos =json.loads(datos_str)

    return jsonify (datos)





##########                    PIZZERIA                      #####################################
@app.route('/pizzeria', methods=['GET', 'POST'])
def pizzeria():
    subtotal=0
    tamano='chica'
    ingredientes=0
    num_pizzas=0
    nombre = ''
    total_pizza = 0
    direccion=''
    telefono=''
    fecha=''
    precio_extra = 0
    ventas_totales = 0

     # COOKIES
    pizzas_cookie = request.cookies.get('pizzas')
    ventas_cookie = request.cookies.get('ventas')
    ##ARRAY
    pizzas = json.loads(pizzas_cookie) if pizzas_cookie else []
    ventas = json.loads(ventas_cookie) if ventas_cookie else []
    ##pizzas =[] lo quitamos porques se define arriba
    ##diccionario
    nueva_pizza={}
    pizzeria_clase = forms.PedidoForm(request.form)
    # Leer cookie (si existe)
    ##pizzas_guardadas = request.cookies.get('pizzas')
    ##if pizzas_guardadas:
    ##    pizzas = json.loads(pizzas_guardadas)
    ##else:
    ##   pizzas = []

    # Crear nueva pizza
    if request.method == 'POST' and 'agregar' in request.form:
        
        tamano=pizzeria_clase.tamano.data
        ##ingredientes= pizzeria_clase.ingredientes.data
        nombre=pizzeria_clase.nombre.data
        direccion = pizzeria_clase.direccion.data
        telefono = pizzeria_clase.telefono.data
        num_pizzas = pizzeria_clase.num_pizzas.data
        ingredientes = request.form.getlist('ingredientes') 
        ##ingredientesCalculo = request.form.getlist('ingredientes') 

         # calculo precio
        num_ingredientes = len(ingredientes)
        precio_extra = num_ingredientes * 10
        precios = {'chica': 40, 'mediana': 80, 'grande': 120}
        subtotal = precios[tamano] + precio_extra
        total_pizza = subtotal * num_pizzas

        #diccionario
        nueva_pizza = {
            'tamano': tamano,
            'ingredientes': ingredientes,
            'num_pizzas': num_pizzas,
            'total_pizza': total_pizza,

            'nombre' : nombre,
            'direccion' : direccion,
            'telefono' : telefono
        }

        # Agregar y guardar en cookies
        datos_str=request.cookies.get('pizzas')
        if not datos_str:
            pizzas = []  # inicializa una lista vacía
        else:
            pizzas = json.loads(datos_str)
            pizzas.append(nueva_pizza)

        ##Si no funciona podemos comentar estas 2: y luego descomentar, para forzar a que sea array
      ##  tem=json.loads(datos_str)
        ##nueva_pizza=tem
        ##estudiantes=tem
        ##lo añade a la lista sin borrar lo que había
        ##pizzas=json.loads(datos_str)
        ##pizzas.append(nueva_pizza)

        response = make_response(render_template('pizzeria.html', form=pizzeria_clase, 
                                             nombre= nombre, tamano = tamano, ingredientes= ingredientes, num_pizzas= num_pizzas, total_pizza = total_pizza, pizzas=pizzas))
        ##cookie
        response.set_cookie('pizzas', json.dumps(pizzas))
    
        return response

    if request.method == 'POST' and 'quitar' in request.form:
        index = int(request.form['quitar'])
        if 0 <= index < len(pizzas):
            pizzas.pop(index)
        response = make_response(render_template('pizzeria.html', form=pizzeria_clase, 
                                             nombre= nombre, tamano = tamano, ingredientes= ingredientes, num_pizzas= num_pizzas, total_pizza = total_pizza, pizzas=pizzas))
        response.set_cookie('pizzas', json.dumps(pizzas))
        return response
    
    if request.method == 'POST' and 'terminar' in request.form:
        ##Total del pedido
        total_pedido = sum(p['total_pizza'] for p in pizzas)

        cliente = pizzas[0]

        nueva_venta = {
            "nombre": cliente['nombre'],
            "direccion": cliente.get('direccion', ''),
            "telefono": cliente.get('telefono', ''),
                "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "total": total_pedido
            }
        
        
        
        ventas.append(nueva_venta)
        
        ventas_totales = sum(v['total'] for v in ventas)
        pizzas = []  # limpia cookie de pizzas
        mensaje = f"Pedido registrado exitosamente. Total a pagar: ${total_pedido}"
        
        response = make_response(render_template('pizzeria.html', form=pizzeria_clase, 
                                             pizzas=pizzas,mensaje=mensaje,ventas_totales=ventas_totales,ventas=ventas,nombre=nombre,direccion=direccion,telefono=telefono))
        response.set_cookie('pizzas', json.dumps(pizzas))
        response.set_cookie('ventas', json.dumps(ventas))
        return response

    # Mostrar la página normalmente
    return render_template('pizzeria.html', form=pizzeria_clase, 
                                             pizzas=pizzas)

   
    
    






@app.route("/ver_cookie")
def ver_cookie():
    datos_str=request.cookies.get('pizzas')
    if not datos_str:
        return "No hay cookie"
    datos =json.loads(datos_str)

    return jsonify (datos)


    # Mostrar tabla en GET
##return render_template('pizzeria.html', form=pizzeria_clase, pizzas=pizzas)










@app.route('/figuras', methods=['GET', 'POST'] )
def figuras():
    l1=0
    l2=0
    figura=""
    area=0
    figuras_clase=forms.User2Form(request.form)
    if request.method=="POST":
        l1=figuras_clase.l1.data
        l2=figuras_clase.l2.data
        figura = request.form.get('figura')
        if figura == 'rectangulo':
            area = int(l1) * int(l2)
        elif figura == 'triangulo':
            area = (int(l1) * int(l2)) / 2
        elif figura == 'circulo':
            area = 3.1416 * (int(l1) ** 2)  # l1 radio  **elevar pyton
        elif figura == 'pentagono':
            area = (5 * int(l1) * l2) / 2  
        else:
            area = 0  
    return render_template('figuras.html', form=figuras_clase, l1=l1, l2=l2, area=area)

if __name__ == '__main__':
    app.run(debug=True)


