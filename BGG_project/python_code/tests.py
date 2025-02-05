from BGG_project.python_code.game_data_extractor import game_data_extractor
import json
from BGG_project.python_code.functions import *
import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, fromstring




# url_xml = 'https://boardgamegeek.com/xmlapi2/thing?id=199792.xml'
# url_xml = 'https://boardgamegeek.com/xmlapi2/search?query=dominion'
#
# search_data = requests.get(url_xml)
# # print(search_data)
# info = search_data.text
# # print(search_data.text)
# # print(type(info))
#
# # games_search_data = urlopen(stored_games)
# # root = ET.fromstring(info)
# # tree = parse(root)
# tree = ET.fromstring(info)
# print(tree)






# url_xml = 'https://boardgamegeek.com/xmlapi2/thing?id=199792.xml'
# id = "199792"
# # send_game_id_to_extract_info(id)
# # game = game_data_extractor(url_xml)
#
# print(GAME)
# for game in GAME:
#     print(game.game_name)

# print(game.game_name)
# print(game.image_small)
# print(game.image)
# print(game.description)
# print(game.year_published)
# print(game.min_players)
# print(game.max_players)
# print(game.min_playtime)
# print(game.max_playtime)
# print(game.min_age)
# print(game.game_name)
# print(game.designers)
# print(game.artists)
# print(game.publishers)

# from urllib.request import urlopen
# from xml.etree.ElementTree import parse
# import re
#
#
# def xml_finder(game_element):
#     return value.find(game_element).attrib.get('value')
#
#
# designers  = []
# artists  = []
# publishers  = []
#
# url = 'https://boardgamegeek.com/xmlapi2/thing?id=199792.xml'
# search_data = urlopen(url)
# tree = parse(search_data)
#
# print(tree)
#
#
# for value in tree.iter('item'):
#     # Image
#     image_small = value.find("thumbnail").text
#     image = value.find("image").text
#     # Description
#     description = value.find("description").text
#     description = re.sub(r'&#10;', '', description)
#     # Year published
#     year_published = xml_finder("yearpublished")
#     # Min/max players
#     min_players = xml_finder("minplayers")
#     max_players = xml_finder("maxplayers")
#     # Min/max playtime
#     min_playtime = xml_finder("minplaytime")
#     max_playtime = xml_finder("maxplaytime")
#     # Min age
#     min_age = xml_finder("minage")
#
#     for element in value:
#         # Game name
#         if element.attrib.get('type') == "primary":
#             game_name = element.attrib.get('value')
#         # Boardgame designer, artist and publisher (can be more than 1)
#         elif element.attrib.get('type') == "boardgamedesigner":
#             boardgame_designer = element.attrib.get('value')
#             designers.append(boardgame_designer)
#         elif element.attrib.get('type') == "boardgameartist":
#             boardgame_artist = element.attrib.get('value')
#             artists.append(boardgame_artist)
#         elif element.attrib.get('type') == "boardgamepublisher":
#             boardgame_publisher = element.attrib.get('value')
#             publishers.append(boardgame_publisher)
#
# print(image_small)
# print(image)
# print(description)
# print(year_published)
# print(min_players)
# print(max_players)
# print(min_playtime)
# print(max_playtime)
# print(min_age)
# print(game_name)
# print(designers)
# print(artists)
# print(publishers)


# Find elements and extract values
# def xml_finder(game_element):
#     return value.find(game_element).attrib.get('value')
#
#
# url_xml = 'https://boardgamegeek.com/xmlapi2/thing?id=199792.xml'
# search_data = urlopen(url_xml)
# tree = parse(search_data)
#
#
# for value in tree.iter('item'):
#     # Id
#     print(value)
#     game_id = value.attrib.get('id')
#     print(game_id)


def write_game_var(game):
    get_global_var("GAME")
    print(GAME)
    empty_variable("GAME")
    GAME.append(game)
    print(GAME)


write_game_var("mi_juego")
get_global_var("GAME")
for game in GAME:
    print(game)