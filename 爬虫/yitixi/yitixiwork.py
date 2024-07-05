import json,jsonpath


with open(r"C:\Users\18824\Desktop\shuju.js", "rb") as f:
    content = f.read().decode("utf-8")
    # print(content)

    # 把json形式的字符串转换成python形式的unicode字符串(utf-8)
    unicodestr = json.loads(content)
    # print(unicodestr)
    # python形式的列表
    commdityName = jsonpath.jsonpath(unicodestr, "$..commdityName")
    etcPrice = jsonpath.jsonpath(unicodestr, "$..etcPrice")
    brandName = jsonpath.jsonpath(unicodestr, "$..brandName")
    vehicleModels = jsonpath.jsonpath(unicodestr, "$...vehicleBrandNameCnOfficial")
    vehicleModel = jsonpath.jsonpath(unicodestr, "$...vehicleModel")
    simplifiedEngineDesc = jsonpath.jsonpath(unicodestr, "$...simplifiedEngineDesc")
    vehicleBrandName = jsonpath.jsonpath(unicodestr, "$..exchangeOE[*].vehicleBrandName")
    oe = jsonpath.jsonpath(unicodestr, "$...oe")
    oeToPartBrandRemark = jsonpath.jsonpath(unicodestr, "$...oeToPartBrandRemark")
    partBrandBrandNameEtc = jsonpath.jsonpath(unicodestr, "$...partBrandBrandNameEtc")
    partBrandCode = jsonpath.jsonpath(unicodestr, "$...partBrandCode")

    print("名称："+str(commdityName[0]))
    print("价格："+str(etcPrice[+0]))
    print("品牌："+str(brandName[0]))
    content = []
    content.append(commdityName[0])
    content.append(etcPrice[0])
    # print(vehicleModels)
    # print(vehicleModel)
    # print(simplifiedEngineDesc)
    string1= ""
    item = []
    for i in range(len(vehicleModels)):
        string = vehicleModels[i]+" "+vehicleModel[i]+" "+simplifiedEngineDesc[i]
        string1 +=string
        item.append(string)

    # print(string1)
    print("使用车型:"+string1)
    content.append(string1)

    item2 = []
    string2 =""
    for i in range(len(vehicleBrandName)):
        if oeToPartBrandRemark[i] == "full":
            oeToPartBrandRemark[i] = " "
        string2 += vehicleBrandName[i]+" "+oe[i]+" "+oeToPartBrandRemark[i]

        # item2.append(string2)
    print("对应OE号:"+string2)
    content.append(string2)
    # print(vehicleBrandName)
    # print(oe)
    # print(oeToPartBrandRemark)
    item3 = []
    string3 = ""
    for i in range(len(partBrandBrandNameEtc)):
        string3 += partBrandBrandNameEtc[i] + " " + partBrandCode[i]

    print("对应品牌件号:" + string3)
    content.append(string3)
    with open("../goods10.csv", "a+") as f :
        f.write(str(content))
    # print(partBrandBrandNameEtc)
    # print(partBrandCode)


# 名称："commdityName"
# 价格："etcPrice"
# 使用车型："vehicleModels“
#     汽车品牌：vehicleBrandNameCnOfficial
#     车型："vehicleModel"
#     发动机排量："simplifiedEngineDesc": "1.5T",
#
# 对应OE号："exchangeOE":
#     品牌：vehicleBrandName
#     OE号：oe
#     备注："oeToPartBrandRemark"
#
# 对应品牌件号：exchangePartBrand
#     品牌：partBrandBrandNameEtc
#     品牌号：partBrandCode"
