password = 123456
count = 3
while True:
	x = input('請輸入密碼： ')
	if int(x) == 123456:
		print('登入成功!')
		break
	else:
		count = count - 1
		if count == 0:
			print('密碼錯誤！ 帳號鎖定15分鐘')
			break
		print('密碼錯誤! 還有', count, '次機會')



