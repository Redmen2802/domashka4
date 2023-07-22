def foo(text):
    """большие буквы"""
    return text.upper()

def foo2(text):
    '''Каждое новое слово с большой буквы'''
    return text.title()

user_input = input('Введите текст')
user_input2 = input('Введите текст')

print(foo(user_input))
print(foo2(user_input2))