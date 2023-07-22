
import time

# 读取倒计时起止时间
with open("countdown.txt", "r") as f:
    start_time_str, end_time_str = f.readlines()

start_time = time.mktime(time.strptime(start_time_str.strip(), "%Y-%m-%d %H:%M:%S"))
end_time = time.mktime(time.strptime(end_time_str.strip(), "%Y-%m-%d %H:%M:%S"))

# 计算倒计时剩余秒数
now = time.time()
left_seconds = int(end_time - now)

while left_seconds > 0:
    # 格式化输出剩余时间
    print(f"距离 {end_time_str.strip()} 还有 {left_seconds // 86400} 天 {left_seconds // 3600 % 24} 小时 {left_seconds // 60 % 60} 分钟 {left_seconds % 60} 秒")

    # 等待一秒钟
    time.sleep(1)

    # 更新剩余秒数
    left_seconds = int(end_time - time.time())

# 倒计时结束
print("时间到！")
