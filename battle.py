# rpg_module.py

import random

class Hero:# 定義勇者類別
    """勇者類別，包含屬性和背包"""
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.XP = 0
        self.lvl = 1
        self.Gold = 0
        
        self.backpack_weapons = []
        self.backpack_armor = []
        self.backpack_loots = []
        self.backpack_items = []
        self.backpack = {
            "weapons": self.backpack_weapons,
            "armor": self.backpack_armor,
            "item": self.backpack_items,
            "loots": self.backpack_loots
        }
    def show_backpack_weapons(self):
        if self.backpack["weapons"]:
            print(f"武器背包: {', '.join(self.backpack['weapons'])}")
        else:
            print("武器背包: 無物品")
    def show_backpack_armor(self):
        if self.backpack["armor"]:
            print(f"護甲背包: {', '.join(self.backpack['armor'])}")
        else:
            print("護甲背包: 無物品")
    def show_backpack_items(self):
        if self.backpack["item"]:
            print(f"道具背包: {', '.join(self.backpack['item'])}")
        else:
            print("道具背包: 無物品")


# 定義敵人類別
class Enemy:
    def __init__(self, health, attack, defense, level, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.name = name

def generate_enemy_in_cave():
    monster_name = random.choice(["哥布林", "骷髏弓箭手", "史萊姆"])
    level = random.randint(1, 15)
    health = 50 + level * 5
    attack = 20 + level * 3
    defense = 10 + level * 2
    return Enemy(health, attack, defense, level, monster_name)
def generate_enemy_in_forest():
    monster_name = random.choice(["狼", "熊", "樹精"])
    level = random.randint(1, 1)
    health = 50 + level * 5
    attack = 20 + level * 3
    defense = 10 + level * 2
    return Enemy(health, attack, defense, level, monster_name)


#遊戲開始
def start_game():
    print("歡迎來到冒險遊戲!")
    print("你將扮演一位勇者，與各種怪物戰鬥，提升自己的等級和屬性。")
    print("祝你好運!")
    hero = Hero(100, 25, 15)
    return hero
#選擇路徑
def where_to_go_intown():
    print("你正在城鎮中，你可以選擇以下路徑:")
    print("1. 前往山脈")    
    print("2. 探索洞穴")
    choice = input("請選擇路徑(1/2):") 
    if choice not in ["1", "2"]:
        print("無效的選擇，請重新選擇。")
        return where_to_go_intown() 
    elif choice == "1":
        print("你選擇了前往山脈。")
        print("====================================")
    elif choice == "2":
        print("你選擇了探索洞穴。")
        print("====================================")
    return choice
    
def get_item(hero, item):
    if item == "道具":
        hero.backpack_items.append("道具")
        print("你獲得了一個道具，已加入背包。")
    elif item == "寶箱":
        hero.backpack_loots.append("寶箱")
        print("你獲得了一個寶箱，已加入背包。")
    elif item == "武器":
        weapon = random.choice(["劍", "斧頭", "弓"])
        hero.backpack_weapons.append(weapon)
        print(f"你獲得了一把 {weapon}，已加入背包。")

def what_we_meet(hero, path):  # 新增 hero 參數
    encounter = random.choice(["enemy", "item", "nothing"])
    if encounter == "enemy":
        enemy = generate_enemy_in_cave() if path == "2" else generate_enemy_in_forest()
        print("===================================")
        print(f"你遇到了一隻 level {enemy.level} 的 {enemy.name}")
        return enemy
    elif encounter == "item":
        item = random.choice(["道具", "寶箱", "武器"])
        get_item(hero, item)
        return item
    else:
        print("這裡什麼都沒有，你繼續前進。")
        return None

    
#選擇行動
def what_to_do(hero, path):
    print("你可以選擇以下行動:")
    print("1. 查看背包")
    print("2. 休息")
    print("3. 繼續冒險")
    print("4. 離開這裡")
    choice = input("請選擇行動(1/2/3/4):")
    if choice == "1":
        hero.show_backpack_weapons()
        hero.show_backpack_armor()
        hero.show_backpack_items()
    elif choice == "2":
        print("你休息了一會兒，恢復了部分體力。")
        hero.health += 20
        if hero.health > 100:
            hero.health = 100
    elif choice == "3":
        print("你決定繼續冒險。")
        encounter = what_we_meet(hero,path)
        if isinstance(encounter, Enemy):
            battle(hero, encounter)
        elif isinstance(encounter, str):
            print(encounter)

    elif choice == "4":
        print("你決定離開這裡，回到城鎮。")
        return "exit"





def battle(hero, enemy):
    round_num = 1
    while hero.health > 0 and enemy.health > 0:
        levelup = False
        print("===================================")
        print(f"第{round_num}回合")
        print(f"你的血量{hero.health} 攻擊力{hero.attack} 防禦力{hero.defense}")
        print(f"{enemy.name}的血量{enemy.health} 攻擊力{enemy.attack} 防禦力{enemy.defense}")
        
        hero_action = input("請選擇行動(1.攻擊/2.防禦):")
        if hero_action not in ["1", "2"]:
            print("請重新輸入")
            continue

        round_num += 1
        enemy_action = random.choice(["1", "2"])

        if hero_action == "1" and enemy_action == "1":
            print(f"勇者與{enemy.name}都發動了攻擊")
            enemy_battle_attack = enemy.attack + random.randint(-10, 10)
            hero_battle_attack = hero.attack + random.randint(-10, 10)
            print(f"勇者的攻擊力{hero_battle_attack} {enemy.name}的攻擊力{enemy_battle_attack}")
            if enemy_battle_attack > hero_battle_attack:
                hero.health -= enemy_battle_attack
                print(f"勇者受到了{enemy_battle_attack}點傷害")
            elif hero_battle_attack > enemy_battle_attack:
                enemy.health -= hero_battle_attack
                print(f"{enemy.name}受到了{hero_battle_attack}點傷害")
            else:
                print("雙方攻擊力相同，無人受傷")

        elif hero_action == "2" and enemy_action == "2":
            print(f"勇者與{enemy.name}都發動了防禦")

        elif hero_action == "1" and enemy_action == "2":
            print(f"勇者發動了攻擊 {enemy.name}防住了攻擊")
            enemy_battle_defense = enemy.defense + random.randint(-10, 10)
            hero_battle_attack = hero.attack + random.randint(-10, 10)
            print(f"勇者的攻擊力{hero_battle_attack} {enemy.name}的防禦力{enemy_battle_defense}")
            if enemy_battle_defense > hero_battle_attack:
                damage = enemy_battle_defense - hero_battle_attack
                hero.health -= damage
                print(f"勇者受到了反擊傷害{damage}")
            elif hero_battle_attack > enemy_battle_defense:
                pass

        elif hero_action == "2" and enemy_action == "1":
            print(f"勇者發動了防禦 {enemy.name}攻擊被擋下來了")
            enemy_battle_attack = enemy.attack + random.randint(-10, 10)
            hero_battle_defense = hero.defense + random.randint(-10, 10)
            print(f"勇者的防禦力{hero_battle_defense} {enemy.name}的攻擊力{enemy_battle_attack}")
            if enemy_battle_attack < hero_battle_defense:
                damage = hero_battle_defense - enemy_battle_attack
                enemy.health -= damage
                print(f"{enemy.name}受到了反擊傷害{damage}")

        print("===================================")
        if hero.health <= 0:
            print("勇者戰敗")
            print("遊戲結束")
            return 
        elif enemy.health <= 0:
            print(f"勇者戰勝了{enemy.name}")
            # 獲得經驗值和升級
            hero.Gold += enemy.level * 10
            gain_xp = (abs(enemy.level - hero.lvl) + 1) * 10
            hero.XP += gain_xp
            print(f"獲得經驗值{gain_xp}")
            if hero.XP >= hero.lvl * 100:
                hero.XP -= hero.lvl * 100
                hero.lvl += 1
                levelup = True
                print(f"升級了!目前等級{hero.lvl}")
            if levelup:
                allocate_stat_points(hero)
            print(f"目前的屬性:攻擊{hero.attack} 防禦{hero.defense} 血量{hero.health}")
            print(f"目前的經驗值{hero.XP} 等級{hero.lvl}")

def allocate_stat_points(hero):
    print("請分配10點屬性點")
    while True:
        try:
            attack_point = int(input("請分配攻擊點數:"))
            defense_point = int(input("請分配防禦點數:"))
            health_point = int(input("請分配血量點數:"))
            if attack_point + defense_point + health_point != 10:
                print("請重新分配10點屬性點")
                continue
            else:
                hero.attack += attack_point
                hero.defense += defense_point
                hero.health += health_point
                break
        except ValueError:
            print("請輸入正確的數字")
