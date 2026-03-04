import sqlite3
db = sqlite3.connect("firstdb.db")
cr=db.cursor()

cr.execute("delete from users where progres = 1 ")
db.commit()

def get_data():

    try :

        cr.execute("select * from users ")
        data =  cr.fetchall()
        print (f"db har {len(data)} raws ")
        print ("this is the users names and id :")
        for raws in data :
            print (f" user {raws[2]} name : {raws[0]}")


    except sqlite3.Error as er :

        print(f"there is an eror : {er} ")

    finally:

        print ( "data base is closed ")
        db.close()



get_data()