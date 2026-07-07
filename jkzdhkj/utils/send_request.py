import allure
import pymysql
import requests


@allure.step("2.发送HTTP请求")
def send_request(**request_data):
    res = requests.request(**request_data)
    return res


def send_jdbc_request(sql,index=0):
    connect = pymysql.Connect(
        host="127.0.0.1",
        port=3306,
        database="mydb",
        user="root",
        password="123456",
        charset="utf8"
    )
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()  # 返回来的是一个元组
    cursor.close()
    connect.close()
    return result[index]



