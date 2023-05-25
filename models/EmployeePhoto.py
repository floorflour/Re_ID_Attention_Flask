from models._db import db


class EmployeePhoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empid = db.Column(db.String(50), unique=True)
    photoid = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"Employee(id={self.id}, empid='{self.empid}', photoid='{self.photoid}'')"

    def create(self, empid, photoid):
        photo = EmployeePhoto(empid=empid, photoid=photoid)
        db.session.add(photo)
        db.session.commit()

    def delete(self, id):
        photo = EmployeePhoto.query.get(id)
        db.session.delete(photo)
        db.session.commit()

    def update(self, id, empid=None, photoid=None):
        photo = EmployeePhoto.query.get(id)
        if empid:
            photo.empid = empid
        if photoid:
            photo.photoid = photoid
        db.session.commit()

    def get_by_id(self, id):
        return EmployeePhoto.query.get(id)

    def get_all(self):
        return EmployeePhoto.query.all()
