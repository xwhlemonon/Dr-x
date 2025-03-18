from flask import jsonify
from werkzeug.exceptions import HTTPException

from api.core.json_result import JsonResult


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_error(e):
        return jsonify(JsonResult.ERROR.to(message=str(e))), e.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        app.logger.error(f'Unexpected error: {e}')
        return jsonify(JsonResult.ERROR.to(message=str(e))), 500
