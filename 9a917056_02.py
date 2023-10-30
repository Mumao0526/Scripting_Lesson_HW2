student = {}
student['id'] = str(input('請輸入您的學號: '))
student['name'] = str(input('請輸入您的姓名: '))
student['chineseScore'] = float(input('請輸入您的國文成績: '))
student['mathScore'] = float(input('請輸入您的數學成績: '))
student['csScore'] = float(input('請輸入您的電腦成績: '))

print('-'*10)

print(f'{student['name']}({student['id']})同學您好:')
print('以下是您的各科成績與分數評定')
print()
total = student['chineseScore'] + student['mathScore'] + student['csScore']
avg = round(total/3, 2)
print(f'國文: {student['chineseScore']} / 數學: {student['mathScore']} / 電腦: {student['csScore']}')
print(f'總分: {total} / 平均: {avg}')

print('-'*10)

isPass =  '合格' if avg > 60 else '不合格'
print(f'成績判定: {isPass}')
print()
