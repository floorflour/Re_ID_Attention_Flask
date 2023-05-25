from flask import jsonify, request
from models.AttentionTable import AttentionTable
from flask import Blueprint
from models.Employee import Employee

change_model = Blueprint("change_model", __name__)


@change_model.route("/change_model", methods=["POST"])
def change_model_f():
    print(request.json)
    name = request.json.get("name")
    timeend = request.json.get("timeend")
    timestart = request.json.get("timestart")
    method = request.json.get("method")
    pageSize = request.json.get("pageSize")
    currentPage = request.json.get("currentPage")
    at = AttentionTable()
    offset = (currentPage - 1) * pageSize
    limit = pageSize
    attentions = at.search(
        name=name,
        start_time=timestart,
        end_time=timeend,
        reco_type=method,
        offset=offset,
        limit=limit,
    )
    employee = Employee()
    attentions_json = []

    for attention in attentions:
        attention_json = {
            "id": attention.id,
            "name": employee.get_name_by_id(emp_id=attention.emp_id),
            "time": attention.time.isoformat(),
            "recognition_type": attention.recognition_type,
            "emp_id": attention.emp_id,
        }
        attentions_json.append(attention_json)
    print(jsonify(attentions_json))
    return jsonify(attentions_json)
