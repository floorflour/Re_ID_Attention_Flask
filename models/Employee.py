from models._db import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    personid = db.Column(db.String(50))
    mailaddress = db.Column(db.String(50))

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', personid='{self.personid}',mailaddress='{self.mailaddress}')"

    def create(self, name, personid, mailaddress):
        emp = Employee(name=name, personid=personid, mailaddress=mailaddress)
        db.session.add(emp)
        db.session.commit()

    def delete(self, id):
        emp = Employee.query.get(id)
        db.session.delete(emp)
        db.session.commit()

    def update(self, id, name=None, personid=None, mailaddress=None):
        emp = Employee.query.get(id)
        if name:
            emp.name = name
        if personid:
            emp.personid = personid
        if mailaddress:
            emp.mailaddress = mailaddress
        db.session.commit()

    def get_by_id(self, id):
        return Employee.query.get(id)

    def get_name_by_id(self, emp_id):
        emp = Employee.query.get(emp_id)
        return emp.name

    def get_all(self):
        return Employee.query.all()
