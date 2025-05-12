from flask import Blueprint, render_template, request
from app.modules.calculadora.logic import calcular_volumen, calcular_quimicos
from flask_login import login_required
from app.utils.auth_utils import permiso_requerido

calculadora_bp = Blueprint('calculadora', __name__)

@calculadora_bp.route('/calculadora', methods=['GET', 'POST'])
@login_required
@permiso_requerido('ver_calculadora')
def index():
    resultado = None
    if request.method == 'POST':
        ancho = float(request.form.get('ancho', 0))
        largo = float(request.form.get('largo', 0))
        altura = float(request.form.get('altura', 0))
        volumen = calcular_volumen(ancho, largo, altura)
        quimicos = calcular_quimicos(volumen)
        resultado = {
            "volumen": volumen,
            "quimicos": quimicos
        }
    return render_template('admin/calculadora.html', resultado=resultado)
