import requests
from xml.etree import ElementTree
import json
#from user import User
#from BGG_project.python_code.game_data_extractor import game_data_extractor as extractor

#Vars
USER = []
USERNAME = ""
SEARCH_OWNED_GAMES = []
OWNED_NAMES_LIST = []


class User:
    boardgame_library = []

    def __init__(self, username):
        self.username = username

    def add_game_to_boardgame_library(self, game: object):
        self.boardgame_library.append(game)

# Ask user for a game
# def get_user_game():
#     user_game = input("Qué juego desea buscar?: ")
#     return user_game


def get_username():
    str_username = ""
    for value in USER:
        # print(value.username)
        str_username = value.username
    global USERNAME
    USERNAME = str_username
    return str_username


def create_user(username: str):
    user = User(username)
    global USER
    USER.append(user)
    # for value in USER:
    #     print(value.username)


def get_global_var(var_name):
    if var_name == "OWNED_NAMES_LIST":
        return OWNED_NAMES_LIST
    elif var_name == "SEARCH_OWNED_GAMES":
        return SEARCH_OWNED_GAMES
    elif var_name == "USERNAME":
        return USERNAME
    elif var_name == "USER":
        return USER


# Reformat game name using user text
def game_name_reformat(user_text):
    user_text = str(user_text)
    user_text = user_text.lower()
    user_text = user_text.replace(" ", "-")
    return user_text


# Returns a query (str)
def query_text(type_of_query, data):
    query = ""
    data = str(data)
    if type_of_query == "find_games_with_name":
        query = ("https://www.boardgamegeek.com/xmlapi2/search?query=" + data)
    elif type_of_query == "open_url_with_id":
        query = ("https://www.boardgamegeek.com/xmlapi2/thing?id=" + data)
    elif type_of_query == "find_user_games":
        query = ("https://www.boardgamegeek.com/xmlapi2/collection?username=" + data + "&subtype=boardgame&own=1")
    else:
        pass
    return query


# Extracting an XML with the search data
def find_games(user_text):
    game = game_name_reformat(user_text)
    game_name = query_text("find_games_with_name", game)
    # print(game_name)
    search_data = requests.get(game_name)
    # print(search_data.text)
    return search_data


# Creates a txt file with user owned game names
def write_txt_file(txt_name, data):
    path = "BGG_project\\txt_files\\" + txt_name
    file = open(path, "w+")
    if txt_name != "username.txt":
        for value in data:
            file.write(value + ",")
    else:
        for value in data:
            file.write(value)            
    file.close()  


# Open the file and overwrite the data we have extracted
def write_xml_file(xml_name, search_data):
    path = "BGG_project\\xml_files\\" + xml_name
    with open(path, "w+", encoding='utf-8') as game_results:
        game_results.write(search_data.text)
        game_results.close()


def write_json_file(json_name, search_data: dict):
    path = "BGG_project\\json_files\\" + json_name
    with open(path, "w+", encoding='utf-8') as json_file:
        json.dump(search_data, json_file)


# Discard not boardgame/boardgame expansions elements
def finded_games_xml_cleaner(xml_name):
    path = "BGG_project\\xml_files\\" + xml_name

    with open(path, 'rt', encoding='utf-8') as file:
        tree = ElementTree.parse(file)
    # print(tree)

    id_list = []
    boardgame_list = []
    boardgame_validation_list = ["boardgame", "boardgameexpansion"]
    validated_nodes = []


    for node in tree.iter('item'):
        if node.attrib.get('type') not in boardgame_validation_list:
            pass
        else:
            validated_nodes.append(node)
    # print(validated_nodes)

    # Get boargames ids/names
    for element in validated_nodes:
        id = element.attrib.get('id')
        id_list.append(str(id))
        name = element[0].attrib.get('value')
        boardgame_list.append(name)
    # print(id_list)
    # print(boardgame_list)

    # Transform results to dict 
    counter = 0
    find_result_dict = {}

    for data in range(0, len(id_list)):
        find_result_dict[id_list[counter]] = boardgame_list[counter]
        counter += 1

    return find_result_dict


# Print and enumerate games of the dict
def print_games(find_result_dict):
    for index, game in enumerate (find_result_dict):
        print((index + 1), ":",find_result_dict[game])
    

def select_game(find_result_dict):
    game_order = int(input("Seleccione el juego que desea: "))
    for index, game in enumerate (find_result_dict):
        if index == (game_order - 1):
            game_id = game
    return game_id

    
# Obtains game info
def get_game_info_xml(game_id):
    game_page = query_text("open_url_with_id", game_id)
    search_data = requests.get(game_page)
    write_xml_file("game_info.xml", search_data)


# Obtains user games(Its necessary execute it 2 times for working)
def get_user_games(username):
    stored_games = query_text("find_user_games", username)
    search_data = requests.get(stored_games)
    write_xml_file("stored_games.xml", search_data)


# Find stored user games
def stored_games(xml_name):

    path = "BGG_project\\xml_files\\" + xml_name
    with open(path, 'rt', encoding='utf-8') as file:
        tree = ElementTree.parse(file)
    # print(tree)

    stored_boardgame_list = []
    owned_names_list = []

    
    for node in tree.iter('item'):
        stored_boardgame_list.append(node)

    for element in stored_boardgame_list:
        id = element.attrib.get('objectid')
        name = element.find('name').text
        game_list = [id, name]
        owned_names_list.append(game_list)

    global OWNED_NAMES_LIST
    for element in owned_names_list:
        OWNED_NAMES_LIST.append(element)
        #print(element)

    #print("OWNED_NAMES_LIST")
    #print(OWNED_NAMES_LIST)
    #return owned_names_list


def find_games_process(game_name):

    #Reformat game name and write the results into a xml file
    search_data = find_games(game_name)
    write_xml_file("finded_games.xml", search_data)

    #Obtains a dict with the cleaned result of the search {id:game_name, id2:game_name2 ...}
    find_result_dict = finded_games_xml_cleaner("finded_games.xml")
    
    #Transforms dicto into a json file
    write_json_file("find_results.json", find_result_dict)
    


    """#Print and enumerate finded games
    print("\n Estos son los juegos que hemos encontrado con ese nombre...\n")
    print_games(find_result_dict)

    #Ask user for a game of the list
    game_id = select_game(find_result_dict)
    #print(game_id)

    #Gets all game-info of BGG selected boardgame page
    get_game_info_xml(game_id)

    #Extracts an object with data from game_info_xml
    game = extractor.game_data_extractor()"""
    
    """
    print(game.image_small)
    print(game.image)
    print(game.description)
    print(game.year_published)
    print(game.min_players)
    print(game.max_players)
    print(game.min_playtime)
    print(game.max_playtime)
    print(game.min_age)
    print(game.game_name)
    print(game.designers)
    print(game.artists)
    print(game.publishers)"""