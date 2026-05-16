import random


def guess_number_game():
    """猜數字遊戲主程式"""
    print("=" * 50)
    print("         歡迎玩猜數字遊戲！")
    print("=" * 50)
    print("\n規則：")
    print("1. 電腦會隨機選擇一個 1 到 100 之間的數字")
    print("2. 你需要猜出這個數字")
    print("3. 電腦會告訴你猜的數字是太大或太小")
    print("4. 看你需要多少次才能猜對！\n")

    # 電腦隨機選擇一個數字
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # 獲取使用者輸入
            user_input = input("請輸入你的猜測 (1-100)：").strip()
            
            # 驗證輸入
            if not user_input.isdigit():
                print("❌ 請輸入有效的數字！\n")
                continue
            
            guess = int(user_input)
            
            if guess < 1 or guess > 100:
                print("❌ 請輸入 1 到 100 之間的數字！\n")
                continue
            
            attempts += 1
            
            # 比較猜測和正確答案
            if guess == secret_number:
                print(f"\n🎉 恭喜你！你猜對了！答案是 {secret_number}")
                print(f"⭐ 你用了 {attempts} 次嘗試！\n")
                
                # 根據嘗試次數給出評分
                if attempts == 1:
                    print("👑 完美！第一次就猜對！")
                elif attempts <= 5:
                    print("🌟 很棒！你很聰明！")
                elif attempts <= 10:
                    print("✨ 不錯！再加油！")
                else:
                    print("💪 繼續練習，下次會更好！")
                
                guessed = True
            elif guess < secret_number:
                print(f"📈 太小了！請試試更大的數字。(已嘗試 {attempts} 次)\n")
            else:
                print(f"📉 太大了！請試試更小的數字。(已嘗試 {attempts} 次)\n")
        
        except ValueError:
            print("❌ 請輸入有效的數字！\n")


def play_again():
    """詢問使用者是否要再玩一次"""
    while True:
        choice = input("你想再玩一次嗎？(是/否)：").strip().lower()
        if choice in ['是', 'y', 'yes']:
            return True
        elif choice in ['否', 'n', 'no']:
            return False
        else:
            print("❌ 請輸入『是』或『否』\n")


def main():
    """主函式 - 控制遊戲流程"""
    play = True
    games_played = 0
    
    while play:
        guess_number_game()
        games_played += 1
        play = play_again()
    
    print(f"\n感謝玩遊戲！你一共玩了 {games_played} 局。")
    print("再見！👋\n")


if __name__ == "__main__":
    main()
