from flask import Blueprint

memo_bp = Blueprint('memo', __name__, url_prefix='/memo')

from . import views 