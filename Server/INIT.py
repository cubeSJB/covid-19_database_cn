#! /usr/bin/python3

import csv
import psycopg2

conn = psycopg2.connect(database='arcgis_108_gdb', user='sde', password='Shaojianbo1125', host='peiking.ksei.top', port='5432')

cursor = conn.cursor()


virus = open('Wuhan-2019-nCoV.csv', encoding='UTF-8')
csvFile = csv.reader(virus)
listNum = 0
File = open('SQL.sql', 'w')
for i in csvFile:
    if listNum % 500 == 0:
        print(listNum)
    listNum += 1
    if i[2] == 'CN' and i[6] != '' and 'y' not in i[6] and 'x' not in i[6] and 'e' not in i[6] and 'd' not in i[6] and 'f' not in i[6] and 'a' not in i[6] and 'b' not in i[6] and 'c' not in i[6] and 'y' not in i[6] and 'y' not in i[6] and 'y' not in i[6]:
        sql = """    """
        # print(i[0], i[4], i[6], i[7], i[8], i[9], i[10])

        DATA = i[0]
        PCD = i[4]
        CCD = i[6]
        CFD = i[7]
        SUS = i[8]
        CUR = i[9]
        DEA = i[10]
        File.write("INSERT INTO sde.info(Dt, P_Code, C_Code, confirmed, suspected, cured, dead) VALUES"+"("+"\'"+DATA+"\'"+","+PCD+","+CCD+","+CFD+","+SUS+","+CUR+","+DEA+")"+";\n")
        # cursor.execute("INSERT INTO sde.info(Dt, P_Code, C_Code, confirmed, suspected, cured, dead) VALUES (%s, %s, %s, %s, %s, %s, %s)", (DATA, PCD, CCD, CFD, SUS, CUR, DEA))