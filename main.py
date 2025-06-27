# main.py

from game import Hero,start_game,where_to_go_intown,what_to_do, get_into_shop
def main():
    hero = start_game()
    while True:
        path = where_to_go_intown()
        while True:
            if path == "3":
                result = get_into_shop(hero)
            else:
                result = what_to_do(hero, path)
            if result == "exit":
                break


if __name__ == "__main__":
    main()
