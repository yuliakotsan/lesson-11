import socket

port = 55000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', int(port)))
while True:
    _str = input('I`m: ')
    _bytes = bytes(_str, encoding='UTF-8')
    count_bytes = sock.send(_bytes)

    data = str((sock.recv(1024)).decode())
    if len(data) == 0:
        print('Server: Disconnected...')
        print('If you want to continue chatting, please run server then client sides.')
        sock.close()
        break
    count_words, data = data.split('::')
    print("\t\t" + count_words + (" word" if (int(count_words) == 1) else " words"))
    print('Server: ', data)

sock.close()

