import csv 

path="data/query_data.csv"

def create_query_txt_csv_file():
    """Create a csv file to store the query data"""
    with open( path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['query_id','query_txt', 'query_response' ,'user_id'])

def get_table_length():
    """Get the length of the csv file"""
    with open( path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        length = 0
        for row in csv_reader:
            length += 1
        return length

#add a new data to last row of csv file
def add_new_query(query_txt, user_id, query_response=None):
    """Add a new query to the csv file"""
    with open( path, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        temp_id= get_table_length()+1
        csv_writer.writerow([temp_id, query_txt, query_response, user_id])
        return temp_id

def update_query_response(query_id, query_response):
    """Update the query response in the csv file"""
    with open( path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        query_array = []
        for row in csv_reader:
            if row[0] == query_id:
                row[2] = query_response
            query_array.append(row)
    with open('query_data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in query_array:
            csv_writer.writerow(row)

def find_user_queries(user_id):
    """Find the user queries from the csv file"""
    with open( path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        query_array = []
        for row in csv_reader:
            if row[3] == user_id:
                query_array.append(row)
        return user_id, query_array
