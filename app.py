from flask import Flask, render_template, request
import forms

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
    # 🌟 PASO 1: Inicializar la variable 'resultado'
    # Esto asegura que exista siempre, incluso en el método GET, resolviendo el UnboundLocalError.
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
    alumnos_clase=forms.UserForm(request.form)
    if request.method=="POST":
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
    return render_template('alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em)


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
