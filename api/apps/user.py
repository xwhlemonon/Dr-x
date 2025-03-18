from flask import Blueprint, jsonify

from api.core.json_result import JsonResult

user_manager = Blueprint('user_manager', __name__)


@user_manager.route("/<user_id>")
def get_user(user_id):
    return jsonify(JsonResult.SUCCESS.to(data={"user_id": user_id}))
