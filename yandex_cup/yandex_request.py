import json
import sys
import urllib

import requests

'''
Разработчики бекенда часто взаимодействуют с многочисленными API, результаты которых нужно ещё и дополнительно обрабатывать. Сейчас вам придётся сделать именно это!
Во входном файле четыре строчки. В первой находится URL сервера, во второй — номер порта. В следующих двух строках записаны два целых 32-разрядных числа: соответственно, a и b. Необходимо осуществить GET-запрос к серверу по указанному номеру порта, передав значения чисел a и b в значениях одноимённых параметров запроса. Сервер ответит JSON-массивом из целых чисел. Сумму этих чисел необходимо распечатать в выходной файл.
Гарантируется, что общее количество чисел в ответе не превосходит 100, при этом каждое из них — 32-разрядное знаковое целое число.

http://127.0.0.1
7777
2
4

[  
  8,  
  6,  
  -2,  
  2,  
  4,  
  17,  
  256,  
  1024,  
  -17,  
  -19  
]

'''
def get_input_data(file):

    with open(file, 'r') as f:
        lines = f.readlines()
    url = lines[0].strip()
    port = int(lines[1].strip())
    a, b = lines[2].strip(), lines[3].strip()
    return url, port, a, b


def main():
    url, port, a, b = get_input_data(file='input.txt')
    response = requests.get(f'{url}:{port}', params={'a': int(a), 'b': int(b)})
    # response = requests.get(f'http://google.com:80', params={'a': a, 'b': b})
    url_values = urllib.parse.urlencode({'a': int(a), 'b': int(b)})
    response = urllib.request.urlopen(f'{url}:{port}?{url_values}')
    content = response.read().decode(response.headers.get_content_charset())
    if not isinstance(content, list):
        raise ValueError('sdf')
    with open('output.txt', 'w') as f:
        f.write(str('asdf'))

    if len(data) != 10:
        raise ValueError('asdf')
    l = json.loads(data)

    print(sum(l))


ans = [
    8,
    6,
    -2,
    2,
    4,
    17,
    256,
    1024,
    -17,
    -19
]
if __name__ == '__main__':
    main()
