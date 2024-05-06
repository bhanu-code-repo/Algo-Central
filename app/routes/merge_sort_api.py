
from flask import Blueprint, request, jsonify
from app.algo.merge_sort import merge_sort
from . import merge_sort_bp

@merge_sort_bp.route('/merge-sort', methods=['POST'])
def mergesort():
    data = request.json
    array = data['array']
    aux = array.copy()
    sorted_array = merge_sort(array, aux, 0, len(array) - 1)
    return jsonify(sorted_array), 200