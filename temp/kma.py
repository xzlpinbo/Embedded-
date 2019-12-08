#-*- condig: utf-8 -*-

from urllib.request import urlopen #python3
from xml.dom import minidom

wDict = {"Clear":"01",          \
         "Partly Cloudy":"02",  \
         "Mostly Cloudy":"03",  \
         "Cloudy":"17",         \
         "Rain":"21",           \
         "Snow/Rain":"05",      \
         "Snow":"32"}

def getWeather(localCode):
    base_url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone="
    url = base_url + str(localCode)
    u = urlopen(url)
    wdata = []

    # url 
    data = u.read()
    dom = minidom.parseString(data)
    item = dom.getElementsByTagName("data")[0]
    
    # data read
    local = dom.getElementsByTagName("category")[0].firstChild.data.strip()

    temp = item.getElementsByTagName("temp")[0].firstChild.data.strip()
    tmx = item.getElementsByTagName("tmx")[0].firstChild.data.strip()
    tmn = item.getElementsByTagName("tmn")[0].firstChild.data.strip()
    wfEn = item.getElementsByTagName("wfEn")[0].firstChild.data.strip()
    ws = item.getElementsByTagName("ws")[0].firstChild.data.strip()
    wd = item.getElementsByTagName("wd")[0].firstChild.data.strip()
    pop = item.getElementsByTagName("pop")[0].firstChild.data.strip()
    reh = item.getElementsByTagName("reh")[0].firstChild.data.strip()
    
    wdata = [wfEn, temp, tmx, tmn, ws, wd, pop, reh, local]
    return wdata

