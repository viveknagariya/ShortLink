import os
from pathlib import Path

from flask import Flask, request
from sqlalchemy import inspect

from .config import Config
from .extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    os.makedirs(app.instance_path, exist_ok=True)

    database_uri = app.config.get("SQLALCHEMY_DATABASE_URI", "")
    if database_uri.startswith("sqlite:///") and not database_uri.startswith(
        "sqlite:////"
    ):
        database_name = database_uri.removeprefix("sqlite:///")
        if database_name in {"", "app.db"}:
            app.config["SQLALCHEMY_DATABASE_URI"] = (
                f"sqlite:///{(Path(app.instance_path) / 'app.db').resolve().as_posix()}"
            )
        elif not os.path.isabs(database_name):
            app.config["SQLALCHEMY_DATABASE_URI"] = (
                f"sqlite:///{(Path(app.instance_path) / database_name).resolve().as_posix()}"
            )

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main_bp

    app.register_blueprint(main_bp)

    def ensure_database():
        with app.app_context():
            inspector = inspect(db.engine)
            existing_tables = set(inspector.get_table_names())
            required_tables = set(db.metadata.tables.keys())

            if not required_tables.issubset(existing_tables):
                db.create_all()

    ensure_database()
    app.config["_DB_READY"] = True

    @app.before_request
    def _ensure_database_ready():
        if not app.config.get("_DB_READY", False):
            ensure_database()
            app.config["_DB_READY"] = True

    @app.after_request
    def _disable_css_cache(response):
        if request.path.endswith("/static/css/style.css"):
            response.headers["Cache-Control"] = (
                "no-store, no-cache, must-revalidate, max-age=0"
            )
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        from flask import render_template

        return render_template("404.html"), 404

    return app
