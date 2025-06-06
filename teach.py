import random
class hero:
  def __init__(self,health,attack,defense):
    self.health=health
    self.attack=attack
    self.defense=defense
    self.XP=0
    self.lvl=1
    self.backpack={"道具":[],"金幣":0,"武器":[],"防具":[]}
class enemy:
  def __init__(self,health,attack,defense,level,name):
    self.health=health
    self.attack=attack
    self.defense=defense
    self.level=level
    self.name=name
BT=hero(100,25,15)


monster_name=random.choice(["哥布林","骷髏弓箭手","史萊姆"])
if monster_name== "哥布林":
  level=random.randint(1,15)
  health=50+level*5
  attack=20+level*3
  defense=10+level*2
  enemy1=enemy(health,attack,defense,level,monster_name)
elif monster_name== "骷髏弓箭手":
  level=random.randint(1,15)
  health=50+level*5
  attack=20+level*3
  defense=10+level*2
  enemy1=enemy(health,attack,defense,level,monster_name)
elif monster_name== "史萊姆":
  level=random.randint(1,15)
  health=50+level*5
  attack=20+level*3
  defense=10+level*2
  enemy1=enemy(health,attack,defense,level,monster_name)

print(f"你遇到了一隻 level {enemy1.level}的{enemy1.name}")
round_num=1

while BT.health>0 and enemy1.health>0:
  levelup = False
  print("===================================")
  print(f"第{round_num}回合")

  print(f"你的血量{BT.health} 攻擊力{BT.attack} 防禦力{BT.defense}")
  print(f"{enemy1.name}的血量{enemy1.health} 攻擊力{enemy1.attack} 防禦力{enemy1.defense}")
  hero_action=input("請選擇行動(1.攻擊/2.防禦):")
  if hero_action!="1" and hero_action!="2":
      print("請重新輸入")
      continue
  round_num+=1
  #依照敵人行動隨機選擇
  enemy_action=random.choice(["1","2"])
  
  #雙方都攻擊
  if hero_action=="1"and enemy_action=="1":
    print(f"勇者與{enemy1.name}都發動了攻擊")
    enemy_battle_attack=enemy1.attack+random.randint(-10,10)
    BT_battle_attack=BT.attack+random.randint(-10,10)
    print(f"勇者的攻擊力{BT_battle_attack} {enemy1.name}的攻擊力{enemy_battle_attack}")
    if enemy_battle_attack>BT_battle_attack:#敵人攻擊力大於我方攻擊力
        BT.health-=enemy_battle_attack
        print(f"勇者受到了{enemy_battle_attack}點傷害")
    elif enemy_battle_attack<BT_battle_attack:#我方攻擊力大於敵人攻擊力
        enemy1.health-=BT_battle_attack
        print(f"{enemy1.name}受到了{BT_battle_attack}點傷害")
    elif enemy_battle_attack==BT_battle_attack:#雙方攻擊力相同
        print(f"勇者與{enemy1.name}的攻擊力相同，雙方都沒有受到傷害")

  #雙方都防禦
  elif hero_action=="2"and enemy_action=="2": 
    print(f"勇者與{enemy1.name}都發動了防禦")

  #我方攻擊 敵人防禦
  elif hero_action=="1"and enemy_action=="2":
    print(f"勇者發動了攻擊 {enemy1.name}防住了攻擊")
    enemy_battle_defense=enemy1.defense+random.randint(-10,10)
    BT_battle_attack=BT.attack+random.randint(-10,10)
    print(f"勇者的攻擊力{BT_battle_attack} {enemy1.name}的防禦力{enemy_battle_defense}")
    if enemy_battle_defense>BT_battle_attack:
      BT.health-=enemy_battle_defense-BT_battle_attack
      print(f"勇者受到了反擊傷害{enemy_battle_defense-BT_battle_attack}")
    elif enemy_battle_defense<BT_battle_attack:
      continue

  #我方防禦 敵人攻擊
  elif hero_action=="2"and enemy_action=="1":

    print(f"勇者發動了防禦 {enemy1.name}攻擊被擋下來了")
    enemy_battle_attack=enemy1.attack+random.randint(-10,10)
    BT_battle_defense=BT.defense+random.randint(-10,10)
    print(f"勇者的防禦力{BT_battle_defense} {enemy1.name}的攻擊力{enemy_battle_attack}")
    if enemy_battle_attack>BT_battle_defense:
        continue
    elif enemy_battle_attack<BT_battle_defense:
      enemy1.health-=BT_battle_defense-enemy_battle_attack
      print(f"{enemy1.name}受到了反擊傷害{BT_battle_defense-enemy_battle_attack}")
  print("===================================")
  #戰鬥結束
  if BT.health<=0:
      print("勇者戰敗")
      break
  elif enemy1.health<=0:
    print(f"勇者戰勝了{enemy1.name}")
    BT.XP+=abs(enemy1.level-BT.lvl)*10
    print(f"獲得經驗值{abs(enemy1.level-BT.lvl)*10}")
    if BT.XP>=BT.lvl*100:
      BT.XP-=BT.lvl*100
      BT.lvl+=1
      levelup = True
      print(f"升級了!目前等級{BT.lvl}")
    if levelup:
      print(f"目前的屬性:攻擊{BT.attack} 防禦{BT.defense} 血量{BT.health}")
      print(f"請分配10點屬性點")
      while True:
        try:
          attack_point = int(input("請分配攻擊點數:"))
          defense_point = int(input("請分配防禦點數:"))
          health_point = int(input("請分配血量點數:"))
          if attack_point + defense_point + health_point != 10:
            print("請重新分配10點屬性點")
            continue
          else:
            BT.attack += attack_point
            BT.defense += defense_point
            BT.health += health_point
            levelup = False
            break
        except ValueError:
          print("請輸入正確的數字")
    print(f"目前的屬性:攻擊{BT.attack} 防禦{BT.defense} 血量{BT.health}")
    print(f"目前的經驗值{BT.XP} 等級{BT.lvl}")
      
        

'''
跟怪物可以進行防禦或攻擊
如果都用攻擊 攻擊力低的會受到傷害 攻擊力高的不會
如果用防禦 攻擊力如果比防禦還低 會受到反傷害的 如果比防禦還高 不會受到傷害
戰鬥時的數值會是自己的數值+-10
然後戰勝後會依照等級給予經驗值
'''