
def sort_list_imperative(numbers):# Процедура в императивном стиле
    n = len(numbers)
    # Проходим по списку и меняем местами соседние элементы местами
    for i in range(n):
        for j in range(n - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

def sort_list_declarative(numbers):# Процедура в декларативном стиле
    return sorted(numbers, reverse=True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [5, 2, 8, 3, 1, 6]
    print("Массив до сортировки", numbers)
    #print("Массив до сортировки", sort_list_imperative(numbers))
    print("Массив до сортировки", sort_list_declarative(numbers))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
