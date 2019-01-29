# Clouse Base Server.py
# server v1.0
# author: paul lee

import socket # include support for data transmission/receiving
import time

sock = socket.socket() # use IPv4 protocol w/ tcp connection support
ip = '192.168.0.20' # assign ip address of server to ip variable
port = 12345 # assign dedicated port number for nexus cloud database server

# bind ip and port
sock.bind((ip, port))

# listen for oncoming connections
sock.listen(5)

while True:

    # establish a connection
    conn , addr = sock.accept()

    # receive the code sent from the client
    code = conn.recv(1024).decode('ascii')
    time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
    if code == 'scd':
        # receive data from client
        company = conn.recv(1024).decode()
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        username = conn.recv(1024).decode()
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        password = conn.recv(1024).decode()
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        pin = conn.recv(1024).decode()
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
        email = conn.recv(1024).decode()
        time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission

        print(company)
        print(username)
        print(password)
        print(pin)
        print(email)

        # save datas to text file
        f = open('credentials.txt', 'a')
        f.write(company + '\n')
        f.write(username + '\n')
        f.write(password + '\n')
        f.write(pin + '\n')
        f.write(email + '\n')
        f.close()

    elif code == 'sbc':
        # receive data from client
        company = conn.recv(1024).decode()

        # open credentials.txt and read all datas into list
        credentials = [line.rstrip('\n') for line in open('credentials.txt')]

        # for debugging purposes: display all lines of data
        for item in credentials:
            print(item)

        # search company from list
        found = False
        specified_credentials = []
        index = 0
        while (index < len(credentials)):
            if (credentials[index] == company):

                specified_credentials.append(credentials[index + 0])
                specified_credentials.append(credentials[index + 1])
                specified_credentials.append(credentials[index + 2])
                specified_credentials.append(credentials[index + 3])
                specified_credentials.append(credentials[index + 4])

                server_code = 'found'

                conn.send(server_code.encode('ascii'))
                time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
            
                conn.send(specified_credentials[0].encode('ascii'))
                time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
                conn.send(specified_credentials[1].encode('ascii'))
                time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
                conn.send(specified_credentials[2].encode('ascii'))
                time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
                conn.send(specified_credentials[3].encode('ascii'))
                time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission
                conn.send(specified_credentials[4].encode('ascii'))
                time.sleep(0.25) # make sure to sleep for .25 seconds to reduce bugs in data transmission

                break
            else:
                index = index + 1

    elif code == 'dac':

        # open credentials.txt and read all datas into list
        credentials = [line.rstrip('\n') for line in open('credentials.txt')]

        company_list = []
        
        # search every 5th element in list and store it in another list namely company
        index = 0
        while index < len(credentials):
            company_list.append(credentials[index])
            index = index + 5

        # the company list has been accumulated with all the company names
        # send these datas to the client
        size = str(len(company_list))
        conn.send(size.encode('ascii'))
        
        for company in company_list:
            conn.send(company.encode('ascii'))
            

        
