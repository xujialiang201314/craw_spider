#coding:gbk
'''
���򣺴���վ�����أ���ȡ��һ��è��ͼƬ
���ߣ������
'''
# import urllib.request
#
# response = urllib.request.urlopen('http://placekitten.com/400/400')  #��ȡurl���������󣬲��õ���Ӧ
# cat_img = response.read()          #��ȡ����
# # print(response.geturl())
# # print(response.info())
# # print(response.getcode())
# print(response)
# # print(type(response))
# with open('cat_400_400.jpg','wb') as f:    #��������
#     f.write(cat_img)

import requests
response = requests.get('http://placekitten.com/400/400')
# print(response.text)
# cat_img = response.read()
with open('cat_400_400_2.jpg','wb') as f:
    f.write(response.content)
