import requests

# Mucho basado en https://www.digitalocean.com/community/tutorials/how-to-display-data-from-the-digitalocean-api-with-django

# Create your views here.

def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/"+str(id)
    r = requests.get(url)
    episode = r.json()
    return episode

def get_episodes_list():
    url = "https://rickandmortyapi.com/api/episode"
    r = requests.get(url, headers={})
    episodes = r.json()
    episodes_list = []
    num_pages = episodes['info']['pages']
    pages = []
    counter = 1
    while counter <= num_pages:
        url = "https://rickandmortyapi.com/api/episode?page="+str(counter)
        r = requests.get(url, headers={})
        episodes_page = r.json()['results']
        for episode in episodes_page:
            episodes_list.append(episode)
        counter += 1
    return episodes_list


def get_episodes_list_filter(words):
    # Filter by name
    url = "https://rickandmortyapi.com/api/episode/?name="+words
    r = requests.get(url, headers={})
    episodes = r.json()
    episodes_list = []
    if 'error' not in episodes.keys():
        num_pages = episodes['info']['pages']
        pages = []
        counter = 1
        while counter <= num_pages:
            url = "https://rickandmortyapi.com/api/episode?page="+str(counter)+"&name="+words
            r = requests.get(url, headers={})
            episodes_page = r.json()['results']
            for episode in episodes_page:
                if episode not in episodes_list:
                    episodes_list.append(episode)
            counter += 1

    # # Filter by episode
    # url = "https://rickandmortyapi.com/api/episode/?episode="+words
    # r = requests.get(url, headers={})
    # episodes = r.json()
    # if 'error' not in episodes.keys():
    #     num_pages = episodes['info']['pages']
    #     pages = []
    #     counter = 1
    #     while counter <= num_pages:
    #         url = "https://rickandmortyapi.com/api/episode?page="+str(counter)+"&episode="+words
    #         r = requests.get(url, headers={})
    #         episodes_page = r.json()['results']
    #         for episode in episodes_page:
    #             if episode not in episodes_list:
    #                 episodes_list.append(episode)
    #         counter += 1
    return episodes_list


def get_characters_list_filter(words):
    # Filter by name
    url = "https://rickandmortyapi.com/api/character/?name="+words
    r = requests.get(url, headers={})
    characters = r.json()
    characters_list = []
    if 'error' not in characters.keys():
        num_pages = characters['info']['pages']
        pages = []
        counter = 1
        while counter <= num_pages:
            url = "https://rickandmortyapi.com/api/character?page="+str(counter)+"&name="+words
            r = requests.get(url, headers={})
            characters_page = r.json()['results']
            for character in characters_page:
                if character not in characters_list:
                    characters_list.append(character)
            counter += 1

    # # Filter by status
    # url = "https://rickandmortyapi.com/api/character/?status="+words
    # r = requests.get(url, headers={})
    # characters = r.json()
    # if 'error' not in characters.keys():
    #     num_pages = characters['info']['pages']
    #     pages = []
    #     counter = 1
    #     while counter <= num_pages:
    #         url = "https://rickandmortyapi.com/api/character?page="+str(counter)+"&status="+words
    #         r = requests.get(url, headers={})
    #         characters_page = r.json()['results']
    #         for character in characters_page:
    #             if character not in characters_list:
    #                 characters_list.append(character)
    #         counter += 1
    #
    # # Filter by species
    # url = "https://rickandmortyapi.com/api/character/?species="+words
    # r = requests.get(url, headers={})
    # characters = r.json()
    # if 'error' not in characters.keys():
    #     num_pages = characters['info']['pages']
    #     pages = []
    #     counter = 1
    #     while counter <= num_pages:
    #         url = "https://rickandmortyapi.com/api/character?page="+str(counter)+"&species="+words
    #         r = requests.get(url, headers={})
    #         characters_page = r.json()['results']
    #         for character in characters_page:
    #             if character not in characters_list:
    #                 characters_list.append(character)
    #         counter += 1
    #
    # # Filter by type
    # url = "https://rickandmortyapi.com/api/character/?type="+words
    # r = requests.get(url, headers={})
    # characters = r.json()
    # if 'error' not in characters.keys():
    #     num_pages = characters['info']['pages']
    #     pages = []
    #     counter = 1
    #     while counter <= num_pages:
    #         url = "https://rickandmortyapi.com/api/character?page="+str(counter)+"&type="+words
    #         r = requests.get(url, headers={})
    #         characters_page = r.json()['results']
    #         for character in characters_page:
    #             if character not in characters_list:
    #                 characters_list.append(character)
    #         counter += 1
    #
    # # Filter by gender
    # url = "https://rickandmortyapi.com/api/character/?gender="+words
    # r = requests.get(url, headers={})
    # characters = r.json()
    # if 'error' not in characters.keys():
    #     num_pages = characters['info']['pages']
    #     pages = []
    #     counter = 1
    #     while counter <= num_pages:
    #         url = "https://rickandmortyapi.com/api/character?page="+str(counter)+"&gender="+words
    #         r = requests.get(url, headers={})
    #         characters_page = r.json()['results']
    #         for character in characters_page:
    #             if character not in characters_list:
    #                 characters_list.append(character)
    #         counter += 1

    return characters_list


