import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='melon',
                             db='us_states',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# Add new rows to the MySQL Table
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`states`, `password`) VALUES (%s, %s)"
        sql = "INSERT INTO states(id, state, population) VALUES(NULL, 'Wayne', '1')"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()