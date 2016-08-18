import os
from application import app

ip = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', 8080))

app.run(ip,port,True)