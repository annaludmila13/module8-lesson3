def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not hasattr(numbers, '__iter__') or isinstance(numbers, str):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)

        # Если все данные некорректные, возвращаем 0
        if len(numbers) == incorrect_data:
            return 0

        # Вычисляем среднее
        return total_sum / (len(numbers) - incorrect_data)

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанный список
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректный список



