import yaml
import time
import os

def sleep(n_secs):
    time.sleep(n_secs)

def get_attr(args):
    dicAttr = {}
    dicAttr['appID'] = "wx834a306b55370aa5"
    dicAttr['appsecret'] = "6dd19d35febb424e4dd4941e453693ee"
    dicAttr['grant_type'] = "client_credential"
    return dicAttr[args]

def setup_test_step(content):
    print("测试步骤开始:%s"%content)
def teardown_test_step(content):
    print("测试步骤结束:%s"%content)
def setup_test_case(content):
    print("测试用例开始:%s"%content)
def teardown_test_case(content):
    print("测试用例结束:%s"%content)


def toISO(t):
	return t.encode("utf8").decode("iso8859-1")