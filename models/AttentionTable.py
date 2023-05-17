
from models._db import db


class AttentionTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    recognition_type = db.Column(db.String(50))
    emp_id = db.Column(db.Integer)

    def __repr__(self):
        return f"AttendanceResult(id={self.id}, time='{self.time}', recognition_type='{self.recognition_type}', emp_id={self.emp_id})"

    def create(self, time, recognition_type, emp_id):
        result = AttentionTable(
            time=time, recognition_type=recognition_type, emp_id=emp_id)
        db.session.add(result)
        db.session.commit()

    def delete(self, id):
        result = AttentionTable.query.get(id)
        db.session.delete(result)
        db.session.commit()

    def update(self, id, time=None, recognition_type=None, emp_id=None):
        result = AttentionTable.query.get(id)
        if time:
            result.time = time
        if recognition_type:
            result.recognition_type = recognition_type
        if emp_id:
            result.emp_id = emp_id
        db.session.commit()

    def get_by_id(self, id):
        return AttentionTable.query.get(id)

    def get_all(self):
        return AttentionTable.query.all()
