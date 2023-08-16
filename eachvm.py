import docker
import requests
import datetime
import json
from flask import Flask

app = Flask(__name__)

containers = dict()

start_time = 0
stop_time = 0

def check_for_backup(mail):
    pass

def backup_data(mail):
    if check_for_backup(mail) is True:
        pass

def create_file(mail):
    pass

def upload_data(mail, start_time, stop_time):
    pass

def start_container(mail):
    mailc = mail.replace('@', '-')
    client = docker.from_env()
    container_name = mailc
    image_name = "flask:v1"
    container = client.containers.run(image_name, detach=True, name=container_name)
    containers[mailc] = container
    start_time = datetime.datetime.now()
    create_file(mail)

def stop_container(mail):
    mailc = mail.replace('@', '-')
    containers[mailc].stop()
    containers[mailc].remove()
    stop_time = datetime.datetime.now()
    upload_data(mail, start_time, stop_time)
    backup_data(mail)

@app.route('/')
def hello_world():
    return "This is each VM server"

@app.route('/start/<mail>', methods=['POST'])
def start(mail):
    start_container(mail)
    return "Container started for {}".format(mail)

@app.route('/stop/<mail>', methods=['POST'])
def stop(mail):
    stop_container(mail)
    return "Container stopped for {}".format(mail)

if __name__ == '__main__':
    app.run(port=8000)
