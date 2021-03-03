from models.db import db, app
from models.user import User as UserModel
import sys,os

if __name__ == '__main__':
    command =  sys.argv[1]
    if command == 'build':
        db.create_all()
        print('created successfully')
    elif command == 'update':
        admin = UserModel(username='admin', email='admin@example.com')
        guest = UserModel(username='guest', email='guest@example.com')
        db.session.add(admin)
        db.session.add(guest)
        db.session.commit()
    elif command == 'clean':
        db.drop_all()
    elif command == 'query':
        user = UserModel.query.filter_by(username='admin').first()
        print(user.email)
    else:
        print("command not supported!")