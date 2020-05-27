from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine, pool

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@migrate.configure
def configure_alembic(cfg):
    engine = create_engine(
        migrate.db.engine.url,
        poolclass=pool.NullPool,
        connect_args={"connect_timeout": 5},
    )
    cfg.attributes["connection"] = engine

    return cfg


from app import models
