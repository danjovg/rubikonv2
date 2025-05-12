from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.models import CategoriaTecnico, db
from app.forms import CategoriaTecnicoForm
from app.utils.auth_utils import permiso_requerido

bp = Blueprint('admin_categorias_tecnicos', __name__, url_prefix='/admin/categorias-tecnicos')

@bp.route('/')
@login_required
@permiso_requerido('gestionar_tecnicos')
def listado():
    categorias = CategoriaTecnico.query.all()
    return render_template('admin/categorias/listado.html', categorias=categorias)

@bp.route('/nuevo', methods=['GET', 'POST'])
@login_required
@permiso_requerido('gestionar_tecnicos')
def nueva_categoria():
    form = CategoriaTecnicoForm()
    if form.validate_on_submit():
        categoria = CategoriaTecnico(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data
        )
        db.session.add(categoria)
        db.session.commit()
        flash("Categoría creada correctamente.", "success")
        return redirect(url_for('admin_categorias_tecnicos.listado'))
    return render_template('admin/categorias/nuevo.html', form=form)
