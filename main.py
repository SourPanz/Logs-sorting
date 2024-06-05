from datetime import datetime


class Operation:
    def __init__(self, duration, info):
        self.duration = duration  # duration - время выполнения операции
        self.info = info  # info - информация об операции

    def __str__(self):
        # строковое представление объекта
        return 'Время выполнения: {}\tИнформация: {}'.format(self.duration, self.info)


# получение всех операций
def get_raw_operations_from_file(folder):
    operations = []
    with open(folder, 'r', encoding='utf-8') as file:
        for line in file:
            operations.append(line)
    return operations


# преобразуем строку во время
def get_time(operation):
    FORMAT = '%H:%M:%S.%f'
    time_index = 12
    return datetime.strptime(operation[:time_index], FORMAT)


# находим длительность операции
def get_duration(operation, next_operation):
    return get_time(next_operation) - get_time(operation)


# проверяем начинается ли строка с времени
def is_time(operation):
    digit_index = 2
    return operation[:digit_index].isdigit()


# сортируем по убыванию длительности операции
def get_sorted(result):
    result = sorted(result, key=lambda log: log.duration, reverse=True)
    return result


# получаем отсортированный список длительности операций и информацию об операциях
def get_operations(operations):
    result = []
    info_index = 36
    operation = operations[0]
    for i in range(1, len(operations)):
        next_operation = operations[i]
        if is_time(next_operation):
            result.append(Operation(get_duration(operation, next_operation), operation[info_index:].lstrip()))
            operation = next_operation
        else:
            operation = operation + next_operation
            continue
    return get_sorted(result)


# вводим путь, количество выводимых элементов, получаем ответ
def find_answer():
    print('Путь файла без кавычек:')
    folder = input()
    print('Введите число операций, которые нужно вывести:')
    line_count = int(input())
    return get_operations(get_raw_operations_from_file(folder))[:line_count]


print(*find_answer())

