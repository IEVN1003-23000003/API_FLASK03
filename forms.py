from wtforms import Form
from wtforms import StringField, EmailField, PasswordField, IntegerField
from wtforms import FloatField  
from wtforms import validators

class UserForm (Form):
    matricula=IntegerField('Matricula',
        [validators.DataRequired(message='La matricula es obligatoria')]
    )
    
    nombre = StringField('Nombre', 
        [validators.DataRequired(message='El campo es requerido')]
    )
    
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