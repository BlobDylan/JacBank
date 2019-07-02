import sqlite3
import base64
from hashlib import sha224
import smtplib
import random

"""This file contains all the functions that the server is responsible of preforming.
it preforms them as a request from the server and returns the appropriate data"""


def send_email(subject, msg, address):
    """sends and email with a given subject and message to a given address.
     returns a which means there's no need to return anything.(void funciton)"""
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
    return 'a'


def email_auth(adress):
    """uses send_email to send an authentication email to a given address
     containing a code generated from the function generate. returns the hash of the code"""
    x = generate(False,True,True,False)
    subject = 'Authentication email for JacBank'
    msg = 'This is your authentication code: ' + x
    send_email(subject,msg,adress)
    return sha224(x.encode('utf-8')).hexdigest()


def get_xpath(url):
    """attempts to get the xpath of a given url and return it."""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    findxpath = ("SELECT xpath FROM link WHERE url = ?")
    cursor.execute(findxpath, [(url)])
    results = cursor.fetchall()
    if results:
        return str(results)
    else:
        return 'a'


def add_xpath(url, xpath):
    """adds a given xpath and url to the link table in the database"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    insertData = """INSERT INTO link(url,xpath)
        VALUES(?,?)"""
    cursor.execute(insertData, [(url), (xpath)])
    db.commit()
    return 'a'


def check_username(username):
    """checks if a given username is in the user table in the database"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    findUser = ("SELECT * FROM user WHERE username = ?")
    cursor.execute(findUser,[(username)])
    if(cursor.fetchall()):
        return 'taken'
    else:
        return 'a'

def check_email(email):
    """checks to see if a given email is being used in the user database"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    findUser = ("SELECT * FROM user WHERE email = ?")
    cursor.execute(findUser, [(email)])
    if (cursor.fetchall()):
        return 'True'
    else:
        return 'False'

def newUser(username,password,email):
    """adds a new user to the user table in the database with a given username password and email."""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    insertData = """INSERT INTO user(username,password,email)
    VALUES(?,?,?)"""
    cursor.execute(insertData, [(username),(sha224(password.encode('utf-8')).hexdigest()),email])
    db.commit()
    db.close()
    return 'a'


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
    """reutns the hash of the password of the user with the given id"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    hash = ("SELECT password FROM user WHERE userID = ?")
    cursor.execute(hash, [(id)])
    results = cursor.fetchall()
    return results[0][0]


def login(username,password):
    """attempts to log in with a given username and password"""
    with sqlite3.connect("UPDB.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username=? AND password=?",(username, sha224(password.encode('utf-8')).hexdigest(),))
    results = cursor.fetchall()
    if results:
        print("Welcome ")
        cursor.execute("SELECT userID FROM user WHERE username=? AND password=?",(username, sha224(password.encode('utf-8')).hexdigest(),))
        x = cursor.fetchall()
        return (str(x))
    else:
        print('returned a because user doesnt exist')
        return 'a'


def remove_website(user_ID, website_name):
    """removes a website from the bank table with a given id and name"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM bank WHERE userID=? AND website=?;",(user_ID,website_name),)
    db.commit()
    db.close()
    return 'a'


def add_new_website(user_ID, website_name, small, capital, numbers, chars, key,url):
    """adds a new website to the bank table with the given arguments"""
    pw = generate(small,capital,numbers,chars)
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    insertData = """INSERT INTO bank(userID,Website,website_password,url)
    VALUES(?,?,?,?)"""
    cursor.execute(insertData,[(user_ID),(website_name),(encode(key, pw)),(url)])
    print("Added website!")
    db.commit()
    db.close()
    return 'a'


def change_website_name(user_ID,website_name,new_name):
    """changes a given websites name in the bank table"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("UPDATE bank SET website=? WHERE userID=? AND website =?" ,(new_name,user_ID,website_name),)
    db.commit()
    db.close()
    return 'a'


def change_user_password(newpass, email):
    """changes the password of the user with the given email to a given password"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("UPDATE user SET password=? WHERE email=?", (sha224(newpass.encode('utf-8')).hexdigest(),email), )
    db.commit()
    db.close()
    return 'a'


def change_website_xpath(user_ID,url,xpath):
    """changes a urls xpath"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("UPDATE link SET xpath=? WHERE url=?" ,(xpath,url),)
    db.commit()
    db.close()
    return 'a'


def get_website_password(user_ID, website_name):
    """gets a given websites password from the banks database of a user with the given id"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT website_password FROM bank WHERE userID=? AND website=?",(user_ID,website_name),)
    results = cursor.fetchall()
    if(not results):
        return 'a'
    else:
        return str(results)


def get_website_names(user_ID):
    """gets all website names from bank of a user with the given id"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT website FROM bank WHERE userID=?",(user_ID,))
    results = cursor.fetchall()
    if not results:
        return 'a'
    else:
        return str(results)


def get_website_urls(user_ID):
    """gets all the websites urls from bank of a user with a given id"""
    db = sqlite3.connect("UPDB.db")
    cursor = db.cursor()
    cursor.execute("SELECT url FROM bank WHERE userID=?",(user_ID,))
    results = cursor.fetchall()
    if not results:
        return 'a'
    else:
        return str(results)


def generate(small, capital, numbers, chars):
    """generates a password conforming to the users preferences that are given"""
    p = ''
    length = random.randint(12, 15)
    for i in range(length):
        x = []
        if small:
            x.append(str(chr(random.randint(97, 122))))
        if capital:
            x.append(str(chr(random.randint(65, 90))))
        if numbers:
            x.append(str(random.randint(0, 9)))
        if chars:
            ch = ['#', '!', '?', '.' ,'*' ,'&' ,'$' ,'@' ,'%']
            x.append(random.choice(ch))
        p += random.choice(x)
    return p
