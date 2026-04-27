import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-key-keep-it-secret"

    instance_path = Path(__file__).parent.parent / "instance"
    instance_path.mkdir(exist_ok=True)

    db_url = os.environ.get("DATABASE_URL")
    if (
        db_url
        and db_url.startswith("sqlite:///")
        and not db_url.startswith("sqlite:////")
    ):
        db_name = db_url.replace("sqlite:///", "")
        SQLALCHEMY_DATABASE_URI = (
            f"sqlite:///{(instance_path / db_name).resolve().as_posix()}"
        )
    else:
        SQLALCHEMY_DATABASE_URI = (
            f"sqlite:///{(instance_path / 'app.db').resolve().as_posix()}"
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "timeout": 30,
            "check_same_thread": False,
        }
    }

    SHORT_URL_DOMAIN = os.environ.get("SHORT_URL_DOMAIN") or "http://127.0.0.1:5000"
