import functions


#functions.get_user_games()
owned_games_list = functions.stored_games("../xml_files/stored_games.xml")
print(owned_games_list)