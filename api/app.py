import logging

from flask import Flask

from apps.user import user_manager
from core.handler_exception import register_error_handlers

logging.basicConfig(  #
    level=logging.INFO,  #
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  #
    handlers=[logging.StreamHandler()]  #
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
register_error_handlers(app)
app.register_blueprint(user_manager, url_prefix='/user')


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello World!'


if __name__ == '__main__':
    logger.info('''
    Starting app...
    ''')
    app.run(debug=True, host='0.0.0.0', port=9090)
