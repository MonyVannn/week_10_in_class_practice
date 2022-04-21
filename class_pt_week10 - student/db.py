from nis import cat
import mysql.connector
import prettytable

'''
State your group member name and id here:
1. 2022119vin - Hellan VIN
2. 2022015huor - Viraksith HUOR
3. 2022147men - Monyvann MEN

'''


# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cat_db",
    port="8889"
)


cursor = mydb.cursor()


def register_cat(cat_info):
    sql = f"INSERT INTO cats (name, gender, breed, dob, description) VALUES ('{cat_info[0]}', '{cat_info[1]}', '{cat_info[2]}', '{cat_info[3]}', '{cat_info[4]}')"
    cursor.execute(sql)

    mydb.commit()



def get_cats():
    sql = "SELECT * FROM cats"
    cursor.execute(sql)
    result = cursor.fetchall()

    return result


def get_cat(id):
    sql = f"SELECT * FROM cats WHERE id LIKE {id}"
    cursor.execute(sql)
    result = cursor.fetchone()
    
    return result[0], result[1], result[2], result[3], result[4], result[5]



def update_cat(cat_update_data):
    sql = f"UPDATE cats SET name = '{cat_update_data[1]}', gender = '{cat_update_data[2]}', breed = '{cat_update_data[3]}', dob = '{cat_update_data[4]}', description = '{cat_update_data[5]}' WHERE id = {cat_update_data[0]}"
    cursor.execute(sql)

    mydb.commit()


def remove_cat(id):
    sql = f"DELETE FROM cats WHERE id = {id}"
    cursor.execute(sql)

    mydb.commit()
