from django.shortcuts import render
from .services import get_episodes_list, get_episode, get_character, get_location, get_character_name, get_episode_name, get_character_id, get_episode_id, get_location_id, get_episodes_list_filter, get_characters_list_filter, get_locations_list_filter

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
         characters.append({'name' : get_character_name(character_url), 'id' : get_character_id(character_url)})

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
         episodes.append({'name' : get_episode_name(episode_url), 'id' : get_episode_id(episode_url)})

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

    location = get_location(id)
    residents = []

    for resident_url in location['residents']:
         residents.append({'name' : get_character_name(resident_url), 'id' : get_character_id(resident_url)})

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
