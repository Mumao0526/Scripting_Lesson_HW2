id = str(input('請輸入您的學號: '))
name = str(input('請輸入您的姓名: '))
chineseScore = float(input('請輸入您的國文成績: '))
mathScore = float(input('請輸入您的數學成績: '))
csScore = float(input('請輸入您的電腦成績: '))

print('-'*10)

print(f'{name}({id})同學您好:')
print('以下是您的各科成績與分數評定')
print()
total = chineseScore + mathScore + csScore
avg = total/3
print(f'國文: {chineseScore} / 數學: {mathScore} / 電腦: {csScore}')
print(f'總分: {total} / 平均: {avg}')

print('-'*10)

isPass =  '合格' if avg > 60 else '不合格'
print(f'成績判定: {isPass}')