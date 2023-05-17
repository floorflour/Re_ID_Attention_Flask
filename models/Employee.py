from models._db import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    personid = db.Column(db.String(50))
    mailaddress = db.Column(db.String(50))

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', personid='{self.personid}',mailaddress='{self.mailaddress}')"
