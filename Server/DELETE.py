
#
def deleteCityData(g_instance, city_name, date):
    try:
        g_instance.execute("DELETE FROM sde.info I WHERE I.dt={} AND I.c_code=(SELECT C.市代码 FROM sde.c C WHERE position({} IN C.市)!=0".format(date, city_name))
        return g_instance.fetchall()

    except:
        return -1

#
def deleteCityDataAll(g_instance, city_name):
    try:
        g_instance.execute("DELETE FROM sde.info I WHERE I.c_code=(SELECT C.市代码 FROM sde.c C WHERE position({} IN C.市)!=0)".format(city_name))
        return g_instance.fetchall()

    except:
        return -1

def deleteProvinceData(g_instance, province_name, date):
    try:
        g_instance.execute("DELETE FROM sde.info I WHERE I.p_code=(SELECT P.省代码 FROM sde.p P WHERE position({} IN P.省)!=0 ) AND I.dt={}".format(province_name, date))
        return g_instance.fetchall()

    except:
        return -1


def deleteProvinceDataAll(g_instance, province_name):
    try:
        g_instance.execute("DELETE FROM sde.info I WHERE I.p_code=(SELECT P.省代码 FROM sde.p P WHERE position({} IN P.省)!=0 )".format(province_name))
        return g_instance.fetchall()

    except:
        return -1