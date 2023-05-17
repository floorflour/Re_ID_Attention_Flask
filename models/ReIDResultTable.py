
from models._db import db


class ReIDResultTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    photo_url = db.Column(db.Integer)
    emp_id = db.Column(db.Integer)
    result = db.Column(db.Boolean)

    def __repr__(self):
        return f"ReIDResult(id={self.id}, photo_url={self.photo_url}, emp_id={self.emp_id}, result={self.result})"

    def create(self, time, photo_url, emp_id, result):
        reid_result = ReIDResultTable(
            time=time, photo_url=photo_url, emp_id=emp_id, result=result)
        db.session.add(reid_result)
        db.session.commit()

    def delete(self, id):
        result = ReIDResultTable.query.get(id)
        db.session.delete(result)
        db.session.commit()

    def update(self, id, time=None, photo_url=None, emp_id=None, result=None):
        result = ReIDResultTable.query.get(id)
        if time:
            result.time = time
        if photo_url:
            result.photo_url = photo_url
        if emp_id:
            result.emp_id = emp_id
        if result:
            result.result = result
        db.session.commit()

    def get_by_id(self, id):
        return ReIDResultTable.query.get(id)

    def get_all(self):
        return ReIDResultTable.query.all()
