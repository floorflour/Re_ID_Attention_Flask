import logging
import threading
import time
from flask import jsonify
from flask import Blueprint
from utils.json import response
from threading import Timer


update_model = Blueprint("update_model", __name__)

is_running = False
error = False


@update_model.route("/update_model", methods=["GET"])
def update_model_f():
    global is_running
    global error
    print(f"is_running:{is_running}")
    print(f"error:{error}")
    if is_running:
        if error:
            return response(code=-1, msg="模型更新失败,请联系管理员")
        else:
            return response(code=-1, msg="模型更新中……请勿重复操作")

    is_running = True
    thread = threading.Thread(target=model_updating)
    thread.start()

    # 3小时后结束线程
    timer = threading.Timer(3 * 3600, set_stop_flag)
    timer.start()

    return jsonify(code=0, msg="模型更新进程已启动")


def set_stop_flag():
    global is_running
    is_running = False
    Timer.cancel()  # 如果发生错误,取消定时器


def model_updating():
    global is_running
    global error

    try:
        logging.info("模型更新开始")
        print(1)
        time.sleep(10)
        print(2)
        logging.info("模型更新成功")
    except:
        error = True
        logging.error("模型更新失败")

    finally:
        is_running = False
