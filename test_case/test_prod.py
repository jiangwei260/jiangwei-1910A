from tools.api import request_tool
from tools.security.md5_tool import md5_passwd

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

def test_json02(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '添加产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {'token':pub_data['token']}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "brand": "苹果果",
  "colors": [
    "玫瑰金","英伦白","中国红"
  ],
  "price": 5100,
  "productCode": "自动生成 字符串 5 数字字母",
  "productName": "苹果10pro",
  "sizes": [
    "5寸"
  ],
  "type": "手机"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]


def test_change_price(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改商品价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    data = {"SKU":pub_data["skuCode"],"price":5890}
    headers = {"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None


    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,data=data,method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_full_sku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '全量调整单个商品库存'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    data = {"skuCode":pub_data["skuCode"],"qty":10000}
    headers = {"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None


    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,data=data,method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)




# featuredef test_post_json(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "产品模块"  # allure报告中一级分类
#     story = '无签名无加密下单'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/order/addOrder"  # 接口地址
#     data = {"skuCode":pub_data["skuCode"],"qty":10000}
#     headers = {"token":pub_data["token"]}
#     json_data = '''
#       {
#
#     "ordeerPrice": 5890,
#     "orderLineList": [
#       {
#         "qty": 100,
#         "skuCode": "${skuCode}"
#       }
#     ],
#     "receiver": "丁满",
#     "receiverPhone": "13255889963",
#     "receivingAddress": "上海",
#     "sign": "",
#     "userName": "xuepl111"
#
#       }
#           '''
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(json_data=json_data,headers=headers,data=data, method=method, url=uri, pub_data=pub_data, status_code=status_code, expect=expect)

def test_post_sign(pub_data):
        method = "POST"  #请求方法，全部大写
        feature = "订单模块"  # allure报告中一级分类
        story = '签名下单接口'  # allure报告中二级分类
        title = "全字段正常流_1"  # allure报告中用例名字
        uri = "/order/addOrderSignBody"  # 接口地址
        headers = {"token":pub_data["token"]}
        s = "receiver=丁满&ordeerPrice=5890&receiverPhone=13255889963&key=guoya"
        sign = md5_passwd(s,"")
        pub_data["sign"] = sign



        # post请求json数据，注意数据格式为字典或者为json串 为空写None
        json_data = '''
        {

    "ordeerPrice": 5890,
    "orderLineList": [
      {
        "qty": 100,
        "skuCode": "${skuCode}"
      }
    ],
    "receiver": "丁满",
    "receiverPhone": "13255889963",
    "receivingAddress": "上海",
    "sign": "${sign}",
    "userName": "xuepl111"

      }
        '''
        status_code = 200  # 响应状态码
        expect = ""  # 预期结果
        # --------------------分界线，下边的不要修改-----------------------------------------
        # method,pub_data和url为必传字段
        request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
