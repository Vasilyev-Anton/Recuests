import requests

list_with_heroes = list()
dict_with_heroes = dict()


def get_characters(name):
    response = requests.get('https://superheroapi.com/api/2619421814940190/search/{}'.format(name))
    res = response.json()
    list_with_heroes.append(res)
    return list_with_heroes


def compare_characters(*other):
    for item in list_with_heroes:
        for element in item['results']:
            if element['name'] in other:
                for characteristic in element['powerstats']:
                    if characteristic == 'intelligence':
                        value = int(element['powerstats'][characteristic])
                        temp_dict = {element['name']: value}
                        dict_with_heroes.update(temp_dict)
    max_value = max(dict_with_heroes.values())
    for hero, intelligence in dict_with_heroes.items():
        if intelligence == max_value:
            print(f"Самый умный супергерой - {hero}")


get_characters('Hulk')
get_characters('Thanos')
get_characters('Captain America')

compare_characters('Hulk', 'Thanos', 'Captain America')
