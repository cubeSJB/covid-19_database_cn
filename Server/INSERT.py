
#
def insertCityData(g_instance, city_name, date, cured, dead, suspected, confirmed):
    try:
        g_instance.execute(
            "INSERT INTO info(DT, P_CODE, C_CODE, CONFIRMED, SUSPECTED, CURED, DEAD)  VALUES(%s, (SELECT C.省代码 FROM sde.c C WHERE C.市=%s), (SELECT C.市代码 FROM sde.c C WHERE C.市=%s),%s, %s, %s, %s);",
            (date, city_name, city_name, confirmed, suspected, cured, dead))
        output = g_instance.fetchall()
        return output

    except:
        return -1
