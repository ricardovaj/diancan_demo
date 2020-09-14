from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
import pymysql
import datetime
import os

conn=pymysql.connect(
    user='root',
    password='123456',
    port=3306,
    host='127.0.0.1',
    db='myshop',
    charset='utf8'
)
cursor=conn.cursor()
cursor.execute('set names utf8')
cursor.execute('set autocommit=1')

@xframe_options_exempt
def getfoodbyid(request):
    id= request.POST.get("id")
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where id="+id
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    if row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getfoodlist(request):
    key= request.POST.get("key")
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct order by id desc "
    if not key.strip()=="":
        strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where proname like '%"+key+"%'  order by id desc "
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# @xframe_options_exempt
# def getfoodlist(request):
#     key= request.GET.get("key")
#     strsql1 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=1  order by id desc "
#     if not key.strip()=="":
#         strsql1 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=1 and  proname like '%"+key+"%'  order by id desc "
#     cursor.execute(strsql1)
#     conn.commit()
#     foodlist1 = []
#     row = cursor.fetchone()
#     while row:
#         foodlist1.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
#         row = cursor.fetchone()
#
#
#     strsql2 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=2  order by id desc "
#     if not key.strip()=="":
#         strsql2 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=2 and proname like '%"+key+"%'  order by id desc "
#     cursor.execute(strsql2)
#     conn.commit()
#     foodlist2 = []
#     row = cursor.fetchone()
#     while row:
#         foodlist2.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
#         row = cursor.fetchone()
#
#
#     strsql3 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=3  order by id desc "
#     if not key.strip() == "":
#         strsql3 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=3 and proname like '%" + key + "%'  order by id desc "
#     cursor.execute(strsql3)
#     conn.commit()
#     foodlist3 = []
#     row = cursor.fetchone()
#     while row:
#         foodlist3.append(
#             {"id": row[0], "proname": row[1], "price": str(row[2]), "brief": row[3], "descriptions": row[4],
#              "istop": row[5], "isstar": row[6], "imgurl": row[7], "typeid": row[8]})
#         row = cursor.fetchone()
#
#     strsql4 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=4  order by id desc "
#     if not key.strip() == "":
#         strsql4 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=4 and proname like '%" + key + "%'  order by id desc "
#     cursor.execute(strsql4)
#     conn.commit()
#     foodlist4 = []
#     row = cursor.fetchone()
#     while row:
#         foodlist4.append(
#             {"id": row[0], "proname": row[1], "price": str(row[2]), "brief": row[3], "descriptions": row[4],
#              "istop": row[5], "isstar": row[6], "imgurl": row[7], "typeid": row[8]})
#         row = cursor.fetchone()
#
#     strsql5 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=5  order by id desc "
#     if not key.strip() == "":
#         strsql5 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where typeid=5 and proname like '%" + key + "%'  order by id desc "
#     cursor.execute(strsql5)
#     conn.commit()
#     foodlist5 = []
#     row = cursor.fetchone()
#     while row:
#         foodlist5.append(
#             {"id": row[0], "proname": row[1], "price": str(row[2]), "brief": row[3], "descriptions": row[4],
#              "istop": row[5], "isstar": row[6], "imgurl": row[7], "typeid": row[8]})
#         row = cursor.fetchone()
#     s0 = ""
#     s0 += "["
#     itemindex1=0
#     for item1 in foodlist1:
#         itemindex1=itemindex1+1
#         s0 += "{"
#         s0 += "name: \""+item1.get("proname")+"\","
#         s0 += "pay:"+str(item1.get("price"))+","
#         s0 += "text:'"+item1.get("brief")+"',"
#         s0 += "Sold:1000,"
#         s0 += "Number:0,"
#         s0 += "FoodId:"+str(item1.get("id"))+""
#         if len(foodlist1)==itemindex1:
#             s0 += "}"
#         else:
#             s0 += "},"
#     s0 += "]"

    # s0 += "["
    # itemindex2 = 0
    # for item2 in foodlist2:
    #     itemindex2 = itemindex2 + 1
    #     s0 += "{"
    #     s0 += "name: \"" + item1.get("proname") + "\","
    #     s0 += "pay:"+str(item1.get("price"))+","
    #     s0 += "text:'" + item1.get("brief") + "',"
    #     s0 += "Sold:1000,"
    #     s0 += "Number:0,"
    #     s0 += "FoodId:"+str(item1.get("id"))+""
    #     if len(foodlist2) == itemindex2:
    #         s0 += "}"
    #     else:
    #         s0 += "},"
    # s0 += "],"
    #
    # s0 += "["
    # itemindex3 = 0
    # for item3 in foodlist3:
    #     itemindex3 = itemindex3 + 1
    #     s0 += "{"
    #     s0 += "name: \"" + item1.get("proname") + "\","
    #     s0 += "pay:"+str(item1.get("price"))+","
    #     s0 += "text:'" + item1.get("brief") + "',"
    #     s0 += "Sold:1000,"
    #     s0 += "Number:0,"
    #     s0 += "FoodId:"+str(item1.get("id"))+""
    #     if len(foodlist3) == itemindex3:
    #         s0 += "}"
    #     else:
    #         s0 += "},"
    # s0 += "],"
    #
    # s0 += "["
    # itemindex4 = 0
    # for item4 in foodlist4:
    #     itemindex4= itemindex4 + 1
    #     s0 += "{"
    #     s0 += "name: \"" + item1.get("proname") + "\","
    #     s0 += "pay:"+str(item1.get("price"))+","
    #     s0 += "text:'" + item1.get("brief") + "',"
    #     s0 += "Sold:1000,"
    #     s0 += "Number:0,"
    #     s0 += "FoodId:"+str(item1.get("id"))+""
    #     if len(foodlist4) == itemindex4:
    #         s0 += "}"
    #     else:
    #         s0 += "},"
    # s0 += "],"
    #
    # s0 += "["
    # itemindex5 = 0
    # for item5 in foodlist5:
    #     itemindex5 = itemindex5 + 1
    #     s0 += "{"
    #     s0 += "name: \"" + item1.get("proname") + "\","
    #     s0 += "pay:"+str(item1.get("price"))+","
    #     s0 += "text:'" + item1.get("brief") + "',"
    #     s0 += "Sold:1000,"
    #     s0 += "Number:0,"
    #     s0 += "FoodId:"+str(item1.get("id"))+""
    #     if len(foodlist5) == itemindex5:
    #         s0 += "}"
    #     else:
    #         s0 += "},"
    # s0 += "]"
    # s0 += "]"
    # print(s0)
    # s1 = s0.split("],")
    # print(s1)
    # response = HttpResponse(s0)
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Headers"] = "Content-Type"
    # response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    # return response

