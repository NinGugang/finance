def complain():
    text = input('Введите текст жалобы: ')
    f = open('complain.txt', 'a', encoding='utf-8')
    f.write(text + '\n')
    f.close()
    print('Ваша жалоба будет рассмотрена в ближайшем времени ')
def bank():
    print('Предложение банка')
    f = open('bank.txt', 'r', encoding='utf-8')
    text = f.read()
    print(text)
    f.close()


