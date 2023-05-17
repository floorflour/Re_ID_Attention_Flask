
from flask import Flask, request
from models.Users import Users
from models.AttentionTable import AttentionTable
from models._db import db
from flask_cors import CORS
from utils.log import init_logger
from utils.json import success, fail
import datetime
app = Flask(__name__)
CORS(app)

db_path = "sqlite:////home/ubuntu/python_workspace/ReID_Attention/api/ReidAttention.db"
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

logger = init_logger("日志")


@app.route('/testget', methods=['GET'])
def test():
    return success('test_____success!')


@app.route('/attention_search', methods=['POST'])
def attention_search():
    print(request.json)
    return success(f"success !!!!!")


@app.route('/testpost', methods=['POST'])
def testpost():
    print(request.json)
    input1 = request.json.get('input1')
    input2 = request.json.get('input2')
    return success(f"input1:{input1}input2:{input2}")


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = Users.query.filter_by(username=username, password=password).first()

    if user:
        return success(user)
    else:
        return fail("用户名或者密码错误！")


if __name__ == '__main__':
    # app.run(debug=True)
    # a = AttentionTable.query.filter_by()
    # 添加记录
    attentionTable = AttentionTable()
    with app.app_context():
        attentionTable.create(time=datetime.datetime.today(),
                              recognition_type='人脸识别', emp_id=1)
        results = attentionTable.get_all()
        print(results)

    # # 删除ID为2的记录
    # AttentionTable.delete(2)

    # # 修改ID为3的记录类型
    # AttentionTable.update(3, recognition_type='指纹识别')

    # # 查询ID为4的记录
    # result = AttentionTable.get_by_id(4)

    # # 查询所有记录
