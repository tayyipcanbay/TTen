from flask import Flask, request
from tesseract_operations import tesseract_it
from user_operations import create_user_if_not_exists
from user_txt_operations import add_new_query
from python_arptable import get_arp_table
import os

app= Flask(__name__)

def read_txt(path):
    with open(path, 'r') as f:
        return f.read()

def get_client_mac(ip):
    arp_table = get_arp_table()
    for entry in arp_table:
        if entry['IP address'] == ip:
            return entry['HW address']
    return None

@app.route('/')
def index():
    return 'Hello World'

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files
    sender_ip = request.remote_addr
    sender_mac = get_client_mac(sender_ip)
    user_id= create_user_if_not_exists(user_mac=sender_mac, user_ip=sender_ip)
    if user_id == None:
        return 'failed'
    for file in files:
        temp_path= os.path.join('incoming-image', files[file].filename)
        files[file].save(temp_path)
        query_txt= tesseract_it(temp_path)
        if query_txt:
            query_id= add_new_query(query_txt=query_txt, user_id=user_id)
            return str(query_id)
        else:
            return 'failed'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3131, debug=True)
