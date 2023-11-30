def short_list_declarative(numbers):
    return sorted(numbers, reverse=True)

# Пример использования
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = short_list_declarative(numbers)
print("Отсортированный список в порядке убывания:", sorted_numbers)
