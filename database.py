import sqlite3

DBNAME = "MoviesData.db"

def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()
#init_db()

#############################################################
def creat_table():
    query = '''
        CREATE TABLE IF NOT EXISTS movies
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        imdb_rate REAL,
        year TEXT,
        country TEXT,
        image TEXT
        )
        '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

#creat_table()

def insert_record(title,imdb_rate,year,country,image):
    query = ''' 
            INSERT INTO movies(title,imdb_rate,year,country,image)
            VALUES(?,?,?,?,?)
            '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(title,imdb_rate,year,country,image))
    conn.commit()
    conn.close()

# insert_record("The Pianist",8.5,"2002","France, Poland, Germany, UK","https://www.moviesapi.ir/images/tt0253474_poster.jpg")
# insert_record("The Great Dictator",8.5,"1940","USA","https://www.moviesapi.ir/images/tt0032553_poster.jpg")
# insert_record("12 Angry Men",8.9,"1954","USA","https://www.moviesapi.ir/images/tt0050083_poster.jpg")
# insert_record("The Matrix",8.7,"1999","USA","https://www.moviesapi.ir/images/tt0133093_poster.jpg")
# insert_record("Oldboy",8.4,"2003","South Korea","http://moviesapi.ir/images/tt0364569_poster.jpg")

# ############################################################

def select_all_records():
    query = 'SELECT * FROM movies'

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows

#print(select_all_records())
#########################################################

def select_record_by_id(id):
    query = 'SELECT *FROM movies WHERE id = ? '
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query,(id,)).fetchone()
    conn.close()
    return row

#print(select_record_by_id(2))
##############################################
def select_record_by_title(title):
    query = ' SELECT * FROM movies WHERE title=? '
    conn = sqlite3.Connection(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query,(title,)).fetchone()
    conn.close()
    return row

#print(select_record_by_title("Pulp Fiction"))

#################################################
def select_record_by_imdb_rate(imdb_rate):
    query = ' SELECT * FROM movies WHERE imdb_rate=? '
    conn = sqlite3.Connection(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query,(imdb_rate,)).fetchall()
    conn.close()
    return row

#print(select_record_by_imdb_rate(9.0))
    
#################################################
def delete_record_by_id(id):
    query = 'DELETE FROM movies WHERE id = ? '

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(id,))
    conn.commit()
    conn.close()
#################################################
def delete_record_by_title(title):
    query = 'DELETE FROM movies WHERE title=? '

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(title,))
    conn.commit()
    conn.close()

#################################################
def update_record_by_id(id,title,imdb_rate,year,country,image):
    query = '''
        UPDATE movies
        SET title = ?,
            imdb_rate= ? ,
            year = ?,
            country = ?,
            image = ?
        WHERE id = ?
            '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(title,imdb_rate,year,country,image,id))
    conn.commit()
    conn.close()

##############################################

def update_record_by_title(title,year,country,imdb_rate):
    query = '''
        UPDATE movies
        SET year=?, country=? , imdb_rate=?
        WHERE title=?
        '''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query,(year,country,imdb_rate,title))
    conn.commit()
    conn.close()
