#
def selectTouchCounty(g_instance, county_name):
    g_instance.execute(
        "SELECT C2.pac, C2.name FROM sde.Co C1, sde.Co C2 WHERE sde.st_touches(C1.shape, C2.shape)=true AND C1.name='{}' ".format(
            county_name))
    return g_instance.fetchall()


#
def selectTouchCountyC(g_instance, county_code):
    g_instance.execute(
        "SELECT C2.pac, C2.name FROM sde.Co C1, sde.Co C2 WHERE sde.st_touches(C1.shape, C2.shape)=true AND C1.pac='{}' ".format(
            county_code))
    return g_instance.fetchall()


#
def selectTouchCity(g_instance, city_name):
    g_instance.execute(
        "SELECT C2.市代码, C2.市 FROM sde.c C1, sde.c C2 WHERE sde.st_touches(C1.shape, C2.shape)=true AND C1.市='{}' ".format(
            city_name))
    return g_instance.fetchall()


#
def selectTouchCityC(g_instance, city_code):
    g_instance.execute(
        "SELECT C2.市代码, C2.市 FROM sde.c C1, sde.c C2 WHERE sde.st_touches(C1.shape, C2.shape)=true AND C1.市代码='{}' ".format(
            city_code))
    return g_instance.fetchall()


#
def selectTouchProvince(g_instance, province_name):
    g_instance.execute(
        "SELECT P2.省代码, P2.省 FROM sde.p P1, sde.p P2 WHERE sde.st_touches(P1.shape, P2.shape)=true AND P1.省='{}' ".format(
            province_name))
    return g_instance.fetchall()


#
def selectTouchProvinceC(g_instance, province_code):
    g_instance.execute(
        "SELECT P2.省代码, P2.省 FROM sde.p P1, sde.p P2 WHERE sde.st_touches(P1.shape, P2.shape)=true AND P1.省代码='{}' ".format(
            province_code))
    return g_instance.fetchall()
