i = 3;
while i > 0:
    password = input('請輸入密碼')
    if password != 'a123456':
        print('密碼不正確')
        i = i - 1
        print('請重新輸入密碼:')
        if i > 0:
            print('還有', i ,'次機會')
        else:
            print('沒機會嘗試了')
    else:
        print('登入成功')
        break