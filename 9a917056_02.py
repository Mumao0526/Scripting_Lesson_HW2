student = {}
student["sid"] = str(input("請輸入您的學號: "))
student["sname"] = str(input("請輸入您的姓名: "))
student["fchina"] = float(input("請輸入您的國文成績: "))
student["fmath"] = float(input("請輸入您的數學成績: "))
student["finfo"] = float(input("請輸入您的電腦成績: "))

print("-" * 30)

print(f"{student['sname']}({student['sid']})同學您好:")
print("以下是您的各科成績與分數評定")
print()
total = student["fchina"] + student["fmath"] + student["finfo"]
avg = round(total / 3, 2)
print(
    f"國文: {student['fchina']} / "
    f"數學: {student['fmath']} / "
    f"電腦: {student['finfo']}"
)
print(f"總分: {total} / 平均: {avg}")

print("-" * 30)

isPass = "合格" if avg > 60 else "不合格"
print(f"成績判定: {isPass}")
print()
