import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:

    with open(filename, "r", newline=new_line) as f:

        text = f.readline().replace('\n', '').split(delimiter)
        text[-1] = text[-1].replace('\r', '')

        con = [{text[i]: val for i, val in enumerate(l_.replace('\n', '').replace('\r', '').split(delimiter))} for l_ in f.readlines()]

        return con


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
