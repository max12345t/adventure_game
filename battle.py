# rpg_module.py

import random

class Hero:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.XP = 0
        self.lvl = 1

class Enemy:
    def __init__(self, health, attack, defense, level, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.name = name

def generate_enemy():
    monster_name = random.choice(["哥布林", "骷髏弓箭手", "史萊姆"])
    level = random.randint(1, 15)
    health = 50 + level * 5
    attack = 20 + level * 3
    defense = 10 + level * 2
    return Enemy(health, attack, defense, level, monster_name)

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
            break
        elif enemy.health <= 0:
            print(f"勇者戰勝了{enemy.name}")
            gain_xp = abs(enemy.level - hero.lvl) * 10
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
