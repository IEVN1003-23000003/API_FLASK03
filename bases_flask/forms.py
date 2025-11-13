from wtforms import Form
from wtforms import StringField, EmailField, PasswordField, IntegerField
from wtforms import FloatField  
from wtforms import validators

class UserForm (Form):
    matricula=IntegerField('Matricula',
        [validators.DataRequired(message='La matricula es obligatoria')]
    )
    
   ## nombre = StringField('Nombre', 
     ##   [validators.DataRequired(message='El campo es requerido')]
    ##)
    
    apellido = StringField('Apellido',
        [validators.DataRequired(message='El campo es requerido')]
    )
    
    correo = EmailField('Correo', 
        [validators.Email(message='Ingrese Correo válido')]
    )

class User2Form (Form):
    l1=IntegerField('  L1',
        [validators.DataRequired(message='El dato es necesario')]
    )

    l2=IntegerField('  L2')

class PedidoForm(Form):
    # cliente
    nombre = StringField('Nombre del cliente', [validators.DataRequired()])
    direccion = StringField('Dirección', [validators.DataRequired()])
    telefono = StringField('Teléfono', [validators.DataRequired()])

    # pizza
    tamano = StringField('Tamaño de pizza', [validators.DataRequired()])
    ingredientes = StringField('Ingredientes', [validators.Optional()])
    num_pizzas = IntegerField('Número de pizzas', [validators.DataRequired(), validators.NumberRange(min=1)])

class DatosPedido(Form):
    # cliente
    nombre = StringField('Nombre del cliente', [validators.DataRequired()])
    direccion = StringField('Dirección', [validators.DataRequired()])
    telefono = StringField('Teléfono', [validators.DataRequired()])

    # pizza
    tamano = StringField('Tamaño de pizza', [validators.DataRequired()])
    ingredientes = StringField('Ingredientes', [validators.Optional()])
    num_pizzas = IntegerField('Número de pizzas', [validators.DataRequired(), validators.NumberRange(min=1)])
     