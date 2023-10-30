num = int(input('請輸入數量:'))

for i in range(1,num,2):
    s = '*' * i
    print(f'{s:^{num}}')
for i in range(num,-1,-2):
    s = '*' * i
    print(f'{s:^{num}}')
    
print()
