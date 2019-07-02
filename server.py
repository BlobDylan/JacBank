# import socket programming library 
import socket

# import thread module 
from _thread import *
import threading
import db_func_server

print_lock = threading.Lock()


# thread fuction
def threaded(c):
    while True:

        # data received from client 
        data = c.recv(1024)
        print(data)
        if not data:
            print('Bye')

            # lock released on exit 
            print_lock.release()
            break

        # reverse the given string from client
        data = data.decode('utf-8')
        print(data)
        vars = data.split(',')
        if (vars[0] == 'send_email'):
            data = db_func_server.send_email(vars[1],vars[2],vars[3])
            c.send(data.encode('utf-8'))


        elif (vars[0] == 'email_auth'):
            data = db_func_server.email_auth(vars[1])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'get_xpath'):
            data = db_func_server.get_xpath(vars[1])
            c.send(data.encode('utf-8'))


        elif (vars[0] == 'add_xpath'):
            data = db_func_server.add_xpath(vars[1],vars[2])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'check_username'):
            data = db_func_server.check_username(vars[1])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'check_email'):
            data = db_func_server.check_email(vars[1])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'check_email'):
            db_func_server.check_email(vars[1])
            c.send(str(data).encode('utf-8'))

        elif (vars[0] == 'newUser'):
            data = db_func_server.newUser(vars[1],vars[2],vars[3])
            c.send(data.encode('utf-8'))


        elif (vars[0] == 'encode'):
            data = db_func_server.encode(vars[1],vars[2])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'decode'):
            data = db_func_server.decode(vars[1],vars[2])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'get_hash_with_id'):
            data = db_func_server.get_hash_with_id(vars[1])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'login'):
            data = db_func_server.login(vars[1],vars[2])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'remove_website'):
            data = db_func_server.remove_website(vars[1],vars[2])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'add_new_website'):
            data = db_func_server.add_new_website(vars[1],vars[2],vars[3],vars[4],vars[5],vars[6],vars[7],vars[8])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'change_website_name'):
            data = db_func_server.change_website_name(vars[1],vars[2],vars[3])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'change_user_password'):
            data = db_func_server.change_user_password(vars[1],vars[2])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'change_website_xpath'):
            data = db_func_server.change_website_xpath(vars[1],vars[2],vars[3])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'get_website_password'):
            data = db_func_server.get_website_password(vars[1],vars[2])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'get_website_names'):
            data = db_func_server.get_website_names(vars[1])
            c.send(data.encode('utf-8'))

        elif (vars[0] == 'get_website_urls'):
            data = db_func_server.get_website_urls(vars[1])
            c.send(data.encode('utf-8'))

        elif(vars[0] == 'generate'):
            data = db_func_server.generate(bool(vars[1] == 'True'),bool(vars[2] == 'True'),bool(vars[3] == 'True'),bool(vars[4] == 'True'))
            c.send(data.encode('utf-8'))

        else:
            print('Error - undefined function')

        # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)

    # put the socket into listening mode 
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit 
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client 
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,))


if __name__ == '__main__':
    Main() 