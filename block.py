from reverseCipher import message

while i >= 0:
    translated = translated + message[i]
    print('i is', i, ', message[i] is', message[i], ', translated is',
          translated)
    i = i - 1

print(translated)