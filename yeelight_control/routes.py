import os

from .yeelight_control import app


@app.route('/status')
def status():
    return os.environ.get('IMAGE_TAG', 'Dev')

