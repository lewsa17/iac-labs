# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os


class Config:

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.getenv("SECRET_KEY", "S#perS3crEt_007")

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets Management
    ASSETS_ROOT = os.getenv("ASSETS_ROOT", "/static/assets")


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = (
        f"{os.getenv('DB_ENGINE', 'postgresql')}://"
        f"{os.getenv('DB_USERNAME', 'appseed_db_usr')}:"
        f"{os.getenv('DB_PASS', 'A0yzveIbDVugnPpIUywLDnl8XPNm3f2p')}@"
        f"{os.getenv('DB_HOST', 'dpg-clmbtgcjtl8s73aig360-a.oregon-postgres.render.com')}:"
        f"{os.getenv('DB_PORT', '5432')}/"
        f"{os.getenv('DB_NAME', 'appseed_db_0v8k')}"
    )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {"Production": ProductionConfig, "Debug": DebugConfig}
