from flask import Blueprint, render_template, redirect, url_for, flash
from ..forms import ContactoForm

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    return render_template('public/index.html')

@public_bp.route('/servicios')
def servicios():
    return render_template('public/servicios.html')

@public_bp.route('/tienda')
def tienda():
    return render_template('public/tienda.html')

@public_bp.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactoForm()
    if form.validate_on_submit():
        flash('Gracias por contactarnos. Te responderemos pronto.', 'success')
        return redirect(url_for('public.contacto'))
    return render_template('public/contacto.html', form=form)