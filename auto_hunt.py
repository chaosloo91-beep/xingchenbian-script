# 自动打怪脚本

import time
import random

class AutoHunt:
    def __init__(self):
        self.monsters = ['怪物A', '怪物B', '怪物C']
        self.is_hunting = True

    def hunt(self):
        while self.is_hunting:
            monster = random.choice(self.monsters)
            print(f'发现 {monster}，开始攻击！')
            time.sleep(random.randint(1, 3))  # 模拟攻击时间
            print(f'击败 {monster}！')
            time.sleep(2)  # 模拟冷却时间

    def stop_hunt(self):
        self.is_hunting = False
        print('停止自动打怪。')

if __name__ == '__main__':
    auto_hunt = AutoHunt()
    try:
        auto_hunt.hunt()
    except KeyboardInterrupt:
        auto_hunt.stop_hunt()