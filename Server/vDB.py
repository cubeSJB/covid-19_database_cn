#! /usr/bin/python3

# -*- coding: utf-8 -*-

import psycopg2

from SELECT import selectPVirusData, selectTouchesVirusData, selectVirusData
from GSELECT import selectTouchProvince, selectTouchCity, selectTouchCounty
from INSERT import insertCityData
from DELETE import deleteCityData, deleteCityDataAll, deleteProvinceData, deleteProvinceDataAll
from ALTER import alterCityData

from socket import *

CONN = psycopg2.connect(database="arcgis_108_gdb", user="sde", password="Shaojianbo1125", host="peiking.ksei.top", port="5432")
print('Connection Build!')
Instance = CONN.cursor()
print('Instance Build!')

print('input 0 to Query')
print('input 1 to GQuery')
print('input 2 to Insert')
print('input 3 to Delete')
print('input 4 to Alter')
print('input -1 to Quit')

while True:
    option = int(input())
    if option == 0:
        print('')
        q_option = int(input())
        if q_option == 1:
            c_name = input('city_name\n')
            date = input('date\n')
            VirusData = selectVirusData(Instance, c_name, date)
            print(VirusData)
        elif q_option == 2:
            p_name = input('province_name')
            date = input('date')
            VirusData = selectPVirusData(Instance, p_name, date)
            print(VirusData)
        elif q_option == 3:
            c_name = input('City_name')
            date = input('date')
            N_VirusData = selectTouchesVirusData(Instance, c_name, date)
            print(N_VirusData)

    elif option == 1:
        q_option = int(input())
        if q_option == 1:
            c_name = input('County Name\n')
            Q_out = selectTouchCounty(Instance, c_name)
            print(Q_out)
        elif q_option == 2:
            c_name = input('City Name\n')
            Q_out = selectTouchCity(Instance, c_name)
            print(Q_out)
        elif q_option == 3:
            p_name = input('Province Name\n')
            Q_out = selectTouchProvince(Instance, p_name)
            print(Q_out)

    elif option == 2:
        q_option = int(input())
        if q_option == 1:
            c_name = input('City Name')
            date = input('Date')
            cured = input('Cured')
            dead = input('Dead')
            suspected = input('Suspected')
            confirmed = input('Confirmed')
            Iout = insertCityData(Instance, c_name, date, cured, dead, suspected, confirmed)
            print(Iout)

    elif option == 3:
        d_option = int(input('D_option'))
        if d_option == 1:
            c_name = input('Delete City Name')
            d_date = input('Delete Date')
            D_out = deleteCityData(Instance, c_name, d_date)
            print(D_out)
        elif d_option == 2:
            c_name = input('Delete City Name')
            D_out = deleteCityDataAll(Instance, c_name)
            print(D_out)
        elif d_option == 3:
            p_name = input('Delete Province Name')
            d_date = input('Delete Date')
            D_out = deleteProvinceData(Instance, p_name, d_date)
        elif d_option == 4:
            p_name = input('Delete Province Name')
            D_out = deleteProvinceDataAll(Instance, p_name)

    elif option == 4:
        c_name = input('City Name')
        date = input('Date')
        cured = input('Cured')
        dead = input('Dead')
        suspected = input('Suspected')
        confirmed = input('Confirmed')
        Aut = alterCityData(Instance, c_name, date, cured, dead, suspected, confirmed)

    elif option == -1:
        break