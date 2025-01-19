import requests
from bs4 import BeautifulSoup
import time
import random
'''
这段代码是不能运行的，因为已经404了，仅供参考
'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

f = open('D:/Python/pythonProject10/doupo.txt', 'a+')

def get_info(url):
    try:
        res = requests.get(url, headers=headers,timeout=10) # 设置超时时间
        res.raise_for_status() # 检查请求是否成功
        soup = BeautifulSoup(res.content, 'html.parser') # 适用BeautifulSoup 解析 html
        contents = soup.find_all('p')
        for content in contents:
            f.write(content.get_text() + '\n') # 写入文件
    except requests.exceptions.RequestException as e:
        print(f"请求失败:{url},错误：{e}")





if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range (2,1665)]
    with open('D:/Python/pythonProject10/doupo.txt','a+',encoding='utf-8') as f:
        for url in urls:
            get_info(url)
            time.sleep(random.uniform(1,3))



