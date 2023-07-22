import time

def focus_timer(duration):
    print(f"专注时钟 {duration // 60} 分钟 {duration % 60} 秒开始！")
    time.sleep(duration)
    print("时间到！专注结束！")

if __name__ == "__main__":
    try:
        focus_duration = int(input("请输入专注时长（分钟）：60")) * 60
        focus_timer(focus_duration)
    except ValueError:60
        print("请输入有效的数字！")
