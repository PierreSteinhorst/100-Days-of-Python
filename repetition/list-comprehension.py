# # # create a list
# # list = [1, 23, 8, 37, 32, 90]
# # print(list)
# # # create another list where values multiply by 2
# # list2 = []
# # for element in list:
# #     list2.append(element * 2)
# # print(list2)
# #
# # # with list comprehension:
# # list_comprehension = [ x * 2 for x in list]
# # print(list_comprehension)
# #
# # list_comprehension = [ x * 2 for x in list if x != 23]
# # print(list_comprehension) # value = 23 is missing
# # list3 = [ x * 2 for x in list_comprehension]
# # print(list3)
#
# '''
# Aufgabe 1
# ----------
# Schreibe als for-Schleife UND List-Comprehension
#     Eingabe: Liste von Zahlen
#     Wenn die Zahl 42 ist: Zahl ignorieren
#     Sonst multipliziere die Zahl mit 10
# '''
#
# string_of_numbers = input("Geben sie die gewünschten Ganzzahlen ein: ")
# list_of_numbers = list(string_of_numbers.split(" "))
# # convert string value into int
# list = []
# for number in list_of_numbers:
#     number = int(number)
#     list.append(number)
#
# new_list = []
# # Lösung for-Loop
# for entry in list:
#     if entry != 42:
#         new_list.append(entry * 10)
#
# print(f"Original List: {list}")
# print(f"For-Loop List: {new_list}")
#
# # Lösung List Cpmrehension
# new_List_Comprehension = [ element * 10 for element in list if element != 42]
# print(f"List Comprehension: {new_List_Comprehension}")

'''
Aufgabe 2
----------
Schreibe ein Programm, welches alle Primzahlen unter 100 findet. Es MUSS
diese Zahlen selbst berechnen.
'''


def prime():
    for number in range(2, 101):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print(number)

prime()