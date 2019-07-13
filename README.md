# weakpasswd

##### explain
根据账户信息及常见后缀组合生成密码  
例如：  
张三 "zhangsan","zs"  
注册网址 "github","github.com"  
会根据这两项关键词生成弱密码 

##### usage
explain: 根据常见词及常用后缀组合生成密码  
common_suffix：常见后缀列表，可自行扩展  
common_conjunction：常见连接符  
word1和word2：输入要生成的相关信息  

执行

```
python3 weakpasswd.py
```
会在当前目录生成名为weakpasswd.txt文件

##### result

![image](https://github.com/Sexisnull/weakpasswd/blob/master/1.png)