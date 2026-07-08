# Python+Pytest 接口自动化测试框架
## 项目简介
基于 Python + Pytest 搭建的数据驱动接口自动化测试框架，通过 Excel 管理全部测试用例，支持 HTTP 接口请求、接口间数据传递、MySQL 数据库校验，集成 Allure 生成可视化测试报告，低代码维护用例，开箱即用。

### 核心能力
1. 数据驱动：Excel 统一管理用例，新增/修改接口无需改动代码
2. 多请求类型：GET/POST，支持 json/data/params/files/headers 传参
3. 数据提取复用：JsonPath 提取响应参数、SQL 查询数据，跨用例传递
4. 双层断言：接口返回值断言 + MySQL 数据库结果断言
5. 可视化报告：Allure 生成分层测试报告，记录执行步骤、失败详情
6. 完整日志：控制台+本地文件双日志输出，方便定位问题
7. 模块化解耦：请求、断言、用例解析、工具类完全分离，易扩展维护

## 技术栈
- 测试运行框架：pytest
- HTTP 请求库：requests
- Excel 读写：openpyxl
- JSON 解析提取：jsonpath
- MySQL 操作：pymysql
- 测试报告：allure-pytest
- 动态参数渲染：jinja2
- 日志：logging

## 项目目录结构
auto_api_test/
├── run.py # 项目启动入口，执行用例 + 生成 allure 报告
├── pytest.ini # pytest 全局配置、日志配置
├── config/
│ └── config.py # 全局配置：域名、数据库、用例文件路径
├── utils/
│ ├── excel_utils.py # Excel 用例读取工具
│ ├── analyse_case.py # 用例参数解析工具
│ ├── send_request.py # http 请求、mysql 连接封装
│ ├── asserts.py # 通用断言封装（接口 / 数据库）
│ ├── allure_utils.py # allure 报告标签、标题封装
│ └── extractor.py # 数据提取工具（响应 /sql 提取）
├── testcases/
│ └── test_runner.py # 测试执行主逻辑，参数化执行所有用例
├── test_data/ # 存放 Excel 测试用例文件
├── logs/ # 自动生成运行日志
└── report/ # allure 原始数据与最终 html 报告
