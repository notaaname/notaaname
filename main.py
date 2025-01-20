import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

info_lists = []

def judgment_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'

def get_info(url):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status() # 检查请求是否成功
        ids = re.findall(r'<h2>(.*?)</h2>', res.text, re.S)
        levels = re.findall(r'<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
        sexs = re.findall('<div class="articleGender(.*?)">', res.text, re.S)
        for id, level, sex in zip(ids, levels, sexs):
            info = {
                'id': id.strip(), # 去除空白字符
                'level': level.strip(),
                'sex': judgment_sex(sex.strip())
            }
            info_list.append(info)
    except requests.exceptions.RequestException as e:
        print(f"请求失败{url},错误,{e}")


if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/text/page/{}'.format(str(i)) for i in range(1,36)]
    with open('D:/Python/pythonProject10/qiushi.txt', 'w', encoding='utf-8') as f:
        pass

    for url in urls:
        get_info(url)
        print(f"一抓取{url}")


    with open('D:/Python/pythonProject10/qiushi.txt', 'a',encoding='utf-8') as f:
        for info_list in info_lists:
            f.write(info_list['id']) + '\n'
            f.write(info_list['level']) + '\n'
            f.write(info_list['sex']) + '\n'



