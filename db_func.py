import ast
import socket

"""In this file I have a collection of all the functions that I don't wish the client to have access too.
all the functions connect to the server and return the appropriate data from it."""


def generate(small, capital, numbers, chars):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'generate,' + str(small) + ',' + str(capital) + ',' + str(numbers) + ',' + str(chars)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')

def send_email(subject, msg, address):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'send_email,' + str(subject) + ',' + str(msg) + ',' + str(address)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def email_auth(address):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'email_auth,' + str(address)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def get_xpath(url):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'get_xpath,' + str(url)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    if data.decode('utf-8') == 'a':
        return None
    return ast.literal_eval(data.decode('utf-8'))


def add_xpath(url, xpath):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'add_xpath,' + str(url) + ',' + str(xpath)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def check_username(username):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'check_username,' + str(username)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')

def check_email(email):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'check_email,' + str(email)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return ast.literal_eval(data.decode('utf-8'))

def newUser(username,password,email):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'newUser,' + str(username) + ',' + str(password) + ',' + str(email)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def encode(key, clear):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'encode,' + str(key) + ',' + str(clear)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def decode(key, enc):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'decode,' + str(key) + ','+ str(enc)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def get_hash_with_id(id):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'get_hash_with_id,' + str(id)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def login(username,password):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'login,' + str(username) + ',' + str(password)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    if data.decode('utf-8') == 'a':
        return None
    return ast.literal_eval(data.decode('utf-8'))


def remove_website(user_ID, website_name):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'remove_website,' + str(user_ID) + ',' + str(website_name)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def add_new_website(user_ID, website_name, small, capital, numbers, chars, key,url):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'add_new_website,'+ str(user_ID) + ',' + str(website_name) + ',' + str(small) + ',' + str(capital) + ',' + str(numbers) + ',' + str(chars) + ',' + str(key) + ',' + str(url)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def change_website_name(user_ID,website_name,new_name):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'change_website_name,' + str(user_ID) + ',' + str(website_name) + ',' + str(new_name)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')
    

def change_user_password(newpass, email):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'change_user_password,' + str(newpass) + ',' + str(email)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()

def change_website_xpath(user_ID,url,xpath):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'change_website_xpath,' + str(user_ID) + ',' + str(url) + ',' + str(xpath)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    return data.decode('utf-8')


def get_website_password(user_ID, website_name):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'get_website_password,' + str(user_ID) + ',' + str(website_name)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    if data.decode('utf-8') == 'a':
        return None
    return ast.literal_eval(data.decode('utf-8'))


def get_website_names(user_ID):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'get_website_names,' + str(user_ID)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    if data.decode('utf-8') == 'a':
        return None
    return ast.literal_eval(data.decode('utf-8'))


def get_website_urls(user_ID):
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = 'get_website_urls,' + str(user_ID)
    print(message)
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from the server :', str(data.decode('utf-8')))
    s.close()
    if data.decode('utf-8') == 'a':
        return None
    return ast.literal_eval(data.decode('utf-8'))