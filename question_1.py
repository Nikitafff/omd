def foo(text):
    return {text.split()[x]: text.split().count(y) for x, y in enumerate(text.split())}

print(foo('dfasdfadf adfadsf sdfadf adfadsf adfadf'))
