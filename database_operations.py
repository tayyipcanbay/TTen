import csv
import os

users_db_path = "data/users.csv"
queries_db_path = "data/queries.csv"


def create_users_db():
    if not os.path.exists(users_db_path):
        with open(users_db_path, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["user_id", "api_key, mail"])


def get_length_of_users_db():
    with open(users_db_path, "r") as file:
        reader = csv.reader(file)
        return len(list(reader))


def find_user_by_token(token):
    with open(users_db_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == token:
                return row[0]
    return False


def find_user_by_id(user_id):
    with open(users_db_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user_id:
                return row[1]
    return None

def create_user_if_not_exists(token, mail):
    if find_user_by_token(token) is False:
        with open(users_db_path, "a") as file:
            writer = csv.writer(file)
            id = get_length_of_users_db() + 1
            writer.writerow([id, token, mail])
            return id
    else:
        return find_user_by_token(token)

#################################################


def create_queries_db():
    if not os.path.exists(queries_db_path):
        with open(queries_db_path, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["query_id", "user_id", "query", "answer"])


def get_length_of_queries_db():
    with open(queries_db_path, "r") as file:
        reader = csv.reader(file)
        return len(list(reader))


def create_query(user_id, query, answer=None):
    with open(queries_db_path, "a") as file:
        writer = csv.writer(file)
        id = get_length_of_queries_db() + 1
        writer.writerow([id, user_id, query, answer])
        return id


def get_single_query(query_id):
    with open(queries_db_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == query_id:
                return row
    return None


def get_all_queries_by_user_id(user_id):
    queries = []
    with open(queries_db_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == user_id:
                queries.append(row)
    return queries


def update_query_answer(query_id, answer):
    try:
        with open(queries_db_path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        with open(queries_db_path, "w") as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == query_id:
                    row[3] = answer
                writer.writerow(row)
                return query_id, True
    except:
        return query_id, False

create_users_db()