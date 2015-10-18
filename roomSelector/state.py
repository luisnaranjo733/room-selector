import os
import sys

from roomSelector.database import init_db, db_session
from roomSelector.models import User
import roomSelector

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
selection_file = os.path.join(PROJECT_ROOT, 'selectionOn.txt')



def selectionStatus():
    return os.path.exists(selection_file)
    
def startSelection():
    open(selection_file, 'a').close()
    for user in User.query.filter(User.is_live_in==True).all():
        user.has_selected = False

    db_session.commit()
    
def stopSelection():
    if os.path.exists(selection_file):
        os.remove(selection_file)

