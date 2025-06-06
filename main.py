# main.py

from battle import Hero, generate_enemy, battle

def main():
    player = Hero(100, 25, 15)
    enemy = generate_enemy()
    print(f"你遇到了一隻 level {enemy.level} 的 {enemy.name}")
    battle(player, enemy)

if __name__ == "__main__":
    main()
