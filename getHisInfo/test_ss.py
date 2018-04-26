
rJsonData={}
rJsonDatas=[]
rExanitems={"extno":"123456","no":"021"}
btable=[rExanitems]
rJsonData["checkItemName"]=btable
#rJsonDatas = [rJsonData]
rJsonDatas.insert(0,rJsonData)

print(rJsonDatas)
for i ,k in  rJsonData.items():
	print i,k