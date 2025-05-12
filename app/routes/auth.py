from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from ..models import Usuario
from ..forms import LoginForm
from .. import bcrypt, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.join(Usuario.persona).filter_by(correo=form.correo.data).first()
        if usuario and bcrypt.check_password_hash(usuario.contraseña_hash, form.contraseña.data):
            login_user(usuario)
            flash('Bienvenido al panel administrativo.', 'success')
            return redirect(url_for('admin.dashboard'))
        flash('Credenciales incorrectas.', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión finalizada.', 'info')
    return redirect(url_for('auth.login'))