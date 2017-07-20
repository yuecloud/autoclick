#coding:utf-8

#登录web.qq.com,手机扫描登录。先手动发一条消息，fiddler或者其它截包工具截取数据包然后补充相应的字段即可

import  requests
import  json
import  urllib


header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' ,
        'Content-Type':'application/x-www-form-urlencoded',
        # 'Accept-Language':'zh-CN,zh;q=0.8',
        #对应的Cookie值
        'Cookie':'ts_last=web2.qq.com/; ts_uid=9687364960; pgv_info=ssid=s4697267024; pgv_pvid=3247915406; pgv_pvi=3346720768; pgv_si=s9721352192; ptisp=ctc; RK=XfHCZhM+zv; pt2gguin=o2880263944; uin=o2880263944; skey=@4RJxqm0n6; p_uin=o2880263944; p_skey=ab0mFgk3q-8Pq-mFlaMqe*svWhh-3RzNGws3mzA8awo_; pt4_token=1LZpLUdelyvYCakyOCTdzZq30fgr3wBovgD-Huxb01s_; ptwebqq=30aa7a7a7ad91ac7f60ad6004c463e0bf52cad5a7eae9916ac459e11bdb13d3e',
        # 'Origin':'https://d1.web2.qq.com',
        'Referer':'https://d1.web2.qq.com/cfproxy.html?v=20151105001&callback=1',

        }



#发送个人信息接口
url='https://d1.web2.qq.com/channel/send_buddy_msg2'

#发送群信息接口
url2='https://d1.web2.qq.com/channel/send_qun_msg2'

#发送讨论组接口
url3="https://d1.web2.qq.com/channel/send_discu_msg2"

str1="[\"https://www.qiushibaike.com/\",[\"font\",{\"name\":\"黑体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]"

str2="[\"sb\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]"

#对应上传的字段值
data = "r=%s" %  json.dumps({"to":997531575,"content":str2,"face":0,"clientid":53999199,"msg_id":95860002,"psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857"})


print requests.post(url,data=data,verify=False,headers = header).content
