import sys
from roomSelector import app

DEBUG = True

if DEBUG:
    host = '127.0.0.1'
    port = '5000'
else:
    host = '69.91.176.28'
    port = '80'
    
if len(sys.argv) > 1:
    host, port = sys.argv[1].split(':')

app.run(host, int(port), debug=True)