@xframe_options_exempt
def getfoodlistbyrandom(request):
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct order by  RAND() limit 4 "
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def login(request):
    #print("接收到的参数typeid="+str(request.GET.get("typeid")))
    username=request.POST.get("username")
    password = request.POST.get("password")
    print(username)
    print(password)
    strsql="select id,username,password,truename,tel,address from tbusers where username='"+username+"' and password='"+password+"' "
    cursor.execute(strsql)
    conn.commit()
    row = cursor.fetchone()
    s=""
    if row:
        s=str({"id": row[0], "username": row[1], "password": row[2], "truename": row[3], "tel": row[4], "address": row[5]})
        s=s.replace("'","\"")
    res="["+s+"]"
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def reg(request):
    username = request.POST.get("_username")
    password = request.POST.get("_password")
    tel = request.POST.get("tel")
    address = request.POST.get("dre")
    truename = request.POST.get("truename")
    cursor.execute('insert into tbusers (username,password,truename,tel,address) value (%s,%s,%s,%s,%s)',
                   (username, password, truename, tel, address))
    conn.commit()
    s = "{\"msg\":\"注册成功\"}"
    res = "[" + s + "]"
    response = HttpResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def addtocar(request):
    #接收参数
    userid = request.POST.get('userid')
    proid = request.POST.get('proid')
    proname = request.POST.get('proname')
    procount = request.POST.get('procount')
    imgurl = request.POST.get('imgurl')
    price = request.POST.get('price')

    ctime = datetime.datetime.now().strftime('%F %T')
    #我们将一个菜品加入购物车的时候，首先要判断购物车里面是否已经存在这个菜品了，如果已经存在，就增加数量，如果不存在，就插入一条新的记录。
    strsql1="select id from tbshoppingcar where proid="+proid+" and sessionid="+userid
    cursor.execute(strsql1)
    conn.commit()
    row=cursor.fetchone()
    strsql2 = "insert into tbshoppingcar(sessionid,proname,proid,procount,ctime,imgurl,price) values ("+userid+",'"+proname+"',"+proid+","+procount+",'"+ctime+"','"+imgurl+"',"+price+") "
    if row:
        strsql2="update tbshoppingcar set procount=procount+"+procount+" where proid="+proid+" and sessionid="+userid
    print(strsql2)
    cursor.execute(strsql2)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getcarlist(request):
    userid= request.POST.get("userid")
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "sessionid": row[1], "proname":row[2], "proid": row[3], "procount": row[4],"ctime": row[5],"imgurl": row[6],"price":str(row[7])})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def deleteitembyid(request):
    id= request.POST.get("id")
    strsql = "delete from tbshoppingcar where id="+id
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def changecarnum(request):
    id= request.POST.get("id")
    typeid = request.POST.get("typeid")
    strsql = "update tbshoppingcar set procount=procount+1 where id=" + id
    if typeid=="0":
        strsql = "update tbshoppingcar set procount = IF(procount > 1, procount - 1,1) where id=" + id
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
#在线下单功能
@xframe_options_exempt
def saveorder(request):
    t = datetime.datetime.now()
    ctime = t.strftime('%Y-%m-%d %H:%M:%S')
    orderid = datetime.datetime.strftime(t, "%Y%m%d%H%M%S%f")
    userid= request.POST.get("userid")
    sumprice = request.POST.get("sumprice")
    sname = request.POST.get("sname")
    stel = request.POST.get("stel")
    saddress = request.POST.get("saddress")
    ptime = request.POST.get("ptime")
    memo = request.POST.get("memo")
    #插入表头信息
    cursor.execute("insert into tborderhead (orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo) values ('"+orderid+"','"+sname+"','"+stel+"','"+saddress+"',"+sumprice+","+userid+",'"+ctime+"','"+ptime+"','"+memo+"')")
    conn.commit()

    #把购物车里面的数据插入到订单明细表
    #先把购物车里当前这个人的菜品查询出来
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    #构造插入订单明细表的sql语句
    sqllists = []
    row = cursor.fetchone()
    while row:
        #{"id": row[0], "sessionid": row[1], "proname": row[2], "proid": row[3], "procount": row[4], "ctime": row[5],"imgurl": row[6], "price": str(row[7])}
        sqllists.append("insert into tborderitems (orderid,proid,proname,price,procount,imgurl) values ('"+orderid+"',"+str(row[3])+",'"+row[2]+"',"+str(row[7])+","+str(row[4])+",'"+row[6]+"')")
        row = cursor.fetchone()
    #遍历sql列表，执行插入订单明细表操作
    for sqlitem in sqllists:
        cursor.execute(sqlitem)
        conn.commit()
    #清空购物车
    cursor.execute("delete from tbshoppingcar where sessionid="+userid)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

