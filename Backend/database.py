import mysql.connector
import datetime

# Create a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Project2023",
    database="lego_store"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Define functions to execute SQL queries

def get_products():
    query = "SELECT * FROM Product"
    cursor.execute(query)
    result = cursor.fetchall()
    converted_result = []
    for row in result:
        dict_row = {'id': row[0],
                    'name': row[1],
                    'set_no': row[2],
                    'price': row[3],
                    'description': row[4],
                    'image': row[5],
                    'availability': row[6],
                    'release_date': datetime.datetime.strftime(row[7], "%Y-%m-%d"),
                    'piece_count': row[8],
                    'product_type_id': row[9]}
        converted_result.append(dict_row)
    return converted_result

def get_sets():
    query = "SELECT * FROM Set"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def create_user(username, password):
    query = "INSERT INTO User (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(query, values)
    db.commit()
    return cursor.lastrowid

def get_user_by_id(user_id):

    cursor.execute(f"SELECT * FROM user WHERE userId = {user_id}")
    row = cursor.fetchone()
    result = {'id': row[0],
              'username': row[1],
              'email': row[2],
              'password': row[3],
              'shopping_cart_id': row[4],
              'address_id': row[5]}
    return result

def get_user_by_username(username):

    cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")
    user = cursor.fetchone()
    #cursor.close()
    return user

def add_user(username, password):

    cursor.execute(f"INSERT INTO user (username, password) VALUES ('{username}', '{password}')")
    db.commit()
    user_id = cursor.lastrowid
    #cursor.close()
    return user_id

def update_user(user_id, username, password):

    cursor.execute(f"UPDATE user SET username = '{username}', password = '{password}' WHERE id = {user_id}")
    db.commit()
    #cursor.close()

def delete_user(user_id):

    cursor.execute(f"DELETE FROM user WHERE id = {user_id}")
    db.commit()
    #cursor.close()