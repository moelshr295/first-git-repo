import sqlite3
db = sqlite3.connect("firstdb.db")
cr = db.cursor()
user_input = (input ("what do you want to do : \n - to sign up => s \n - to update => u \n - to delete => d \n to show your data => w \n >>> ")).strip().lower()


def sign_up() :
    new_user = input("whats your name : ").strip().lower()
    new_prog = input("what is you progras : ")
    cr.execute("select * from users_2 ")
    data =  cr.fetchall()
    new_id = len(data)+1
    cr.execute(f"insert into users_2 (name,progres,id) values ('{new_user}','{new_prog}',{new_id})")
    print(f"you are now a user \n your data name: {new_user} \n with the id {new_id} \n your progres is :{new_prog} ")
    
def delete()  :
        delete_name =input("what is the name of the user you want to delete : ").strip().lower()
        cr.execute("select * from users_2 where name = ?",(delete_name,))
        data =  cr.fetchall()
        if  data :
            cr.execute("delete from users_2 where name = ?",(delete_name,)) 
            print (f"user {delete_name} has been deleted ")    
        else :
            print ("that name is not here\nplese try again ")
        
def updating() :
     up_name = input("what is the name of the user :\n >>>").strip().lower()
     prog = input("what is the new progres you want to write : \n>>>")
     cr.execute("update users_2 set progres = ? where name = ?",(prog,up_name,))
     print(f"user {up_name} progres is updated to {prog} :)")




if user_input in ["s", "u" , "d" , "w"] : 
    print (f" you chose {user_input} .")
    if user_input == "s" :
        print("sining up")
        sign_up()

    if user_input == "d" :
         delete()
    
    if user_input == "u" : 
         print ('updating : ')
         updating()

    if user_input == "w"  :
         name = input("to show your data write your name : \n >>>").strip().lower()
         cr.execute("select * from users_2 where name = ?",(name,)) 
         data = cr.fetchone()
         
         if data != None : 
              print(f"your data is : \n - name : {data[0]} \n - progres : {data[1]}\n - id : {data[2]}")           
         else :
              y_n = input ("you are not a user \n do you want to sign up : y / n ").strip().lower()
              if y_n == "n" :
                   print("thank you good bay :(")
              elif y_n == "y" : 
                   sign_up()
              else: print (" rong answer good bay :( ") 

else :
    print("sorry ronnge input ")
#closeing and commeting 
db.commit()
db.close()
print ( "db is closed ")