import functions
import game_data_extractor as extractor



if __name__ == "__main__":
    #Ask user for a game and write results into a xml file
    user_game = functions.get_user_game()
    search_data = functions.find_games(user_game)
    functions.write_xml_file("finded_games.xml", search_data)

    #Obtains a dict with the cleaned result of the search {id:game_name, id2:game_name2 ...}
    find_result_dict = functions.finded_games_xml_cleaner("finded_games.xml")

    #Print and enumerate finded games
    print("\n Estos son los juegos que hemos encontrado con ese nombre...\n")
    functions.print_games(find_result_dict)

    #Ask user for a game of the list
    game_id = functions.select_game(find_result_dict)
    #print(game_id)

    #Gets all game-info of BGG selected boardgame page
    functions.get_game_info_xml(game_id)

    #Extracts an object with data from game_info_xml
    game = extractor.game_data_extractor()
    
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
    print(game.publishers)
