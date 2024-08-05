from flask import Blueprint

from .routes import login_manager, index_manager

bp = Blueprint('admin', __name__, url_prefix='/admin')

bp.add_url_rule('/login_manager', 'login_manager', login_manager, methods=["GET", "POST"])
bp.add_url_rule("/index_manager", 'index_manager', index_manager, methods=["GET", "POST"])