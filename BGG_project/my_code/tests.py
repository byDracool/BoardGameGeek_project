from xml.etree import ElementTree
import re


with open("game_info.xml", 'rt', encoding='utf-8') as game_file:
    tree = ElementTree.parse(game_file)
    #print(tree)

#Image
for value in tree.iter('item'):
    image_small = value.find("thumbnail").text
    image = value.find("image").text

print(image_small)
print(image)


#Name
for value in tree.iter('item'):
    for name in value:
        if name.attrib.get('type') =="primary":
            game_name = name.attrib.get('value')

print(game_name)

#Description
for value in tree.iter('item'):
    description = value.find("description").text
    description = re.sub(r'&#10;', '', description)

print(description)

#Year published
for value in tree.iter('item'):
    year_published = value.find("yearpublished")
    year_published = year_published.attrib.get('value')

print(year_published)

#Min/max players
for value in tree.iter('item'):
    min_players = value.find("minplayers").attrib.get('value')
    max_players = value.find("maxplayers").attrib.get('value')

print(min_players)
print(max_players)

#Min/max playtime
for value in tree.iter('item'):
    min_playtime = value.find("minplaytime").attrib.get('value')
    max_playtime = value.find("maxplaytime").attrib.get('value')

print(min_playtime)
print(max_playtime)

#Min age
for value in tree.iter('item'):
    min_age = value.find("minage").attrib.get('value')

print(min_age)

#Boardgame designer (can be more than 1)
designers  = []
for value in tree.iter('item'):
    for link in value:
        if link.attrib.get('type') == "boardgamedesigner":
            boardgame_designer = link.attrib.get('value')
            designers.append(boardgame_designer)

print(designers)

#Boardgame artist (can be more than 1)
artists  = []
for value in tree.iter('item'):
    for link in value:
        if link.attrib.get('type') == "boardgameartist":
            boardgame_artist = link.attrib.get('value')
            artists.append(boardgame_artist)

print(artists)

#Boardgame publisher (can be more than 1)
publishers  = []
for value in tree.iter('item'):
    for link in value:
        if link.attrib.get('type') == "boardgamepublisher":
            boardgame_publisher = link.attrib.get('value')
            publishers.append(boardgame_publisher)

print(publishers)
