import os
import pytest

if __name__ == "__main__":
    pytest.main(["-vs","./testcases/testrunner.py", "--alluredir","./report/json_report", "-clean_alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")
