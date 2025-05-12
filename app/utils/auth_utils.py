from flask_login import current_user
from functools import wraps
from flask import redirect, url_for, flash

def permiso_requerido(nombre_permiso):
    def decorador(f):
        @wraps(f)
        def decorado(*args, **kwargs):
            if not current_user.is_authenticated:
                flash("Debes iniciar sesión.", "warning")
                return redirect(url_for("auth.login"))
            permisos = [rp.permiso.nombre for rp in current_user.rol.permisos_asociados]
            if nombre_permiso not in permisos:
                flash("No tienes permiso para acceder a esta sección.", "danger")
                return redirect(url_for("admin.dashboard"))
            return f(*args, **kwargs)
        return decorado
    return decorador
