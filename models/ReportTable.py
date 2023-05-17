
from models._db import db


class ReportTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    recognition_type = db.Column(db.String(50))
    emp_id = db.Column(db.Integer)

    def __repr__(self):
        return f"AttendanceResult(id={self.id}, time='{self.time}', recognition_type='{self.recognition_type}', emp_id={self.emp_id})"
