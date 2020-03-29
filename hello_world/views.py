from django.shortcuts import render
from .services import get_episodes_list, get_episode, get_character, get_location, get_character_with_url, get_episode_with_url, get_location_id, get_episodes_list_filter, get_characters_list_filter, get_locations_list_filter, get_multiple_character

def hello_world(request):
    episodes_list = get_episodes_list()
    episodes = episodes_list

    for ep in episodes:
        ep = {
            'episode' : ep['episode'],
            'name' : ep['name'],
            'air_date' : ep['air_date'],
            'id' : ep['id'],
        }

    context = {'episodes_info' : episodes}

    return render(request, 'hello_world.html', context)


def show_episode(request):
    id = request.GET.get('id', '')

    episode = get_episode(id)
    characters = []

    for character_url in episode['characters']:
         character = get_character_with_url(character_url)
         characters.append({'name' : character['name'], 'id' : character['id']})

    episode_info = {
        'episode_number' : episode['episode'],
        'name' : episode['name'],
        'air_date' : episode['air_date'],
        'code' : episode['id'],
        'characters' : characters,
    }

    context = {'episode_info' : episode_info}
    return render(request, 'episode.html', context)


def show_character(request):
    id = request.GET.get('id', '')

    character = get_character(id)
    episodes = []

    for episode_url in character['episode']:
         episode = get_episode_with_url(episode_url)
         episodes.append({'name' : episode['name'], 'id' : episode['id']})

    if character['origin']['name'] != 'unknown':
        origin = {'name' : character['origin']['name'], 'id' : get_location_id(character['origin']['url'])}
    else:
        origin = {'name' : character['origin']['name'], 'id' : -1}

    if character['location']['name'] != 'unknown':
        location = {'name' : character['location']['name'], 'id' : get_location_id(character['location']['url'])}
    else:
        location = {'name' : character['location']['name'], 'id' : -1}

    character_info = {
        'name' : character['name'],
        'status' : character['status'],
        'species' : character['species'],
        'type' : character['type'],
        'gender' : character['gender'],
        'origin' : origin,
        'location' : location,
        'image' : character['image'],
        'episodes' : episodes,
    }

    context = {'character_info' : character_info}
    return render(request, 'character.html', context)



def show_location(request):
    id = request.GET.get('id', '')
    cuantas_req = 1
    location = get_location(id)
    residents = []

    resident_ids = ""
    for resident_url in location['residents']:
         resident_ids += resident_url.split("/")[-1]+","
         # character = get_character_with_url(resident_url)
         # residents.append({'name' : character['name'], 'id' : character['id']})
         # cuantas_req += 1

    if len(resident_ids) > 0:
        residents_total = get_multiple_character(resident_ids[:-1])
        for res in residents_total:
            residents.append({'name' : res['name'], 'id' : res['id']})

    location_info = {
        'name' : location['name'],
        'type' : location['type'],
        'dimension' : location['dimension'],
        'residents' : residents,
    }

    context = {'location_info' : location_info}
    return render(request, 'location.html', context)

def show_search(request):
    words = request.GET.get('words', '')

    episodes = get_episodes_list_filter(words)
    characters = get_characters_list_filter(words)
    locations = get_locations_list_filter(words)

    for ep in episodes:
        ep = {
            'episode' : ep['episode'],
            'name' : ep['name'],
            'air_date' : ep['air_date'],
            'id' : ep['id'],
        }

    for char in episodes:
        char = {
            'name' : char['name'],
            'id' : char['id'],
        }

    for loc in locations:
        loc = {
            'name' : loc['name'],
            'id' : loc['id'],
        }

    context = {'words' : words, 'episodes_info' : episodes, 'characters_info' : characters, 'locations_info' : locations}

    return render(request, 'search.html', context)
