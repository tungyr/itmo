import json

def http_headers_to_json(txt_file_path, json_file_path):
    """Перевод заголовков из html в json"""
    with open(txt_file_path) as f:
        string = f.readline()
        string = string.split()
        dict_json = {}

        if string[1] == '200':
                dict_json['protocol'] = string[0]
                dict_json['status_code'] = string[1]
                dict_json['status_message'] = string[2]

        elif string[1] == '301':
                dict_json['protocol'] = string[0]
                dict_json['status_code'] = string[1]
                dict_json['status_message'] = string[2] + ' ' + string[3]

        elif string[0] == 'GET':
                dict_json['method'] = string[0]
                dict_json['uri'] = string[1]
                dict_json['protocol'] = string[2]


        with open(txt_file_path) as f:
            f.readline()
            for i in f:
                if i != '\n':
                    i = i.replace('\n','')
                    i = i.split(': ')
                    dict_json.update({i[0]:i[1]})


        with open(json_file_path, 'w') as f:
                json.dump(dict_json, f, indent=4)
