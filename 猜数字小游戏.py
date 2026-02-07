import random

def guess_number_game():
    """猜数字小游戏：1-100随机数，提示大小，统计次数"""
    print("🎉 欢迎来到猜数字小游戏！")
    print("我已经想好了1-100之间的一个整数，快来猜吧！")
    
    # 生成随机数
    secret_num = random.randint(1, 100)
    guess_count = 0  # 猜的次数
    
    while True:
        try:
            # 获取用户输入
            user_guess = int(input("\n请输入你猜的数字："))
            guess_count += 1
            
            # 判断逻辑
            if user_guess < secret_num:
                print("❌ 太小了，再往大了猜！")
            elif user_guess > secret_num:
                print("❌ 太大了，再往小了猜！")
            else:
                print(f"\n🎉 恭喜你猜对了！答案就是{secret_num}！")
                print(f"你一共猜了{guess_count}次，真棒！")
                break  # 猜对退出循环
        except ValueError:
            # 处理非数字输入
            print("⚠️ 请输入有效的整数哦！")

# 启动游戏
if __name__ == "__main__":
    guess_number_game()