# 微信index厨师展示
# @xframe_options_exempt
def getcookerlistbyrandom(request):
    strsql = "select id,cookername,cookernews,imgurl from tbcooker order by  RAND() limit 3 "
    cursor.execute(strsql)
    conn.commit()
    cookerlist = []
    row = cursor.fetchone()
    while row:
        cookerlist.append({"id": row[0], "cookername": row[1], "cookernews": row[2],"imgurl": row[3]})
        row = cursor.fetchone()
    s = str(cookerlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


# 留言展示
@xframe_options_exempt
def getnewslistbyrandom(request):
    strsql = "select id,author,contents,createtime from tbnews order by  RAND() limit 10 "
    cursor.execute(strsql)
    conn.commit()
    newslist = []
    row = cursor.fetchone()
    while row:
        newslist.append({"id": row[0], "author": row[1], "contents": row[2], "createtime": row[3]})
        row = cursor.fetchone()
    s = str(newslist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

# 轮播图展示
@xframe_options_exempt
def getviewpagerlistbyrandom(request):
    strsql = "select id,imgurl from viewpager order by  RAND() limit 3 "
    cursor.execute(strsql)
    conn.commit()
    viewpagerlist = []
    row = cursor.fetchone()
    while row:
        viewpagerlist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    s = str(viewpagerlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def news(request):
    username = request.POST.get("username")
    news = request.POST.get("news")
    t = datetime.datetime.now()
    ctime = t.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('insert into tbnews (author,contents,createtime) value (%s,%s,%s)',(username,news,ctime))
    conn.commit()
    s="{\"msg\":\"留言成功\"}"
    res="["+s+"]"
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

# 订单
@xframe_options_exempt
def getorderlist(request):
    userid = request.POST.get("userid")
    print(userid)
    strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo,proname,proid,procount,imgurl,price from v_order where memberid=" + userid
    cursor.execute(strsql)
    conn.commit()
    orderlist = []
    row = cursor.fetchone()
    while row:
        orderlist.append({"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4],"sumprice": str(row[5]), "memberid": str(row[6]), "ctime": row[7], "ptime": row[8],"memo": row[9], "proname": row[10], "proid": row[11], "procount": row[12], "imgurl": row[13],"price": str(row[14])})
        row = cursor.fetchone()
    s = str(orderlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def saveorder(request):
    t = datetime.datetime.now()
    ctime = t.strftime('%Y-%m-%d %H:%M:%S')
    orderid = datetime.datetime.strftime(t, "%Y%m%d%H%M%S%f")
    userid= request.POST.get("userid")
    sumprice = request.POST.get("sumprice")
    sname = request.POST.get("sname")
    stel = request.POST.get("stel")
    saddress = request.POST.get("saddress")
    ptime = request.POST.get("ptime")
    memo = request.POST.get("memo")
    #插入表头信息
    cursor.execute("insert into tborderhead (orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo) values ('"+orderid+"','"+sname+"','"+stel+"','"+saddress+"',"+sumprice+","+userid+",'"+ctime+"','"+ptime+"','"+memo+"')")
    conn.commit()

    #把购物车里面的数据插入到订单明细表
    #先把购物车里当前这个人的菜品查询出来
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    #构造插入订单明细表的sql语句
    sqllists = []
    row = cursor.fetchone()
    while row:
        #{"id": row[0], "sessionid": row[1], "proname": row[2], "proid": row[3], "procount": row[4], "ctime": row[5],"imgurl": row[6], "price": str(row[7])}
        sqllists.append("insert into tborderitems (orderid,proid,proname,price,procount,imgurl) values ('"+orderid+"',"+str(row[3])+",'"+row[2]+"',"+str(row[7])+","+str(row[4])+",'"+row[6]+"')")
        row = cursor.fetchone()
    #遍历sql列表，执行插入订单明细表操作
    for sqlitem in sqllists:
        cursor.execute(sqlitem)
        conn.commit()
    #清空购物车
    cursor.execute("delete from tbshoppingcar where sessionid="+userid)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

