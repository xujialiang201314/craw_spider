#coding:gbk
'''
���򣺽�����top250��Ӱ�񵥷���excel��
���ߣ������
ʱ�䣺2020��3��9��
'''
import openpyxl

with open('����top250.txt','rt') as f:
    t = f.read()
    print(type(t))
wb = openpyxl.Workbook()
# wb.guess_types= True
ws = wb.active
ws.append(['����','��Ӱ��'])
for lines in t.split('\n'):
    ws.append(lines.split('  '))
wb.save('����top250.xlsx')
