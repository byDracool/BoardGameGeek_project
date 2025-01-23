import requests
from xml.etree import ElementTree


# Ask user for a game
def get_user_game():
    user_game = input("Qué juego desea buscar?: ")
    return user_game


# Ask for a username
def get_username():
    username = input("Escriba el nombre de usuario: ")
    return username


# Reformat game name using user text
def game_name_reformat(user_text):
    user_text = user_text.lower()
    user_text = user_text.replace(" ", "-")
    return user_text


# Returns a query (str)
def query_text(type_of_query, data):
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

# Open the file and overwrite the data we have extracted
def write_xml_file(xml_name, search_data):
    with open(xml_name, "w+", encoding='utf-8') as game_results:
        game_results.write(search_data.text)
        game_results.close()

# Discard not boardgame/boardgame explansions elements
def finded_games_xml_cleaner(xml_name):

    with open(xml_name, 'rt', encoding='utf-8') as file:
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

    print(find_result_dict.items())
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
    #username = get_username()
    stored_games = query_text("find_user_games", username)
    search_data = requests.get(stored_games)
    write_xml_file("../xml_files/stored_games.xml", search_data)
    search_data = requests.get(stored_games)
    write_xml_file("../xml_files/stored_games.xml", search_data)


# Find stored user games
def stored_games(xml_name):

    with open(xml_name, 'rt', encoding='utf-8') as file:
        tree = ElementTree.parse(file)
    # print(tree)

    stored_boardgame_list = []
    owned_names_list = []

    
    for node in tree.iter('item'):
        stored_boardgame_list.append(node)

    for element in stored_boardgame_list:
        name = element.find('name').text
        owned_names_list.append(name)

    return owned_names_list

