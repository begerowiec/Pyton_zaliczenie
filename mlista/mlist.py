from termcolor import colored


class MList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.elements = []

    def write(self):
        print(colored("Rozmiar listy: " + str(self.size), "yellow"))
        print(colored("Pojemność listy: " + self.capacity, "yellow"))
        print(colored("Elementy: [", "yellow"), end='')
        for x in range(len(self.elements)):
            if x+1 < len(self.elements):
                print(self.elements[x] + ",", end='')
            else:
                print(self.elements[x], end='')

        print(colored("]", "yellow"))

    def add_item(self, x):
        if int(self.capacity) > int(self.size):
            self.elements.append(x)
            self.size = self.size + 1
            return True
        else:
            print(colored("Przekroczono pojemność listy!", "red"))
            return False

    def find(self, search_element):
        flag = True
        for x in range(len(self.elements)):
            if self.elements[x] == search_element:
                print(colored("Pozycja podanego elementu w liście: " + str(x), "yellow"))
                flag = False
                return True
        if flag:
            print(colored("Brak podanego elementu w liście", "red"))
            return False

    def download(self, element):
        element = int(element)
        if element < int(self.size):
            print(colored("Element o indeksie[ " +
                          str(element) + "] to: " +
                          str(self.elements[element]), "yellow"))
            return True
        else:
            print(colored("Pod podanym indeksem nie ma żadnego elementu", "red"))
            return False

    def my_size(self):
        print(colored("Aktualny rozmiar wynosi: " + str(self.size), "yellow"))
        return int(self.size)

    def my_capacity(self):
        print(colored("Aktualna pojemność wynosi: " + str(self.capacity), "yellow"))
        return int(self.capacity)

    def rem_rep(self, torem):
        flag = True
        todel = []
        for x in range(len(self.elements)):
            if self.elements[x] == torem and not flag:
                todel.append(x)
                self.size = self.size - 1
            elif self.elements[x] == torem and flag:
                flag = False
        res = todel[::-1]
        for y in range(len(res)):
            del self.elements[res[y]]

    def reverse(self):
        res = self.elements[::-1]
        self.elements = res

    def inc_capacity(self, val):
        if int(val) > 0 and int(val) > int(self.capacity):
            self.capacity = val
            return True
        else:
            print(colored("Nie można zwiększyć pojemności", "red"))
            return False

    def red_capacity(self, val):
        if 0 < int(val) < int(self.capacity) and int(val) >= self.size:
            self.capacity = val
            return True
        else:
            print(colored("Nie można zmniejszyć pojemności", "red"))
            return False
