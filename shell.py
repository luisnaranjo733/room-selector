
from sys import argv

from roomSelector.database import init_db, db_session
from roomSelector.models import User

init_db()

if __name__ == '__main__':
    if len(argv) == 1:
        print('Create is -c')
        print('List is -c')
        print('Delete is -d')
        exit(1)

    flag = argv[1]

    if flag == '-c':
        u = User(name='luis')
        db_session.add(u)
        db_session.commit()

    elif flag == '-l':
        print('Users:')
        for user in User.query.all():
            print('\t%r (%s)' % (user, user.phone))
        print('')
    elif flag == '-d':
        User.query.delete()
        db_session.commit()
else:
    luis = User.query.filter(User.name == 'Luis Naranjo').first()