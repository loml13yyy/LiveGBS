# LiveGBS
LiveGBS弱口令即用户注册漏洞单批检测脚本
![图片](https://github.com/user-attachments/assets/5f5c76f8-a563-4d45-9b97-36d746586ac4)

```shell
漏洞描述：
LiveGBS save接口处存在逻辑缺陷漏洞，当Cisco IOS XE Web UI在互联网公开时，恶意攻击者可能会利用此漏洞添加具有15级访问权限的账户，使服器处于继不安全的状态

fofa搜索语句：
icon_hash="-206100324"

工具利用：
  -h, --help            show this help message and exit
  -u URL, --url URL     单个漏洞网址
  -f FILE, --file FILE  批量检测文本

PS：
成功检测到漏洞时，脚本会自动生成一个success.txt文件用于存放成功的url
```

