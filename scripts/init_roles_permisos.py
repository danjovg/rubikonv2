import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Rol, Permiso, Usuario

app = create_app()

# Diccionario base de permisos por rol
ROLES_Y_PERMISOS = {
    'admin': [
        'ver_panel', 'gestionar_usuarios', 'gestionar_tecnicos',
        'gestionar_clientes', 'ver_reportes', 'usar_calculadora',
        'gestionar_cotizaciones', 'gestionar_facturacion'
    ],
    'tecnico': ['usar_calculadora', 'ver_panel'],
    'vendedor': ['gestionar_clientes', 'gestionar_cotizaciones'],
    'auditor': ['ver_reportes']
}

with app.app_context():
    db.create_all()

    # Crear permisos
    for permisos in ROLES_Y_PERMISOS.values():
        for nombre in permisos:
            if not Permiso.query.filter_by(nombre=nombre).first():
                db.session.add(Permiso(nombre=nombre))

    # Crear roles y asignar permisos
    for rol_nombre, permisos in ROLES_Y_PERMISOS.items():
        rol = Rol.query.filter_by(nombre=rol_nombre).first()
        if not rol:
            rol = Rol(nombre=rol_nombre)
            db.session.add(rol)
            db.session.flush()

        rol.permisos.clear()
        for nombre_permiso in permisos:
            permiso = Permiso.query.filter_by(nombre=nombre_permiso).first()
            if permiso and permiso not in rol.permisos:
                rol.permisos.append(permiso)

    db.session.commit()
    print("✅ Roles y permisos creados o actualizados correctamente.")
