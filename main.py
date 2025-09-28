# main.py
def is_leap_year(year):
    if year < 0:
        return False
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

if __name__ == "__main__":
    input_val = input().strip()
    try:
        year = int(input_val)
        if is_leap_year(year):
            print("是闰年")
        else:
            print("不是闰年")
    except ValueError:
        print("输入错误")
