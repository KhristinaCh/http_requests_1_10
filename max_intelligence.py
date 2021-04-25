import requests

characters_list = ['Hulk', 'Captain America', 'Thanos']
ids_list = {}
intelligence_list = {}


def search_id(name):
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    response = requests.get(url)
    data = response.json()
    for item in data['results']:
        if f'{name}' == item['name']:
            ids_list[int(item['id'])] = name


def search_intelligence(_id):
    url = f'https://superheroapi.com/api/2619421814940190/{_id}/powerstats'
    response = requests.get(url)
    data = response.json()
    intelligence_list[_id] = data['intelligence']


for character in characters_list:
    search_id(character)


for _id in ids_list.keys():
    search_intelligence(_id)

    
# print(ids_list)
# print(intelligence_list)
print(ids_list[max(intelligence_list)])

