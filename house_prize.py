#coding:gbk
'''
程序：爬取2017主要城市房价工资比排行榜
作者：徐佳梁
时间：2020年3月6日
'''
import requests
import bs4
import re
import openpyxl
#获取网页
def get_url(url):
    res = requests.get(url)
    return res
#提取网页数据
def get_data(res):
    data_target = []
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    content = soup.find(id="Cnt-Main-Article-QQ")#返回网页中含id="Cnt-Main-Article-QQ"的所有内容，<class 'bs4.element.Tag'>
    # content2 = soup.find_all(id="Cnt-Main-Article-QQ")#返回列表
    # print(content)
    # print(type(content2))
    data = content.find_all('p',style="TEXT-INDENT: 2em")
    # print(data)
    data = iter(data)
    for line in data:
        # print(line.text)
        if line.text.isnumeric():
            data_target.append([
                re.search(r'\[(.+)\]',next(data).text).group(1),
                re.search(r'\d.*', next(data).text).group(),
                re.search(r'\d.*', next(data).text).group(),
                re.search(r'\d.*', next(data).text).group(),
            ])
    # print(data_target)
    return data_target
#保存进excel文件中
def to_excel(data_target):
    wb = openpyxl.Workbook()#创建工作环境
    wb.guess_types= True
    ws = wb.active
    ws.append(['城市','平均房价','平均工资','房价工资比'])#第一行
    for each in data_target:
        ws.append(each)
    wb.save('2017主要城市房价工资比排行榜.xlsx')#保存
#主函数
def main():
    url = 'https://news.house.qq.com/a/20170702/003985.htm'
    res = get_url(url)
    data_target = get_data(res)
    to_excel(data_target)
    # with open('2017房价排行.txt','w',encoding = 'utf-8') as f:
    #     f.write(res.text)

if __name__=='__main__':
    main()

