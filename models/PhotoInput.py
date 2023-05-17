from models._db import db


class PhotoInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_time = db.Column(db.DateTime)
    photo_url = db.Column(db.String(255))
    recognitions = db.Column(db.String(255))
    status = db.Column(db.Boolean)   # 添加的状态字段

    def __repr__(self):
        return f"PhotoInput(id={self.id}, input_time='{self.input_time}', photo_url='{self.photo_url}', recognitions='{self.recognitions}', status={self.status})"
