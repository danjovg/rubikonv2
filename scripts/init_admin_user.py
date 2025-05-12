
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Persona, Usuario, Rol
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()

    # Verificar si ya existe la persona
    correo = "admin@rubikonsa.com"
    persona = Persona.query.filter_by(correo=correo).first()
    if not persona:
        persona = Persona(
            nombre="Administrador General",
            correo=correo,
            telefono="55555555",
            tipo_persona="usuario",
            tipo_entidad="persona",
            documento="123456789",
            tipo_documento="DPI"
        )
        db.session.add(persona)
        db.session.flush()  # para obtener el ID

    # Verificar si ya existe el usuario
    usuario_existente = Usuario.query.filter_by(persona_id=persona.id).first()
    if not usuario_existente:
        rol_admin = Rol.query.filter_by(nombre='admin').first()
        if not rol_admin:
            print("⚠️ Rol 'admin' no encontrado. Asegúrate de correr primero init_roles_permisos.py")
            sys.exit()

        usuario = Usuario(
            persona_id=persona.id,
            contraseña_hash=generate_password_hash("admin1234"),
            activo=True,
            rol_id=rol_admin.id
        )
        db.session.add(usuario)
        db.session.commit()
        print("✅ Usuario administrador creado exitosamente.")
        print("Correo: admin@rubikonsa.com")
        print("Contraseña: admin1234")
    else:
        print("ℹ️ El usuario ya existe. No se creó uno nuevo.")
