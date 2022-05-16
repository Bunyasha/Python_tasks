# Напишите программу, удаляющую из текста все слова, содержащие "абв".
text=list(map(str,input('Введите текст: ').split()))
text=' '.join(text)
text=text.lower()
print(type(text))
print(text)

def delete_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ''.join(text)


text = delete_words(text)
print(text)