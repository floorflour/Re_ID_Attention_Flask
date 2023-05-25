from models._db import db
from models.Employee import Employee


class AttentionTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    recognition_type = db.Column(db.String(50))
    emp_id = db.Column(db.Integer)

    def __repr__(self):
        return f"AttendanceResult(id={self.id}, time='{self.time}', recognition_type='{self.recognition_type}', emp_id={self.emp_id})"

    def create(self, time, recognition_type, emp_id):
        result = AttentionTable(
            time=time, recognition_type=recognition_type, emp_id=emp_id
        )
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

    def search(
        self,
        name=None,
        start_time=None,
        end_time=None,
        emp_id=None,
        reco_type=None,
        offset=0,
        limit=None,
    ):
        query = self.query
        if name:
            emp_ids = []
            emp_ids = [e.id for e in Employee.query.filter(Employee.name == name)]
            emp_ids += [
                e.id for e in Employee.query.filter(Employee.name.ilike(f"%{name}%"))
            ]
            query = query.filter(AttentionTable.emp_id.in_(emp_ids))

        if start_time:
            query = query.filter(AttentionTable.time >= start_time)
        if end_time:
            query = query.filter(AttentionTable.time <= end_time)
        if emp_id:
            query = query.filter(AttentionTable.emp_id == emp_id)
        if reco_type:
            query = query.filter(AttentionTable.recognition_type == reco_type)
        query = query.offset(offset).limit(limit)
        attentions = query.all()
        return attentions

    def get_all(self):
        return AttentionTable.query.all()
