#coding=utf-8

__author__ = 'Administrator'

import os,xml.dom.minidom

def getXmlData(key):

    xmlpath = os.getcwd()+'\\TestData\\testdata.xml'
    dom = xml.dom.minidom.parse(xmlpath)

    root = dom.documentElement
    name = root.getElementsByTagName(key)
    nameValue = name[0]
    return nameValue.firstChild.data



TESTURL = getXmlData('testurl')
KEFU_USERNAME = getXmlData('kefu_username')
KEFU_PASSWORD = getXmlData('kefu_password')
KEFU_RESULT = getXmlData('kefu_result')
GONGYINGLIAN_USERNAME = getXmlData('gongyinglian_username')
GONGYINGLIAN_PASSWORD = getXmlData('gongyinglian_password')
GONGYINGLIAN_RESULT = getXmlData('gongyinglian_result')
WULIU_USERNAME = getXmlData('wuliu_username')
WULIU_PASSWORD = getXmlData('wuliu_password')
WULIU_RESULT = getXmlData('wuliu_result')
WAIBU_USERNAME = getXmlData('waibu_username')
WAIBU_PASSWORD = getXmlData('waibu_password')
WAIBU_RESULT = getXmlData('waibu_result')
MYSQL_HOST = getXmlData('mysql_url')
MYSQL_USERNAME = getXmlData('mysql_username')
MYSQL_PASSWORD = getXmlData('mysql_password')
MYSQL_DB = getXmlData('mysql_db')
GAPPLICATIONNUMBER = getXmlData('gapplicationnumber')
ORDER_PHONE = getXmlData('order_phone')
STATION_ID = getXmlData('station_id')
STATION_NAME = getXmlData('station_name')
AREA = getXmlData('area')


