import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"倒计时 {minutes} 分钟开始！")
    time.sleep(seconds)
    print(f"时间到！你已专注了 {minutes} 分钟！")

if __name__ == "__main__":
    minutes = int(input("请输入专注的时间（分钟）："))
    focus_timer(minutes)
