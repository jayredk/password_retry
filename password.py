# 密碼重試程式
# password - '123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 輸入正確 則印出 “登入成功！”
# 輸入錯誤 則印出 ”密碼錯誤！還有＿次機會“	

password = '123456'
count = 3
while count > 0:
	x = input('請輸入密碼： ')
	count = count - 1
	if x == password:
		print('登入成功!')
		break
	else:
		if count == 0:
			print('密碼錯誤！ 帳號鎖定15分鐘')
			break
		print('密碼錯誤! 還有', count, '次機會')



