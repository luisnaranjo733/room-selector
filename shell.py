
from sys import argv

from roomSelector.database import init_db, db_session
from roomSelector.models import User, UserType, Room, House

init_db()

def query_all_db_items():
    tables = [User, UserType, Room, House]
    results = {}
    for table in tables:
        results[table.__tablename__] = table.query.all()
    return results



if __name__ == '__main__':
    if len(argv) == 1:
        print('Create is -c')
        print('List is -c')
        print('Delete is -d')
        exit(1)

    flag = argv[1]

    if flag == '-c':
        ut_common = UserType()
        ut_common.name = 'common'
        db_session.add(ut_common)

        ut_admin = UserType()
        ut_admin.name = 'admin'
        db_session.add(ut_admin)


        u_admin = User(name='luis', email='luis@gmail.com', password_hash='test')
        u_admin.type = ut_admin
        db_session.add(u_admin)

        u_common = User(name='nick', email='nick@gmail.com', password_hash='test')
        u_common.type = ut_common
        db_session.add(u_common)


        h = House()
        h.name =  'phi delts'
        h.manager = u_admin
        db_session.add(h)


        r =  Room()
        r.house = h
        db_session.add(r)

        db_session.commit()

    elif flag == '-l':
        db_items = query_all_db_items()
        for item in db_items:
            print item.upper()
            print db_items[item]
            print ' '

    elif flag == '-d':
        User.query.delete()
        UserType.query.delete()
        db_session.commit()

    exit(0)

items = query_all_db_items()
h = items['house'][0]
r = items['room'][0]
u = items['user'][0]
ut = items['user_type'][0]
