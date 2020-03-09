#coding:gbk
'''
程序：爬取网易云热评
作者：徐佳梁
时间：2020年3月5日
'''
import requests
import json
def get_target_url(target_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    data = {'params':'9ZL19VKcX7r7YUOQQPQ2zCXp+m5YIEqiiNpom+8jyuk8RHNZxn/D9Z+vcYFxJkbPX39J5Tw9eMqznN1VKbri3b52unc5vnYetvGHPluKmdUL4tgUZwo/qLZzAD0uSQie5VovvuwrbuJhfNQakSVwQPvOi31MH5vtMzR9LpLnQxVHDwkZ4pJzLENELqWEF/Ig'
            ,'encSecKey':'1ae8cb6fa7af617a0bf839f4d495c233c97bd7ed0d2b12f4306770b97df2727006062d68bc8f3f6da9b9765b9ab9d1ef58f0cd65901cccc51cb1b94506a3983659b538a8411632cd77a1b4e48e6d67c727ea5a73bfdb4c5ea708c0d0f3ac13e9c36fc47d4d74bf06cf2f91e6480ceaabda9ea7ab7ecb6ff59dbabea41ffbf0b8'}

    res = requests.post(target_url,data = data,headers = headers)
    return res

def get_hot_comments(res,music_name):
    comments = json.loads(res.text)
    hot_comments = comments['hotComments']
    # print(hot_comments)
    with open(music_name+'热评.txt','w',encoding='utf-8') as f:
        for each in hot_comments:
            f.write('id:{}\n'.format(each['user']['nickname']))
            f.write('评论：{}\n'.format(each['content']))
            f.write('——————————————————————————————————————————\n')
    # print(comments["hotComments"])


def main():
    print('请输入音乐名称：')
    music_name = str(input())
    print('请输入音乐网址：')
    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(input().split('=')[1])
    res = get_target_url(target_url)
    # print(res.text)
    get_hot_comments(res,music_name)

if __name__=='__main__':
    main()

