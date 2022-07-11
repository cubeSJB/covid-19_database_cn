#! /usr/bin/python3

import socket
# import vDB
import psycopg2
import datetime
import time

from ALTER import alterCityData
from SELECT import selectPVirusData, selectTouchesVirusData, selectVirusData
from GSELECT import selectTouchProvince, selectTouchCity, selectTouchCounty, selectTouchCityC, selectTouchCountyC, \
    selectTouchProvinceC
from INSERT import insertCityData
from DELETE import deleteCityData, deleteCityDataAll, deleteProvinceData, deleteProvinceDataAll

CONN = psycopg2.connect(database="arcgis_108_gdb", user="sde", password="Shaojianbo1125", host="peiking.ksei.top",
                        port="5432")
t = time.localtime(time.time())
print('Connection Build At ' + time.asctime(t))
Instance = CONN.cursor()
print('Instance Build!')

serve = socket.socket()
host = '0.0.0.0'
host6 = '::0'
port = 8000

Key = (('root', 'ubuntu'), ('user', 'ubuntu'))

tcp_server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
tcp_server.bind((host6, port))
tcp_server.listen(1)


def returnDateProcess(returnData):
    if returnData == -1:
        return -1
    returnInfoString = ''
    returnNum = len(returnData)
    for i in range(returnNum):
        returnInfoString += returnData[i][1]
        returnInfoString += ','
        returnInfoString += returnData[i][0]
        returnInfoString += ','
        for j in range(8):
            try:
                returnInfoString += returnData[i][j + 2]
            except IndexError:
                returnInfoString += ' '
            returnInfoString += ','

    returnInfoString = returnInfoString[0:-1]
    return returnInfoString, returnNum


while True:
    connection, addr = tcp_server.accept()

    Data = connection.recv(1024).decode('UTF-8')
    t = time.localtime(time.time())
    print('Received an information from' + addr + 'at ' + time.asctime(t))

    Strings = Data.split(',')

    Status = ''
    returnNum = 0
    if Strings[0][0] == 'L':
        if Strings[1] == 'admin' and Strings[2] == 'admin':
            Status = 'L,'
            connection.send('L,0'.encode('UTF-8'))

        else:
            Status = 'R,'
            connection.send('R,0'.encode('UTF-8'))

        continue

    elif Strings[0][0] == 'Q':
        returnInfoString = ''
        if Strings[1][0] == '0':
            date = Strings[2]
            c_name = Strings[3]
            returnInfoString, returnLength = returnDateProcess(selectVirusData(Instance, c_name, date))
            if returnInfoString != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '1':
            date = Strings[2]
            p_name = Strings[3]
            returnInfoString, returnLength = returnDateProcess(selectPVirusData(Instance, p_name, date))
            if returnInfoString != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '2':
            date = Strings[2]
            c_name = Strings[3]
            returnInfoString, returnLength = returnDateProcess(selectTouchesVirusData(Instance, c_name, date))
            if returnInfoString != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '3':
            o_name = Strings[3]
            returnInfoString, returnLength = returnDateProcess(selectTouchCounty(Instance, o_name))
            if returnInfoString != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '4':
            c_name = Strings[3]
            returnInfoString, returnLength = returnDateProcess(selectTouchCity(Instance, c_name))
            if returnInfoString != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '5':
            p_name = Strings[3]
            returnInfoString, returnLength = returnDateProcess(selectTouchProvince(Instance, p_name))
            if returnInfoString != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        else:
            returnNum = 0
            pass

    elif Strings[0][0] == 'I':
        date = Strings[2]
        c_name = Strings[3]
        returnFunc = insertCityData(Instance, c_name, date, Strings[4], Strings[6], Strings[5], Strings[7])
        if returnFunc != -1:
            Status = 'Y,'
        else:
            Status = 'N,'

    elif Strings[0][0] == 'D':
        if Strings[1][0] == '0':
            c_name = Strings[3]
            returnFunc = deleteCityDataAll(Instance, c_name)
            if returnFunc != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '1':
            date = Strings[2]
            c_name = Strings[3]
            returnFunc = deleteCityData(Instance, c_name, date)
            if returnFunc != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '2':
            p_name = Strings[3]
            returnFunc = deleteProvinceDataAll(Instance, p_name)
            if returnFunc != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

        elif Strings[1][0] == '3':
            date = Strings[2]
            p_name = Strings[3]
            returnFunc = deleteProvinceData(Instance, p_name, date)
            if returnFunc != -1:
                Status = 'Y,'
            else:
                Status = 'N,'

    elif Strings[0][0] == 'A':
        date = Strings[2]
        c_name = Strings[3]
        returnFunc = alterCityData(Instance, c_name, date, Strings[4], Strings[6], Strings[5], Strings[7])
        if returnFunc != -1:
            Status = 'Y,'
        else:
            Status = 'N,'

    else:
        connection.close()
        connection.send('R,0'.encode('UTF-8'))
        break

    if Status == 'Y,':
        if Strings[0][0] == 'Q':
            SendData = Status + str(returnLength) + ',' + returnInfoString
        else:
            SendData = Status + '0'
    else:
        SendData = Status + '0'
    connection.send(SendData.encode('UTF-8'))
    print('Send Data to {} !'.format(addr))
