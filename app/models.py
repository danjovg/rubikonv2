from .database import db
from flask_login import UserMixin
from datetime import datetime

# ====================================
# 🧍 TABLA BASE: PERSONAS
# ====================================

class Persona(db.Model):
    __tablename__ = 'personas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    tipo_persona = db.Column(db.String(50))  # cliente, usuario, tecnico, empleado, proveedor
    tipo_entidad = db.Column(db.String(50))  # persona, empresa
    documento = db.Column(db.String(50))
    tipo_documento = db.Column(db.String(20))  # DPI, NIT, Pasaporte

    # Relaciones
    usuario = db.relationship("Usuario", uselist=False, back_populates="persona")
    cliente = db.relationship("Cliente", uselist=False, back_populates="persona")
    tecnico = db.relationship("Tecnico", uselist=False, back_populates="persona")
    empleado = db.relationship("Empleado", uselist=False, back_populates="persona")
    proveedor = db.relationship("Proveedor", uselist=False, back_populates="persona")

# ====================================
# 🔐 USUARIOS Y ROLES
# ====================================

class Rol(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    descripcion = db.Column(db.String(200))
    usuarios = db.relationship("Usuario", back_populates="rol")

    permisos = db.relationship('Permiso', secondary='rol_permiso', back_populates='roles')

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    contraseña_hash = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    persona = db.relationship("Persona", back_populates="usuario")
    rol = db.relationship("Rol", back_populates="usuarios")

# ====================================
# 👤 TIPOS DE PERSONAS DERIVADAS
# ====================================

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    persona = db.relationship("Persona", back_populates="cliente")

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    cargo = db.Column(db.String(100))

    persona = db.relationship("Persona", back_populates="empleado")

class Tecnico(db.Model):
    __tablename__ = 'tecnicos'
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    especialidad = db.Column(db.String(100))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias_tecnicos.id'))

    persona = db.relationship("Persona", back_populates="tecnico")
    categoria = db.relationship("CategoriaTecnico", back_populates="tecnicos")

class CategoriaTecnico(db.Model):
    __tablename__ = 'categorias_tecnicos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    descripcion = db.Column(db.String(200))

    tecnicos = db.relationship('Tecnico', back_populates='categoria')

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    razon_social = db.Column(db.String(150))

    persona = db.relationship("Persona", back_populates="proveedor")

# ====================================
# 🧪 PERMISOS
# ====================================

class Permiso(db.Model):
    __tablename__ = 'permisos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    descripcion = db.Column(db.String(200))

    roles = db.relationship('Rol', secondary='rol_permiso', back_populates='permisos')

class RolPermiso(db.Model):
    __tablename__ = 'rol_permiso'
    id = db.Column(db.Integer, primary_key=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    permiso_id = db.Column(db.Integer, db.ForeignKey('permisos.id'))

# ====================================
# 🏊 PROYECTOS Y SERVICIO TÉCNICO
# ====================================

class Piscina(db.Model):
    __tablename__ = 'piscinas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    nombre_proyecto = db.Column(db.String(100))
    tipo = db.Column(db.String(50))  # residencial, comercial
    ancho = db.Column(db.Float)
    largo = db.Column(db.Float)
    altura_max = db.Column(db.Float)
    altura_min = db.Column(db.Float)
    volumen_m3 = db.Column(db.Float)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class VisitaTecnica(db.Model):
    __tablename__ = 'visitas_tecnicas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    tecnico_id = db.Column(db.Integer, db.ForeignKey('tecnicos.id'))
    fecha = db.Column(db.DateTime)
    motivo = db.Column(db.String(200))
    notas = db.Column(db.Text)

# ====================================
# 🛒 TIENDA Y PRODUCTOS
# ====================================

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(200))

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))

# ====================================
# 📄 COTIZACIONES Y FACTURAS
# ====================================

class Cotizacion(db.Model):
    __tablename__ = 'cotizaciones'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float)
    estado = db.Column(db.String(50))  # pendiente, aprobada, rechazada

class DetalleCotizacion(db.Model):
    __tablename__ = 'detalle_cotizacion'
    id = db.Column(db.Integer, primary_key=True)
    cotizacion_id = db.Column(db.Integer, db.ForeignKey('cotizaciones.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)
    precio_unitario = db.Column(db.Float)

class Factura(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float)
    metodo_pago = db.Column(db.String(50))

class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'
    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)
    precio_unitario = db.Column(db.Float)

# ====================================
# 🚚 ENVÍOS Y LOGÍSTICA
# ====================================

class Ruta(db.Model):
    __tablename__ = 'rutas'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200))
    responsable = db.Column(db.String(100))

class Envio(db.Model):
    __tablename__ = 'envios'
    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'))
    ruta_id = db.Column(db.Integer, db.ForeignKey('rutas.id'))
    fecha_envio = db.Column(db.DateTime)
    estado = db.Column(db.String(50))  # en tránsito, entregado, cancelado

# ====================================
# ✅ TAREAS Y OPERACIONES
# ====================================

class TareaAsignada(db.Model):
    __tablename__ = 'tareas_asignadas'
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    descripcion = db.Column(db.String(200))
    fecha_asignada = db.Column(db.DateTime)
    estado = db.Column(db.String(50))  # pendiente, en progreso, completada
    modulo_referencia = db.Column(db.String(100))  # piscina, cliente, etc.
    id_referencia = db.Column(db.Integer)

# ====================================
# 📝 ETIQUETAS DINÁMICAS
# ====================================

class Etiqueta(db.Model):
    __tablename__ = 'etiquetas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

class Etiquetado(db.Model):
    __tablename__ = 'etiquetado'
    id = db.Column(db.Integer, primary_key=True)
    etiqueta_id = db.Column(db.Integer, db.ForeignKey('etiquetas.id'))
    modulo = db.Column(db.String(100))  # tabla
    id_registro = db.Column(db.Integer)

# ====================================
# 📋 BITÁCORAS Y AUDITORÍA
# ====================================

class BitacoraLogin(db.Model):
    __tablename__ = 'bitacora_login'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    ip = db.Column(db.String(100))
    exito = db.Column(db.Boolean)

class BitacoraActividad(db.Model):
    __tablename__ = 'bitacora_actividad'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100))
    accion = db.Column(db.String(200))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

class ErrorLog(db.Model):
    __tablename__ = 'errores'
    id = db.Column(db.Integer, primary_key=True)
    modulo = db.Column(db.String(100))
    mensaje = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

class AuditoriaGlobal(db.Model):
    __tablename__ = 'auditoria_global'
    id = db.Column(db.Integer, primary_key=True)
    tabla = db.Column(db.String(100))
    id_registro = db.Column(db.Integer)
    campo = db.Column(db.String(100))
    valor_anterior = db.Column(db.String(255))
    valor_nuevo = db.Column(db.String(255))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

# ====================================
# ⚙️ CONFIGURACIÓN GLOBAL
# ====================================

class ConfiguracionEmpresa(db.Model):
    __tablename__ = 'configuracion_empresa'
    id = db.Column(db.Integer, primary_key=True)
    nombre_empresa = db.Column(db.String(100))
    direccion = db.Column(db.String(200))
    correo_contacto = db.Column(db.String(100))
    telefono = db.Column(db.String(50))