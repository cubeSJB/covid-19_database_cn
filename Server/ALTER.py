from INSERT import *
from DELETE import *


# Alter

def alterCityData(g_instance, city_name, date, cured, dead, suspected, confirmed):
    er = deleteCityData(g_instance, city_name, date)
    if er != -1:
        insertCityData(g_instance, city_name, date, cured, dead, suspected, confirmed)
        return 0
    else:
        return -1
