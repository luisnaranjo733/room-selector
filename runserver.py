import sys
from roomSelector import app

DEBUG = False

if DEBUG:
    host = '127.0.0.1'
    port = '5000'
else:
    host = '192.168.1.27'
    port = '80'

if len(sys.argv) > 1:
    host, port = sys.argv[1].split(':')

app.run(host, int(port), debug=True)
