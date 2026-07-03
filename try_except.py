try:
    n = int(input('> '))
    if n == 100:
        raise ValueError('запрещенное значение')
except (ValueError, TypeError) as err:
    print('Error', err)
# except TypeError as err:
#     print('Error', err)
except ZeroDivisionError as err:
    print('Error', err)
else:
    print('выполняется при отсутствии ошибки')
finally:
    print('выполняется всегда')
# except Exception as err:
#     print( err)
# n = int(input('> '))