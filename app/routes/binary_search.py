from flask import request, jsonify, current_app
from . import binary_search_bp
from app.utils.binary_search_utils import binary_search_iterative, binary_search_recursive

@binary_search_bp.route('/api/v1/binary-search/iterative', methods=['POST'])
def handle_binary_search_iterative():
    try:
        nums = request.get_json()['nums']
        target = request.get_json()['target']
        result = binary_search_iterative(nums, target)
        return jsonify({'result': {'index': result, 'target': sorted(nums)[result], 'sorted nums': sorted(nums)}})
    except Exception as e:
        current_app.logger.error(e)

@binary_search_bp.route('/api/v1/binary-search/recursive', methods=['POST'])
def handle_binary_search_recursive():
    try:
        nums = request.get_json()['nums']
        target = request.get_json()['target']
        result = binary_search_recursive(nums, 0, len(nums) - 1, target)
        return jsonify({'result': {'index': result}})
    except Exception as e:
        current_app.logger.error(e)
