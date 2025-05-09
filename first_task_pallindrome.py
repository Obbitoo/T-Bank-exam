def pallindrome(word):
    flag = False
    for i in range(len(word)):
        temp_list = list(word)
        temp_list.pop(i)
        check_word = ''.join(temp_list)
        if check_word == check_word[::-1]:
            flag = True
            break
    return flag


x_word = input()
if pallindrome(x_word):
    print('YES')
else:
    print('NO')
