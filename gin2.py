def lol(name):
    ind = 0
    with open(name +'.txt', encoding='UTF-8') as file:
        a= file.read().split('/n')
    while True:
        if ind> len(a) -1:
            break
        stroka = yield a[ind]
        if stroka == 'next':
            ind += 1
        if stroka == 'previous' and ind >= 1:
            ind -=1

ginet = lol('gin')
print(next(ginet))
print(ginet.send('next'))
print(ginet.send('previous'))