def get_locations_list_filter(words):
    # Filter by name
    url = "https://rickandmortyapi.com/api/location/?name="+words
    r = requests.get(url, headers={})
    locations = r.json()
    locations_list = []
    if 'error' not in locations.keys():
        num_pages = locations['info']['pages']
        pages = []
        counter = 1
        while counter <= num_pages:
            url = "https://rickandmortyapi.com/api/location?page="+str(counter)+"&name="+words
            r = requests.get(url, headers={})
            locations_page = r.json()['results']
            for location in locations_page:
                if location not in locations_list:
                    locations_list.append(location)
            counter += 1

    # # Filter by type
    # url = "https://rickandmortyapi.com/api/location/?type="+words
    # r = requests.get(url, headers={})
    # locations = r.json()
    # if 'error' not in locations.keys():
    #     num_pages = locations['info']['pages']
    #     pages = []
    #     counter = 1
    #     while counter <= num_pages:
    #         url = "https://rickandmortyapi.com/api/location?page="+str(counter)+"&type="+words
    #         r = requests.get(url, headers={})
    #         locations_page = r.json()['results']
    #         for location in locations_page:
    #             if location not in locations_list:
    #                 locations_list.append(location)
    #         counter += 1
    #
    # # Filter by dimension
    # url = "https://rickandmortyapi.com/api/location/?dimension="+words
    # r = requests.get(url, headers={})
    # locations = r.json()
    # if 'error' not in locations.keys():
    #     num_pages = locations['info']['pages']
    #     pages = []
    #     counter = 1
    #     while counter <= num_pages:
    #         url = "https://rickandmortyapi.com/api/location?page="+str(counter)+"&dimension="+words
    #         r = requests.get(url, headers={})
    #         locations_page = r.json()['results']
    #         for location in locations_page:
    #             if location not in locations_list:
    #                 locations_list.append(location)
    #         counter += 1

    return locations_list


def get_character_name(url):
    r = requests.get(url, headers={})
    character = r.json()
    return character['name']

def get_character_id(url):
    r = requests.get(url, headers={})
    character = r.json()
    return character['id']

def get_character_with_url(url):
    r = requests.get(url, headers={})
    character = r.json()
    return character

def get_episode_name(url):
    r = requests.get(url, headers={})
    episode = r.json()
    return episode['name']

def get_episode_id(url):
    r = requests.get(url, headers={})
    episode = r.json()
    return episode['id']

def get_character(id):
    url = "https://rickandmortyapi.com/api/character/"+str(id)
    r = requests.get(url)
    character = r.json()
    return character

def get_location(id):
    url = "https://rickandmortyapi.com/api/location/"+str(id)
    r = requests.get(url)
    location = r.json()
    return location

def get_location_id(url):
    r = requests.get(url, headers={})
    location = r.json()
    return location['id']

# (1)
# print("Episodes list")
# for episode in get_episodes_list():
#     print("Nombre: "+episode['name'])
#     print("Fecha: "+episode['air_date'])
#     print("Código: "+str(episode['id']))
#     print("\n")

# (2)
# print("\n")
# print("Episodio: "+get_episode(19)['episode'])
# print("\n")
# print("Nombre: "+get_episode(19)['name'])
# print("\n")
# print("Personajes:")
# for character_url in get_episode(19)['characters']:
#     print(get_character_name(character_url))

# (3)
# id = 35
# print("\n")
# print(get_character(id))
# print("\n")
# print("Nombre: "+get_character(id)['name'])
# print("Estado: "+get_character(id)['status'])
# print("Especie: "+get_character(id)['species'])
# print("Tipo: "+get_character(id)['type'])
# print("Género: "+get_character(id)['gender'])
# print("Origen: "+get_character(id)['origin']['name'])
# print("Ubicación: "+get_character(id)['location']['name'])
# print("Imágen: "+get_character(id)['image'])
# <img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
# print("\n")
# print("Episodios:")
# for episode_url in get_character(id)['episode']:
#     print(get_episode_name(episode_url))

# (4)
# id=3
# print(get_location(id))
# print("\n")
# print("Nombre: "+get_location(id)['name'])
# print("Tipo: "+get_location(id)['type'])
# print("Dimensión: "+get_location(id)['dimension'])
# print("Residentes:")
# for resident_url in get_location(id)['residents']:
#     print(get_character_name(resident_url))
