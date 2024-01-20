import json
client_info = {}



def load():
    global client_info
    with open('client.json', 'r', encoding='utf-8') as json_file:
        client_info = json.load(json_file)





def save():
    global client_info
    with open('client.json', 'w', encoding='utf-8') as outfile:
        json.dump(client_info, outfile)


def show_info():
    print('Информация о счетах')
    print('--------------------------------------------------------')
    for account in client_info['accounts']:
        print(f'Имя: {account["name"]}')
        print(f'Платежная система: {account["system"]}')
        print(f'Номер: {account["number"]}')
        print(f'Тип: {account["type"]}')
        print(f'Баланс: {account["balance"]}')
        print(f'Срок действия: {account["validity period"]}')
        print('--------------------------------------------------------')
def predict():
    expenses = 0
    income = 0
    months = []
    for transaction in client_info['transactions']:
        if transaction['type'] == 'списание':
            expenses += transaction['amount']
        if transaction['type'] == 'зачисление':
            income += transaction['amount']
        if transaction['date'] not in months:
            months.append(transaction['date'])
        print('Предполагаемые расходы в следующем месяце', expenses / len(months))
        print('Предполагаемые доходы в следующем месяце', income / len(months))





def make_transaction():
    global client_info
    print('Доступные счета')
    a = 1
    for account in client_info['accounts']:
        print(f'{a} - {account["name"]} - {account["number"]}')
        a += 1
    account_num = int(input('Введите счет: '))
    for a in range(len(client_info['accounts'])):
        if a + 1 == account_num:
            account = client_info['accounts'][a]['number']
            break
    else:
        print('Такого аккаунта не сущевствует')
        return
    print("Типы транзакций:")
    print("1 - списание")
    print("2 - зачисление")
    transaction_type = input('Введите тип транзакции: ')
    if transaction_type == '1':
        transaction_type = 'списание'
    elif transaction_type == '2':
        transaction_type = 'зачисление'
    else:
        print('Такого типа не сущевствует')
        return
    print('Дата транзакций: ')
    year = input('Введите год: ')
    month = input('Введите месяц: ')
    if int(year) > 2024 or int(month) > 12 or int(month) < 1:
        print('Неверная дата')
        return
    try:
        amount = int(input('Введите сумму: '))
    except:
        print('Ошибка ввода')
        return
    if amount < 1:
        print("Сумма не может быть меньше одного")
    if transaction_type == 'списание':
        client_info['accounts'][account_num - 1]['balance'] -= amount
    elif transaction_type == 'зачисление':
        client_info['accounts'][account_num - 1]['balance'] += amount
    client_info['transactions'].append({
        'account': account,
        'type': transaction_type,
        'date': {'year': year, 'month': month},
        'amount': amount
    })
    print(client_info['transactions'][-1])
    print('Транзакиця записана')
