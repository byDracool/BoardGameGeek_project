import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.python_code.functions import *

FINDED_GAMES_LIST = []


def show_find_results():
    with open("BGG_project\\json_files\\find_results.json", 'r') as file:
        data = json.load(file)
        [FINDED_GAMES_LIST.append((value) + " : " + data[value]) for value in data]
        #[(f"{value} : {data[value]}") for value in data]
        return FINDED_GAMES_LIST


@rx.page(route="/finded_games", title="Finded_games")
def finded_games() -> rx.Component:  
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                    rx.text(
                        "These are the games we have found with that name...",
                        align="center",
                        justify="center",
                        size="5",
                        spacing=Size.DEFAULT.value,
                        style=styles.header_style
                    ),
                    rx.center(
                        rx.list(
                            [rx.list.item(game) for game in (show_find_results())],
                            padding_top=Size.DEFAULT.value,
                        ),
                    ), 
            align="center",
            justify="center",        
            ),
        ),
        footer(),
    ) 