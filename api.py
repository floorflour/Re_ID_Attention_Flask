from flask import Flask, jsonify
from models import AttentionTable
from flask import Flask, jsonify, request
from models.Users import Users
from search_all import search_all
from change_model import change_model
from update_model import update_model
from models._db import db
from flask_cors import CORS
from utils.log import init_logger
from utils.json import success, fail

app = Flask(__name__)
CORS(app)

app.register_blueprint(search_all)
app.register_blueprint(change_model)
app.register_blueprint(update_model)

db_path = "sqlite:////home/ubuntu/python_workspace/ReID_Attention/api/ReidAttention.db"
app.config["SQLALCHEMY_DATABASE_URI"] = db_path
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

logger = init_logger("日志")


@app.route("/testget", methods=["GET"])
def test():
    return success("test_____success!")


@app.route("/testpost", methods=["POST"])
def testpost():
    print(request.json)
    input1 = request.json.get("input1")
    input2 = request.json.get("input2")
    return success(f"input1:{input1}input2:{input2}")


# @app.route('/serach_all', methods=['POST'])
# def search_all():
#     page_num = request.args.get('pageNum')
#     page_size = request.args.get('pageSize')

#     query = AttentionTable.query
#     total = query.count()  # 获取总条数

#     query = query.limit(page_size).offset((page_num - 1) * page_size)
#     attentions = query.all()

#     attentions_json = []
#     for attention in attentions:
#         attention_json = {
#             'id': attention.id,
#             'time': attention.time.isoformat(),
#             'recognition_type': attention.recognition_type,
#             'emp_id': attention.emp_id
#         }

#     return jsonify({
#         'list': attentions_json,
#         'totalCount': total  # 返回总条数
#     })


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    user = Users.query.filter_by(username=username, password=password).first()

    if user:
        return success(user)
    else:
        return fail("用户名或者密码错误！")


if __name__ == "__main__":
    app.run(debug=True)
