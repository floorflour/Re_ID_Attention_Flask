from flask import jsonify


def success(data=None):
    return response(code=0, msg="success", data=data)


def fail(msg):
    return response(code=-1, msg=msg)


def response(code, msg, data=''):
    return jsonify({'code': code, 'msg': msg, 'data': data})
