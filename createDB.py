import random
import sqlite3

with sqlite3.connect("persons.db") as db:
    cursor = db.cursor()


create_txt = """CREATE TABLE IF NOT EXISTS person_access_table(
                id integer PRIMARY KEY,
                person_name text NOT NULL ,
                person_id text NOT NULL ,
                n_key integer ,
                n_card integer ,
                n_finger integer ,
                pic_path text NOT NULL);
                """
cursor.execute(create_txt)

name = "محمد سینا ریماز"
iid = 12345668

for i in range(1,21):
    name_ = name + str(i)
    id_ = iid + 10*i
    n_key = random.randint(0,3)
    n_finger = random.randint(0,3)
    n_card = random.randint(0,3)
    path = 'person image/{}.jpg'.format(i)
    insert_execute = """INSERT INTO person_access_table (id,person_name,person_id,
                        n_key,n_card,n_finger,pic_path) VALUES(?,?,?,?,?,?,?)"""
    cursor.execute(insert_execute,(i,name_,str(id_),n_key,n_card,n_finger,path))
    db.commit()