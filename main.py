import json
import requests
from urllib import parse
import  time
import schedule

def select():
    header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    url = "https://www.gdghospital.org.cn/Ajax/AjaxData.aspx"
    body = {"action": "GetdoctorSearch",
            "dockey": "刘媛"}
    payload = parse.urlencode(body)

    r = requests.post(url, headers=header, data=payload)  # 请求url，获得返回的数据信息
    text = r.text  # 获得的返回数据使用text方法进行获取
    # print(text)
    jsonobj = json.loads(text)  # 将响应内容转换为Json对象

    message = jsonobj["data"][0]["hasRegInfo"]  # 从Json对象获取想要的内容
    # print(message)

    if message > "2023-07-09":
        requests.get(url="https://xizhi.qqoq.net/XZeaee627d888d0f67a6af89a2f327d423.channel?title=有新的排班时间&content=有新的排班时间")
    else:
            print("没放号排班时间")
while True:
    time.sleep(60)
    select()
