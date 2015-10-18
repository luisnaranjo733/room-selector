
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


user_data = '''Hassam Farooq,farooh@uw.edu,40,common,1
Glen Kabacheuski,glenk@uw.edu,45,common,2
Jason Mukai,jmukai@uw.edu,50,common,3
Eric Page,epage@uw.edu,45,admin,4
Joey Bell,joeyb@uw.edu,60,common,5
Alex Tielker,atielk@uw.edu,70,admin,6
Tyler Nakagawa,tnak14@uw.edu,50,common,7
Daniel Karpman,dkarp@uw.edu,35,common,8
Ethan McGregor,ermmcgregor@uw.edu,25,common,9
Nicholas Polsin,nickyp@uw.edu,39,common,10'''


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

        u_common = User(name='raj', email='raj@gmail.com', password_hash='test')
        u_common.type = ut_common
        db_session.add(u_common)

        h = House()
        h.name =  'phi delts'
        h.manager = u_admin
        db_session.add(h)

        for i in range(10):
            room = Room()
            room.house = h
            db_session.add(room)
            db_session.commit()


        for line in user_data.split('\n'):
            name, email, points, user_type, room = line.split(',')
            room = Room.query.filter(Room.id == int(room)).first()
            user_type = UserType.query.filter(UserType.name == user_type).first()
            user = User(name=name)
            user.email = email
            user.house_points = points
            user.type = user_type
            user.room = room
            db_session.add(user)
            db_session.commit()








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

