# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

import pymysql

from collections import OrderedDict

def index(request):
	return render(request,'getHisInfo/getHisInfo.html')

def getHisInfo(request):
	#ceshi = '{"resultCode":0,"resultDatas":[{"bedNo":"13","testResult":"化验结果","cardType":"","layerNo":"2","isExamOrg":"N","placeOfBirth":"西安","admIdIss":"1","insuranceId":"122222","applyDepartmentName":"外科","checkItemName":[{"extNo":"151","itemName":"胸部平扫"}],"admId":"123457","diagnosis":"临床诊断","costType":"现金","patientWeight":"48","accessionNo":"0123456","applyDoctorName":"贾洁","chiefComplaint":"主诉","provinceName":"陕西","maritalStatus":"Y","sex":"M","checkPurpose":"检查目的","profession":"","historyCondition":"","patientName":"Django测试","address":"高新六路","nation":"汉族","surgeryResult":"手术结果","districtName":"高新区","idcardNo":"","checkPartName":"胸部","race":"陕西","zipcode":"710077","extNo":"151","telephone":"13511131111","regionNo":"1","hisId":"0123456","modalityName":"放射","cityName":"西安","applyHospitalId":"10010","eMail":"1123@c22.com","attending":"贾洁","totalFee":"1250","applyHospital":"陕西中医医院","applyParam":"","attention":"注意事项","isExigence":"Y","floorNo":"5","birthday":"1991-07-01","dormitoryNo":"1","patientStature":"158","payStatus":"0","degree":"小学","scanningType":"2"}],"resultDetail":"共查询到 1 条记录"}'
	#ceshi = {"dd":"sfas","ff":"sdfsd"}
	ceshi = {"resultCode":0,"resultDatas":[{"bedNo":"13","testResult":"化验结果","cardType":"","layerNo":"2","isExamOrg":"N","placeOfBirth":"西安","admIdIss":"1","insuranceId":"122222","applyDepartmentName":"外科","checkItemName":[{"extNo":"151","itemName":"胸部平扫"}],"admId":"123457","diagnosis":"临床诊断","costType":"现金","patientWeight":"48","accessionNo":"0123456","applyDoctorName":"贾洁","chiefComplaint":"主诉","provinceName":"陕西","maritalStatus":"Y","sex":"M","checkPurpose":"检查目的","profession":"","historyCondition":"","patientName":"Django测试","address":"高新六路","nation":"汉族","surgeryResult":"手术结果","districtName":"高新区","idcardNo":"","checkPartName":"胸部","race":"陕西","zipcode":"710077","extNo":"151","telephone":"13511131111","regionNo":"1","hisId":"0123456","modalityName":"放射","cityName":"西安","applyHospitalId":"10010","eMail":"1123@c22.com","attending":"贾洁","totalFee":"1250","applyHospital":"陕西中医医院","applyParam":"","attention":"注意事项","isExigence":"Y","floorNo":"5","birthday":"1991-07-01","dormitoryNo":"1","patientStature":"158","payStatus":"0","degree":"小学","scanningType":"2"}],"resultDetail":"共查询到 1 条记录"}
	
	#return render(request,'getHisInfo/getHisInfo.html',{"ceshi":ceshi})
	#return HttpResponse(json.dumps(ceshi), content_type="application/json")
	return HttpResponse(json.dumps(ceshi, ensure_ascii=False))
	#return HttpResponse(ceshi)


his_table={
"hisId" :"hisId",
"accessionNo":"accessionNo",
"checkPartName":"checkPartName",
"checkItemName":"checkItemName",
"patientName":"patientName",
"sex":"sex",
"birthday":"birthday",
"admId":"admId",
"admIdIss":"admIdIss",
"extNo":"extNo"
}

def searchata():

	conn = pymysql.connect(host="192.168.1.40",port=3306,user="root",passwd="root",db="his",charset='utf8',cursorclass=pymysql.cursors.DictCursor)
	 # 在默认情况下cursor方法返回的是BaseCursor类型对象，
	 #BaseCursor类型对象在执行查询后每条记录的结果以列表(list)表示。如果要返回字典(dict)表示的记录，就要设置cursorclass参数为MySQLdb.cursors.DictCursor类。
	cursor = conn.cursor()
	#cursor.execute("select * from pacs_gethisinfo group by modalityName")
	cursor.execute("select * from gao_test_mysql  where accessionNo ='{}' or hisId = '{}'".format("012345","012345"))

	#datas = cursor.fetchone()
	datas = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()

	rJsonData={}
	rExanitems={}
	for i in datas:
		for yizhen_name,his_name in his_table.items():
			for name ,value in i.items():
				if name == his_name:
					rJsonData[yizhen_name]=value
				    #print(rJsonData[yizhen_name])

				if name == "checkItemName":
					rExanitems["itemName"]=value

				if name == "extNo":
					rExanitems["extNo"]= value

	btable=[rExanitems]
	rJsonData["checkItemName"]=btable
	ctable = [rJsonData]
	#print(c)
	
	#print(a)
	length = len(datas)
	sResultDetail="共查询到 {} 条记录".format(length)
	rJsonObject={}
	rJsonObject["resultCode"]=0
	rJsonObject["resultDatas"]=ctable
	rJsonObject["resultDetail"]=sResultDetail
	#print(rJsonObject)
	#returndata = json.dumps(rJsonObject)
	#print(rJsonObject)
	datass=json.dumps(rJsonObject, ensure_ascii=False)
	print(datass)
	return rJsonObject

a= searchata()

