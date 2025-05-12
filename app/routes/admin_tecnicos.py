from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.models import Tecnico, CategoriaTecnico, Persona, db
from app.forms import TecnicoForm
from app.utils.auth_utils import permiso_requerido

bp = Blueprint('admin_tecnicos', __name__, url_prefix='/admin/tecnicos')

@bp.route('/')
@login_required
@permiso_requerido('gestionar_tecnicos')
def listado():
    tecnicos = Tecnico.query.all()
    return render_template('admin/tecnicos/listado.html', tecnicos=tecnicos)

@bp.route('/nuevo', methods=['GET', 'POST'])
@login_required
@permiso_requerido('gestionar_tecnicos')
def nuevo_tecnico():
    form = TecnicoForm()
    form.categoria_id.choices = [(c.id, c.nombre) for c in CategoriaTecnico.query.all()]

    if form.validate_on_submit():
        persona = Persona.query.get(form.persona_id.data)
        if not persona:
            flash("Persona no encontrada.", "danger")
            return redirect(url_for('admin_tecnicos.listado'))

        tecnico = Tecnico(
            persona_id=persona.id,
            especialidad=form.especialidad.data,
            categoria_id=form.categoria_id.data
        )
        db.session.add(tecnico)
        db.session.commit()
        flash("Técnico registrado correctamente.", "success")
        return redirect(url_for('admin_tecnicos.listado'))

    return render_template('admin/tecnicos/nuevo.html', form=form)
