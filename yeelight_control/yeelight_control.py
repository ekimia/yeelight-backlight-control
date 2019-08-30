import json
import logging

from flask import (
    Blueprint,
    jsonify,
    request,
)

from yeelight import Bulb
from yeelight.utils import rgb_to_yeelight

from typing import (
    Any,
    List,
    Optional,
)

BULB_IPS = [
    '192.168.7.249',
    '192.168.7.250',
    '192.168.7.251',
    '192.168.7.252',
]


bp = Blueprint('yeelight_control', __name__, url_prefix='/yeelight-control')


@bp.route('/turn-on', methods=['POST'])
def turn_on():
    content = request.get_json(silent=True)
    print(request.data)
    _send_command_to_all_bulbs('bg_set_power', params=['on'])

    body = json.loads(request.data.decode('utf-8'))
    color = body.get('color').lower()

    rbg_value = None
    if color == 'red':
        rbg_value = (255, 0, 0)
    elif color == 'blue':
        rbg_value = (0, 0, 255)
    elif color.lower() == 'shiva':
        rbg_value = (0, 255, 0)
    elif color == 'gold':
        rbg_value = hex_to_rbg_string('ffd998')
    elif color == 'pink':
        rbg_value = hex_to_rbg_string('ff18f1')
    elif color == 'light blue':
        rbg_value = hex_to_rbg_string('9bcaff')
    else:
        rbg_value = hex_to_rbg_string(color.lower())

    for ip in BULB_IPS:
        bulb = Bulb(ip)
        print(bulb)
        try:
            bulb.turn_on()
            bulb.send_command('bg_set_rgb', [rgb_to_yeelight(*rbg_value)])
        except Exception as e:
            print(f'nope {e}')

    return jsonify()


@bp.route('/turn-off', methods=['POST'])
def turn_off():
    _send_command_to_all_bulbs('bg_set_power', params=['off'])

    return jsonify()


def _send_command_to_all_bulbs(command: str, params: Optional[List[Any]] = None):
    for ip in BULB_IPS:
        bulb = Bulb(ip)
        print(bulb)
        try:
            bulb.turn_on()
            bulb.send_command(command, params)
        except Exception as e:
            print(f'nope {e}')


def hex_to_rbg_string(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
