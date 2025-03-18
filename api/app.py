import logging

from flask import Flask, jsonify

from api.core.json_result import JsonResult
from apps.user import user_manager
from core.handler_exception import register_error_handlers

logging.basicConfig(  #
    level=logging.DEBUG,  #
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  #
    handlers=[logging.StreamHandler()]  #
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
register_error_handlers(app)
app.register_blueprint(user_manager, url_prefix='/user')


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(JsonResult.SUCCESS.to())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
    logger.info('''
    Starting app...
    ''')
