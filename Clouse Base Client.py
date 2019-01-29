# Cloud Base Client.py
# client v1.0
# author: paul lee

import socket # include support for data transmission/receiving
import time

# ask user to enter a command
# list of commands:
# 
#   1: scd - store credential data
#   2: sbc - search by company
#   3: dac - display all companies

repeat_menu = True
while repeat_menu == True:

    sock = socket.socket() # use IPv4 protocol w/ tcp connection support
    ip = '192.168.0.20' # assign ip address of server to ip variable
    port = 12345 # assign dedicated port number for nexus cloud database server

    # connect to the server
    sock.connect((ip, port))
    
    cmd = input('Enter command: ')

    if cmd == 'scd':
        # send a code to the server to tell it that we are storing credential data
        code = 'scd'
        sock.send(code.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        
        # ask the user to enter core credential info
        company = input('Enter company name: ')
        username = input('Enter username: ')
        password = input('Enter password: ')
        pin = input('Enter pin: ')
        email = input('Enter email: ')

        # send datas to server for storage
        sock.send(company.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        sock.send(username.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        sock.send(password.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        sock.send(pin.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        sock.send(email.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission

        sock.close()

    elif cmd == 'sbc':
        # send a code to the server to tell it that we are searching credential data
        code = 'sbc'
        sock.send(code.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission

        # ask user to enter company name that he/she wants to search data for
        company = input('Enter company name: ')

        # send data to server
        sock.send(company.encode('ascii'))
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission

        # receive server code and data(s)
        server_code = sock.recv(1024).decode('ascii')
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        if server_code == 'found':

            company = sock.recv(1024).decode('ascii')
            time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
            username = sock.recv(1024).decode('ascii')
            time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
            password = sock.recv(1024).decode('ascii')
            time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
            pin = sock.recv(1024).decode('ascii')
            time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
            email = sock.recv(1024).decode('ascii')

            print(company)
            print(username)
            print(password)
            print(pin)
            print(email)
                
        elif server_code == 'false':
            msg = sock.recv(1024).decode('ascii')
            time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
            print(msg)

        sock.close()

    elif cmd == 'dac':
        # send a code to the server to tell it that we are searching credential data
        code = 'dac'
        sock.send(code.encode('ascii'))
        time.sleep(0.25)

        # receive the size of company list
        size = int(sock.recv(1024).decode('ascii'))

        # receive company data
        company_list = []
        for index in range(size):
            company = sock.recv(1024).decode('ascii')
            company_list.append(company)

        # display all company names
        for item in company_list:
            print(item)

        sock.close()

        
        
        

