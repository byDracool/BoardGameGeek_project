import functions

#functions.get_user_games()
#owned_games_list = functions.stored_games("../xml_files/stored_games.xml")
#print(owned_games_list)

dict = {"13":"CATAN","278":"Catan Card Game","306":"Die Siedler von Catan: Historische Szenarien","325":"CATAN: Seafarers",
        "926":"CATAN: Cities & Knights","1137":"Die Siedler von Catan: Das Buch zum Spielen"}

def text_to_list_formatter(txt_name):
    owned_names_list = []
    path = "..\\txt_files\\" + txt_name
    with open(path, 'r') as file:
        lines = [line.split(",") for line in file]

    for line in lines:
        owned_names_list.append(line)
    return owned_names_list


"""lista_prueba = ['1911 Amundsen vs Scott', '5-Minute Dungeon', '5-Minute Dungeon: Curses! Foiled Again!', '7 Wonders Duel', '7 Wonders Duel: Pantheon', 
                'Aftermath', 'Agricola', 'Amun-Re', 'Ankh: Gods of Egypt', 'Ankh: Gods of Egypt - Guardians Set', 'Ankh: Gods of Egypt - Pantheon', 
                'Ankh: Gods of Egypt - Pharaoh', 'Ankh: Gods of Egypt - Tomb of Wonders', 'Architects of the West Kingdom', 'Asante', 'Ascension: Realms Unraveled', 
                'Azul', 'Azul: Stained Glass of Sintra', 'Bandido', 'Barony', 'Bears vs Babies']"""

#texto = "1911 Amundsen vs Scott,5-Minute Dungeon,5-Minute Dungeon: Curses! Foiled Again!,7 Wonders Duel,7 Wonders Duel: Pantheon,Aftermath,Agricola"
#owned_names_list = text_to_list_formatter("owned_names_list.txt")
#print(owned_names_list)
#texto = list(texto)
#nuevo_texto = texto.split()
#print(nuevo_texto)

lista = []

for value in dict:
    print(value)
    print(dict[value])
    lista.append(value + " : " + dict[value])

print(lista)