#coding:gbk
'''
������ȡ2017��Ҫ���з��۹��ʱ����а�
���ߣ������
ʱ�䣺2020��3��6��
'''
import requests
import bs4
import re
import openpyxl
#��ȡ��ҳ
def get_url(url):
    res = requests.get(url)
    return res
#��ȡ��ҳ����
def get_data(res):
    data_target = []
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    content = soup.find(id="Cnt-Main-Article-QQ")#������ҳ�к�id="Cnt-Main-Article-QQ"���������ݣ�<class 'bs4.element.Tag'>
    # content2 = soup.find_all(id="Cnt-Main-Article-QQ")#�����б�
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
#�����excel�ļ���
def to_excel(data_target):
    wb = openpyxl.Workbook()#������������
    wb.guess_types= True
    ws = wb.active
    ws.append(['����','ƽ������','ƽ������','���۹��ʱ�'])#��һ��
    for each in data_target:
        ws.append(each)
    wb.save('2017��Ҫ���з��۹��ʱ����а�.xlsx')#����
#������
def main():
    url = 'https://news.house.qq.com/a/20170702/003985.htm'
    res = get_url(url)
    data_target = get_data(res)
    to_excel(data_target)
    # with open('2017��������.txt','w',encoding = 'utf-8') as f:
    #     f.write(res.text)

if __name__=='__main__':
    main()

