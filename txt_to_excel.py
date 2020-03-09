#coding:gbk
'''
程序：将豆瓣top250电影榜单放入excel中
作者：徐佳梁
时间：2020年3月9日
'''
import openpyxl

with open('豆瓣top250.txt','rt') as f:
    t = f.read()
    print(type(t))
wb = openpyxl.Workbook()
# wb.guess_types= True
ws = wb.active
ws.append(['排名','电影名'])
for lines in t.split('\n'):
    ws.append(lines.split('  '))
wb.save('豆瓣top250.xlsx')
