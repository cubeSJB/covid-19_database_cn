
# Select

#
def selectTouchesVirusData(g_instance, city_name, date):
    g_instance.execute(
        "SELECT C.市 AS City, I.dt AS Date, I.cured, I.dead, I.suspected, I.confirmed, I.cured-I2.cured AS CUAD,I.confirmed-I2.confirmed AS CFAD, I.dead-I2.dead AS DEAD, I.suspected-I2.suspected AS SUAD FROM sde.info I, sde.info I2,sde.c C WHERE I.c_code IN (SELECT C2.市代码 FROM sde.c C1, sde.c C2 WHERE sde.st_touches(C1.shape, C2.shape)=true AND C1.市={0}) AND I2.c_code IN (SELECT C2.市代码 FROM sde.c C1, sde.c C2 WHERE sde.st_touches(C1.shape, C2.shape)=true AND C1.市={0}) AND I.dt={1} AND I.c_code=C.市代码 AND I2.dt=I.dt-1".format(city_name, date))
    output = g_instance.fetchall()
    return output


#
def selectVirusData(g_instance, city_name, date):
    g_instance.execute(
        "SELECT C.市 AS City, I.dt AS Date, I.cured, I.dead, I.suspected, I.confirmed, I.cured-I2.cured AS CUAD,I.confirmed-I2.confirmed AS CFAD, I.dead-I2.dead AS DEAD, I.suspected-I2.suspected AS SUAD FROM sde.info I,sde.info I2, sde.c C WHERE I.dt=%s AND I2.dt=I.dt-1 AND I.c_code=C.市代码 AND I2.c_code=C.市代码 AND C.市=%s",
        (date, city_name))
    output = g_instance.fetchall()
    return output


#
def selectPVirusData(g_instance, province_name, date):
    g_instance.execute(
        "SELECT I1.pcode, I1.pdt, I1.pconfirmed, I1.psuspected, I1.pcured, I1.pdead, I1.pconfirmed-I2.pconfirmed, I1.psuspected-I2.psuspected, I1.pcured-I2.pcured, I1.pdead-I2.pdead FROM (SELECT SUM(I.suspected) psuspected, SUM(I.confirmed) pconfirmed, SUM(I.cured) pcured, SUM(I.dead) pdead, i.dt pdt, i.p_code pcode FROM sde.info I GROUP BY I.dt, I.p_code) I1, (SELECT SUM(I.suspected) psuspected, SUM(I.confirmed) pconfirmed, SUM(I.cured) pcured, SUM(I.dead) pdead, i.dt pdt, i.p_code pcode FROM sde.info I GROUP BY I.dt, I.p_code) I2, sde.p P WHERE I1.pdt=%s AND I2.pdt=I1.pdt-1 AND I1.pcode=P.省代码 AND I2.pcode=P.省代码 AND P.省=%s;",
        (date, province_name))
    output = g_instance.fetchall()
    return output
