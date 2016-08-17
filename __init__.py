from flask import Flask
import os
from views.record import record


app = Flask(__name__)

app.config.from_object('config')

app.register_blueprint(record)

ip = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', 8080))

app.run(ip,port,True)