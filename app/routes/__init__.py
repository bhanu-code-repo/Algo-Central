from flask import Blueprint

binary_search_bp = Blueprint('binary_search', __name__)
merge_sort_bp = Blueprint('merge_sort', __name__)

from . import binary_search_api
from . import merge_sort_api