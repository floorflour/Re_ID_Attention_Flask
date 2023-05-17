
from models._db import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    permission = db.Column(db.Enum('普通用户', '管理员'))

    def __repr__(self):
        return f"User(id={self.id}, emp_id={self.emp_id}, username='{self.username}', password='{self.password}', permission='{self.permission}')"

    def create(self, emp_id, username, password, permission):
        user = Users(emp_id=emp_id, username=username,
                     password=password, permission=permission)
        db.session.add(user)
        db.session.commit()

    def delete(self, id):
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()

    def update(self, id, emp_id=None, username=None, password=None, permission=None):
        user = Users.query.get(id)
        if emp_id:
            user.emp_id = emp_id
        if username:
            user.username = username
        if password:
            user.password = password
        if permission:
            user.permission = permission
        db.session.commit()

    def get_by_id(self, id):
        return Users.query.get(id)

    def get_all(self):
        return Users.query.all()
