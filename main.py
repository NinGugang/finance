from client import *
from bank import *
from plot import *
if __name__ == '__main__':
    load()
    command = ''
    while command != '10':
        print("Доступные действия:")
        print("1 - посмотреть предложения банка")
        print("2 - отправить жалобу")
        print("3 - информация о счетах")
        print("4 - посмотреть прогноз доходов и расходов на следующий месяц")
        print("5 - добавить транзакцию")
        print("6 - посмотреть график доллара к рублю")
        print("7 - посмотреть график доллара к биткоину")
        print("10 - выйти")
        command = input('выберите действие: ')
        if command == '1':
            bank()
        elif command == '2':
            complain()
        elif command == '3':
            show_info()
        elif command == '4':
            predict()
        elif command == '5':
            make_transaction()
        elif command == '6':
            rub_usd()
        elif command == '7':
            usd_btc()
        elif command == '10':
            print('Сохранение изменений...')
            save()
            print('До свидания')
        else:
            print('Действие не распознано')
        input()





