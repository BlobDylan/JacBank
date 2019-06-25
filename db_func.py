import sqlite3
import getPassword
import base64
from hashlib import sha224
import smtplib


def send_email(subject, msg, address):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('jacbankhelp@gmail.com', 'JaC53!#B4nK?')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('jacbankhelp@gmail.com', address, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


def email_auth(adress):
    x = getPassword.generate(False,True,True,False)
    subject = 'Authentication email for JacBank'
    msg = 'This is your authentication code: ' + x
    send_email(subject,msg,adress)
    return sha224(x.encode('utf-8')).hexdigest()


def get_xpath(url):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    findxpath = ("SELECT xpath FROM link WHERE url = ?")
    cursor.execute(findxpath, [(url)])
    results =  cursor.fetchall()
    if results:
        return results
    else:
        return None


def add_xpath(url, xpath):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    insertData = """INSERT INTO link(url,xpath)
        VALUES(?,?)"""
    cursor.execute(insertData, [(url), (xpath)])
    db.commit()


def check_username(username):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    findUser = ("SELECT * FROM user WHERE username = ?")
    cursor.execute(findUser,[(username)])
    if(cursor.fetchall()):
        return('taken')

def check_email(email):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    findUser = ("SELECT * FROM user WHERE email = ?")
    cursor.execute(findUser, [(email)])
    if (cursor.fetchall()):
        return True

def newUser(username,password,email):
    #recieves password and username and creates a new user in the database
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    insertData = """INSERT INTO user(username,password,email)
    VALUES(?,?,?)"""
    cursor.execute(insertData, [(username),(sha224(password.encode('utf-8')).hexdigest()),email])
    db.commit()
    db.close()


def encode(key, clear):
    """recieves a clear text and encodes it with a given key"""
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    """recieves an encoded text and decodes it with a given key"""
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def get_hash_with_id(id):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    hash = ("SELECT password FROM user WHERE userID = ?")
    cursor.execute(hash, [(id)])
    results = cursor.fetchall()
    return results[0][0]


def login(username,password):
    #attempts to log in with a given username and password
    with sqlite3.connect("UPDB.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username=? AND password=?",(username, sha224(password.encode('utf-8')).hexdigest(),))
    results = cursor.fetchall()
    if results:
        print("Welcome ")
        cursor.execute("SELECT userID FROM user WHERE username=? AND password=?",(username, sha224(password.encode('utf-8')).hexdigest(),))
        return cursor.fetchall()
    else:
        print('returned none because user doesnt exist')
        return None


def remove_website(user_ID, website_name):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM bank WHERE userID=? AND website=?;",(user_ID,website_name),)
    db.commit()
    db.close()


def add_new_website(user_ID, website_name, small, capital, numbers, chars, key,url):
    pw = getPassword.generate(small,capital,numbers,chars)
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    insertData = """INSERT INTO bank(userID,Website,website_password,url)
    VALUES(?,?,?,?)"""
    cursor.execute(insertData,[(user_ID),(website_name),(encode(key, pw)),(url)])
    print("Added website!")
    db.commit()
    db.close()


def change_website_name(user_ID,website_name,new_name):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("UPDATE bank SET website=? WHERE userID=? AND website =?" ,(new_name,user_ID,website_name),)
    db.commit()
    db.close()

def change_user_password(newpass, email):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("UPDATE user SET password=? WHERE email=?", (sha224(newpass.encode('utf-8')).hexdigest(),email), )
    db.commit()
    db.close()

def change_website_xpath(user_ID,url,xpath):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("UPDATE link SET xpath=? WHERE url=?" ,(xpath,url),)
    db.commit()
    db.close()


def get_website_password(user_ID, website_name):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT website_password FROM bank WHERE userID=? AND website=?",(user_ID,website_name),)
    results = cursor.fetchall()
    if(not results):
        print("no password found")
    else:
        return results[0][0]

def get_website_names(user_ID):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT website FROM bank WHERE userID=?",(user_ID,))
    results = cursor.fetchall()
    if not results:
        return None
    else:
        return results

def get_website_urls(user_ID):
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT url FROM bank WHERE userID=?",(user_ID,))
    results = cursor.fetchall()
    if not results:
        return None
    else:
        return results