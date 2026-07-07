import allure
from jinja2 import Template
import jsonpath
import pymysql
import pytest
import requests
from utils.allure_utils import allure_init
from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import read_excel
from utils.send_request import send_request, send_jdbc_request


class TestRunner:

    #读取测试用例文件中的所有数据
    data = read_excel()

    # 提取后的数据通过初始化一个空字典{}来保存
    all = {}

    @pytest.mark.parametrize("case", data)
    def test_case(self,case):

        # 引用全局的all
        all = self.all

        # 根据all的值，渲染case
        case = eval(Template(str(case)).render(all))

        #初始化allure报告
        allure_init(case)

        # 1.解析请求数据
        request_data = analyse_case(case)

        # 2.发起请求获取相应结果
        res = send_request(**request_data)
        # res = requests.request(**request_data)

        # 3.处理断言
        #HTTP响应断言

        http_assert(case,res)
        # assert res.json()["meta"]["msg"] == case["expected"]
        # if case["check"]:
        #     assert jsonpath.jsonpath(res.json(),case["check"])[0] == case["expected"]
        # else:
        #     assert case["expected"] in res.text

        #数据库断言
        jdbc_assert(case)
        # if case["sql_check"] and case["sql_expected"]:
        #     assert send_jdbc_request(case["sql_check"]) == case["sql_expected"]


            # connect = pymysql.Connect(
            #     host = "127.0.0.1",
            #     port = 3306,
            #     database = "mydb",
            #     user = "root",
            #     password = "123456",
            #     charset = "utf8"
            # )
            # cursor = connect.cursor()
            # cursor.execute(case["sql_check"])
            # result = cursor.fetchone() #返回来的是一个元组
            # cursor.close()
            # connect.close()
            # assert result[0] == case["sql_expected"]



        # 4.提取
        # json提取
        if case["jsonExData"]:
            for key, value in eval(case["jsonExData"]).items():
                value = jsonpath.jsonpath(res.json(),value)[0]
                all[key] = value


        # 数据库提取
        if case["sqlExData"]:
            for key, value in eval(case["sqlExData"]).items():

                value = send_jdbc_request(value)
                all[key] = value
                # connect = pymysql.Connect(
                #     host="127.0.0.1",
                #     port=3306,
                #     database="mydb",
                #     user="root",
                #     password="123456",
                #     charset="utf8"
                # )
                # cursor = connect.cursor()
                # cursor.execute(value)
                # result = cursor.fetchone()  # 返回来的是一个元组
                # cursor.close()
                # connect.close()
                # value = result[0]
                # all[key] = value




