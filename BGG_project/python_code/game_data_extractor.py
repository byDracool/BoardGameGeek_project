from xml.etree import ElementTree
import re
from BGG_project.python_code import boardgame


def game_data_extractor():

    designers  = []
    artists  = []
    publishers  = []

    #Find elements and extract values
    def xml_finder(element):
        return value.find(element).attrib.get('value')

    with open("game_info.xml", 'rt', encoding='utf-8') as game_file:
        tree = ElementTree.parse(game_file)
        #print(tree)
    
    for value in tree.iter('item'):
        #Image
        image_small = value.find("thumbnail").text
        image = value.find("image").text
        #Description
        description = value.find("description").text
        description = re.sub(r'&#10;', '', description)
        #Year published
        year_published = xml_finder("yearpublished")
        #Min/max players
        min_players = xml_finder("minplayers")
        max_players = xml_finder("maxplayers")
        #Min/max playtime
        min_playtime = xml_finder("minplaytime")
        max_playtime = xml_finder("maxplaytime")
        #Min age
        min_age = xml_finder("minage")

        for element in value:
            #Game name
            if element.attrib.get('type') =="primary":
                game_name = element.attrib.get('value')
            #Boardgame designer, artist and publisher (can be more than 1)
            elif element.attrib.get('type') == "boardgamedesigner":
                boardgame_designer = element.attrib.get('value')
                designers.append(boardgame_designer)
            elif element.attrib.get('type') == "boardgameartist":
                boardgame_artist = element.attrib.get('value')
                artists.append(boardgame_artist)
            elif element.attrib.get('type') == "boardgamepublisher":
                boardgame_publisher = element.attrib.get('value')
                publishers.append(boardgame_publisher)

    #print(image_small)
    #print(image)
    #print(description)
    #print(year_published)
    #print(min_players)
    #print(max_players)
    #print(min_playtime)
    #print(max_playtime)
    #print(min_age)
    #print(game_name)
    #print(designers)
    #print(artists)
    #print(publishers)

    # Create an object (game) with all extracted parameters
    game = boardgame.Boardgame(game_name, image, image_small, description, year_published, min_players, max_players, min_playtime, max_playtime, min_age, designers, artists, publishers)
    
    return game


