#密码重试程式

#先在程式码中 设定好密码 password = 'a123456'
#最多输入三次密码
#如果正确 就印出'登录成功'
#如果不正确 就印出'密码错误！还有____ 几次机会！'
password = 'a123456'
i = 3
while True:
    pwd = input('请输入密码：')	
    if pwd == 'password':
        print('登入成功')
        break # 逃出回圈
    else:
    	i = i - 1
    	print('密码错误！还有', i ,'次机会')
    	if 1 == 0:
    		break