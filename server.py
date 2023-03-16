import socket

dictionary = {
    "Hello": "Hello, welcome to chatGPT",
    "Hi": "Hi, welcome to chat",
    "What is the capital of Great Britain": "London",
    "What is the capital of Ukraine": "Kyiv",
    "How are you?": "I`m fine. What about you?",
    "Thanks, ok": ';)',
    "Bye": 'Goodbye, see you next time.'
    }

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
conn, addr = sock.accept()
print('connected:', addr)

while True:
    host, port = addr
    from_client = str((conn.recv(1024)).decode())
    print('Client-'+str(port)+': ', from_client)
    answer = 'I don`t know. What do you mean?'
    if from_client in dictionary:
        answer = dictionary[from_client]

    print('I`m: ', answer)

    count_words = len(from_client.split(' '))
    answer = str(count_words) + "::" + answer

    if from_client == 'Bye':
        to_client = bytes(answer + " Connection closed. Server shutdown", encoding='UTF-8')
        conn.send(to_client)
        break
    else:
        to_client = bytes(answer, encoding='UTF-8')
        conn.send(to_client)

conn.close()
