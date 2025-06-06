# main.py

from battle import Hero,start_game,where_to_go_intown,what_to_do
def main():
    hero = start_game()
    while True:
        path = where_to_go_intown()
        while True:
            result = what_to_do(hero, path)
            if result == "exit":
                break


if __name__ == "__main__":
    main()
