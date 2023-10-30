num = int(input("請輸入星星數量:"))

if num % 2 != 0:
    for i in range(num):
        if i <= num // 2:
            print(' ' * (num//2 - i) + '*' * (i * 2 + 1))
        else:
            print(' ' * (i - num//2) + '*' * (i * -2 + num * 2 - 1))
else:
    for i in range(num + 1):
        if i < num // 2:
            print(' ' * (num//2 - i) + '*' * (i * 2 + 1))
        elif i == num // 2:
            print('*' * num)
        else:
            print(' ' * (i - num//2) + '*' * (i * -2 + num * 2 + 1))

print()
