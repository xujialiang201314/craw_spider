#coding:gbk
'''
������ȡ�嵰��������ͼ
���ߣ������
ʱ�䣺2020��2��18��
'''
import urllib.request
import  os
import random
import  time
#ʹ�ô���ip
ip_list = ['183.146.213.198:80','218.75.158.153:3128']
my_ip = random.choice(ip_list)
print(my_ip)
proxy_support = urllib.request.ProxyHandler({'http':my_ip})
opener = urllib.request.build_opener(proxy_support)  #���ơ�����һ��opener
urllib.request.install_opener(opener)#��װopener  #����opener
opener.addheaders =[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')]

#������ҳ
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    # print(html)
    return html

#��ȡͼƬ��ҳ�����֣��Ѽ��ܣ�
# def get_page(url):
#     html = url_open(url).decode('utf-8')
#     a = html.find('current-comment-page')
#     a = html.find('jandan.net/00xx/',a)
#     b = html.find('#comments',a)+9
#     print(html[a:b])
#     return 'http://'+html[a:b]
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('<a title="Older Comments" href=') + 32
    b = html.find('��һҳ</a>',a) - 32
    # print(html[a:b])

    return html[a:b]


#��ȡͼƬ��ַ
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    # print(a)
    while a!=-1:
        b = html.find('.jpg',a,a+255)
        # print(b)

        if b != -1:
            img_addrs.append('http:'+html[a+9:b+4])
            # print(html[a+9:b+4])
        else:
            b=a+9
        a = html.find('img src=',b)
    # print(img_addrs)
    return img_addrs


#����ͼƬҳ��
def save_imgs(folder,img_addrs):
    for each in img_addrs:
        file_name = each.split('/')[-1]
        with open(file_name,'wb') as f:
            with open(file_name,'wb') as f:
                img = url_open(each)
                f.write(img)

#����ͼƬ�����������ļ�����
def download_mm(folder='xxoo',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/ooxx/'
    next_page = 'http://jandan.net/ooxx/MjAyMDAyMTktMTYx#comments'
    # next_page = url + 'MjAyMDAyMTktMTU1' + '#comments'
    # print(x)
    # page_url = url + get_page(url)+'#coments'
    # img_addrs = find_imgs(page_url)
    # save_imgs(folder, img_addrs)
    # page_num = int(get_page(url))
    for page in range(pages):
        # page_url = url + str(next_page) + '#coments'
        img_addrs = find_imgs(next_page)
        save_imgs(folder,img_addrs)
        next_page = 'http:' + get_page(url)
        time.sleep(5)

if __name__ == '__main__':
    print('��������ȡ��ҳ������5����ʾ��ȡ5��ҳ���ͼƬ����')
    pages = int(input())
    folder = 'xxoo'
    download_mm(folder, pages)