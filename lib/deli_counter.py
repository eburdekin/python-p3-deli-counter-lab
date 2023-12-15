katz_deli = []


def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            message += f" {i + 1}. {katz_deli[i]}"
        print(message)


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    number = katz_deli.index(name) + 1
    print(f"Welcome, {name}. You are number {number} in line.")


def now_serving(l):
    if not l:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {l[0]}.")
        del l[0]
