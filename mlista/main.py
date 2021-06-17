from mlist import MList
from termcolor import colored


def start():
    while True:
        capacity_set = input(colored("Podaj początkowy rozmiar listy: ", "green"))
        try:
            val = int(capacity_set)
            if val > 0:
                my_list = MList(capacity_set)
                break
            else:
                print(colored("Zły początkowy rozmiar! Spróbuj ponownie. \n", "red"))
        except ValueError:
            print(colored("WRONG! Proszę podać liczbę. \n", "red"))

    while True:
        print("\n Wybierz polecenie: "
              "\n - pisz \n - dodaj_element \n - znajdz \n - pobierz \n - rozmiar "
              "\n - pojemnosc \n - usun_powtorzenia \n - odwroc \n - zwieksz_pojemnosc "
              "\n - zmniejsz_pojemnosc \n - wyjscie")
        command = input("Twój wybór: ")

        if command == "pisz":
            my_list.write()

        elif command == "dodaj_element":
            x = input("Podaj element: ")
            my_list.add_item(x)

        elif command == "znajdz":
            y = input("Podaj szukany element: ")
            my_list.find(y)

        elif command == "pobierz":
            z = input("Podaj index listy: ")
            my_list.download(z)

        elif command == "rozmiar":
            my_list.my_size()

        elif command == "pojemnosc":
            my_list.my_capacity()

        elif command == "usun_powtorzenia":
            e = input("Podaj jaki powtarzający się element usunąć: ")
            my_list.rem_rep(e)

        elif command == "odwroc":
            my_list.reverse()

        elif command == "zwieksz_pojemnosc":
            o = input("Podaj zwiększoną pojemność listy: ")
            my_list.inc_capacity(o)

        elif command == "zmniejsz_pojemnosc":
            p = input("Podaj zmniejszoną pojemność listy: ")
            my_list.red_capacity(p)

        elif command == "wyjscie":
            print(colored("Papa :) ! \n", "blue"))
            exit()

        else:
            print(colored("Oooops!! Wrong command, try again! \n", "red"))


if __name__ == '__main__':
    start()
