import csv
from user_txt_operations import get_table_length

path= "data/user_data.csv"

def create_user_csv_file():
    """Create a csv file to store the user data"""
    with open( path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['user_id','user_mac' ,'user_ip'])

def find_user_id(user_mac):
    """Find the user id from the csv file"""
    with open( path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[1] == user_mac:
                return row[0]
        return False

def add_new_user(user_mac,user_ip):
    if find_user_id(user_mac=user_mac):
        return find_user_id(user_mac=user_mac)
    else:
        with open( path, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            temp_id= get_table_length()+1
            csv_writer.writerow([temp_id, user_mac, user_ip])
        return temp_id

def create_user_if_not_exists(user_mac, user_ip):
    if not find_user_id(user_mac=user_mac):
        temp_id= add_new_user(user_mac=user_mac, user_ip=user_ip)
        return temp_id
    else:
        return find_user_id(user_mac=user_mac)
