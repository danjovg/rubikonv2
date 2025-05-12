from flask import Flask
from .config import Config
from .database import db
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'

    # Blueprints
    from .routes.public import public_bp
    from .routes.auth import auth_bp
    from .routes.admin import admin_bp
    from app.routes.admin_tecnicos import bp as admin_tecnicos_bp
    from app.routes.admin_categorias_tecnicos import bp as admin_categorias_tecnicos_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(admin_tecnicos_bp)
    app.register_blueprint(admin_categorias_tecnicos_bp)

    return app