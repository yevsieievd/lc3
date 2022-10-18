
import sqlite3

db = 'lc3.db'

def create_tb_movie():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS movie(
    movieid INTEGER NOT Null PRIMARY KEY AUTOINCREMENT,
    title varchar(50) NOT NULL,
    year int NOT NULL,
    score float NOT NULL
    )
    '''
    cur.execute(sql)
    con.close()

def drop_movies():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = 'DROP TABLE IF EXISTS movie'
    cur.execute(sql)
    con.close()


def ins_data():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''   
     INSERT INTO movie  (title, year, score)
     VALUES       
     ("Monty Python and the Holy Grail", 1975, 8.2),       
     ("And Now for Something Completely Different", 1971, 7.5),
     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
     ("Monty Python's The Meaning of Life", 1983, 7.5),
     ("Monty Python's Life of Brian", 1979, 8.0)
    '''
    cur.execute(sql)
    con.commit()
    con.close()


def prn_movies():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''   
     SELECT movieid, year, title FROM movie ORDER BY year
    '''
    for row in cur.execute(sql):
        print(row)
    con.close()


def prn_movies_by_score():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = 'SELECT score movieid, year, title FROM movie ORDER BY score DESC'
    for row in cur.execute(sql):
        print(row)
    con.close()


def update_movie():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''   
    UPDATE movie
    SET  score = 8.3
    WHERE title = 'Monty Python and the Holy Grail'
    '''
    cur.execute(sql)
    con.commit()
    con.close()


def del_movie():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = "DELETE FROM movie WHERE title = 'Monty Python Live at the Hollywood Bowl'"
    cur.execute(sql)
    con.commit()
    con.close()


if __name__ == '__main__':
    drop_movies()
    create_tb_movie()
    ins_data()
    prn_movies()
    update_movie()
    prn_movies_by_score()
    del_movie()
    prn_movies_by_score()