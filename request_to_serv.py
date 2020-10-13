
import urllib.request
import urllib
import json

'''
http://127.0.0.1
7777
2
4

    a = [
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

    with open(file, 'r') as file:
        lines = file.readlines()
    url = lines[0].strip()
    port = int(lines[1].strip())
    a, b = lines[2].strip(), lines[3].strip()
    return url, port, a, b


def main():
    url, port, a, b = get_input_data(file='input.txt')

    url_values = urllib.parse.urlencode({'a': int(a), 'b': int(b)})
    response = urllib.request.urlopen(f'{url}:{port}/?{url_values}')

    content = response.read().decode(response.headers.get_content_charset()).strip()
    data = json.loads(content)

    if len(data) != 10:
        raise ValueError('asdf')

    # if data[0] != 8:
    # 	raise ValueError('sadf')
    # if data[1] != 6:
    # 	raise ValueError('sadf')
    # if data[2] != -2:
    # 	raise ValueError('sadf')
    # if data[3] != 2:
    # 	raise ValueError('sadf')
    # if data[4] != 4:
    # 	raise ValueError('sadf')        
    # if data[5] != 17:
    # 	raise ValueError('sadf')  
    # if data[6] != 256:
    # 	raise ValueError('sadf')   
    # if data[7] != 1024:
    # 	raise ValueError('sadf')   
    # if data[8] != -17:
    # 	raise ValueError('sadf')   
    # if data[9] != -19:
    # 	raise ValueError('sadf')         
    if not isinstance(data, list):
        raise ValueError('sdf')
        
    # a = data[10]
    s = 0
    for i in range(len(data)):
    	s += data[i]
    
    #print(1279)
    with open('output.txt', 'w') as f:
        f.write(f'{s}')
    print(s)


if __name__ == '__main__':
    main()
