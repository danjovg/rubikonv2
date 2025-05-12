from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, TextAreaField, FloatField, IntegerField, SelectField, HiddenField)
from wtforms.validators import DataRequired, Email, Length

# 🔐 Login
class LoginForm(FlaskForm):
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

# 🧍 Persona
class PersonaForm(FlaskForm):
    nombre = StringField('Nombre completo', validators=[DataRequired()])
    correo = StringField('Correo electrónico', validators=[Email()])
    telefono = StringField('Teléfono')
    direccion = StringField('Dirección')
    tipo_persona = SelectField('Tipo de persona', choices=[
        ('cliente', 'Cliente'),
        ('usuario', 'Usuario'),
        ('empleado', 'Empleado'),
        ('tecnico', 'Técnico'),
        ('proveedor', 'Proveedor')
    ], validators=[DataRequired()])
    tipo_entidad = SelectField('Entidad', choices=[
        ('persona', 'Persona natural'),
        ('empresa', 'Empresa')
    ])
    tipo_documento = SelectField('Tipo de documento', choices=[
        ('DPI', 'DPI'), ('NIT', 'NIT'), ('Pasaporte', 'Pasaporte')
    ])
    documento = StringField('Número de documento')
    submit = SubmitField('Guardar')

# 🔐 Usuario (requiere persona_id)
class UsuarioForm(FlaskForm):
    persona_id = HiddenField('Persona ID')
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    rol_id = SelectField('Rol', coerce=int)
    submit = SubmitField('Crear usuario')

# 👤 Cliente
class ClienteForm(FlaskForm):
    persona_id = HiddenField('Persona ID')
    submit = SubmitField('Registrar cliente')

# 👨‍🔧 Técnico
class TecnicoForm(FlaskForm):
    persona_id = HiddenField('ID Persona', validators=[DataRequired()])
    especialidad = StringField('Especialidad', validators=[DataRequired()])
    categoria_id = SelectField('Categoría', coerce=int)
    submit = SubmitField('Guardar Técnico')

# 👨‍🔧 Categoría Técnico
class CategoriaTecnicoForm(FlaskForm):
    nombre = StringField('Nombre de la categoría', validators=[DataRequired()])
    descripcion = StringField('Descripción')
    submit = SubmitField('Guardar categoría')

# 👨‍💼 Empleado
class EmpleadoForm(FlaskForm):
    persona_id = HiddenField('Persona ID')
    cargo = StringField('Cargo')
    submit = SubmitField('Registrar empleado')

# 🏢 Proveedor
class ProveedorForm(FlaskForm):
    persona_id = HiddenField('Persona ID')
    razon_social = StringField('Razón Social')
    submit = SubmitField('Registrar proveedor')

# 🛒 Producto
class ProductoForm(FlaskForm):
    nombre = StringField('Nombre del producto', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    precio = FloatField('Precio', validators=[DataRequired()])
    stock = IntegerField('Stock disponible')
    categoria = SelectField('Categoría', coerce=int)
    submit = SubmitField('Guardar producto')

# 🏊 Piscina
class PiscinaForm(FlaskForm):
    cliente_id = SelectField('Cliente', coerce=int)
    nombre_proyecto = StringField('Nombre del proyecto', validators=[DataRequired()])
    tipo = SelectField('Tipo de piscina', choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')])
    ancho = FloatField('Ancho (m)')
    largo = FloatField('Largo (m)')
    altura_max = FloatField('Altura máxima (m)')
    altura_min = FloatField('Altura mínima (m)')
    volumen_m3 = FloatField('Volumen (m³)')
    submit = SubmitField('Registrar piscina')

# 📋 Cotización
class CotizacionForm(FlaskForm):
    cliente_id = SelectField('Cliente', coerce=int)
    producto_id = SelectField('Producto', coerce=int)
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Agregar a cotización')

# 📬 Contacto Público
class ContactoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo', validators=[Email()])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')

