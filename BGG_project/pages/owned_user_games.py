import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.python_code.functions import *


@rx.event
def username():
    path = "BGG_project\\txt_files\\username.txt"
    with open(path, 'r') as file:
        username = file.read()
    return username

@rx.event
def generate_list():
    owned_names_list = []
    path = "BGG_project\\txt_files\\owned_names_list.txt"
    with open(path, "r") as file:
        text = file.read()
        if text:
            text = text.rstrip(text[-1])
            owned_names_list = text.split(",")
    return owned_names_list


@rx.page(route="/owned_games", title="Owned games")
def stored_games() -> rx.Component:  
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                    rx.text(
                        "User  " + "'" + username() + "'",
                        align="center",
                        justify="center",
                        size="5",
                        spacing=Size.DEFAULT.value,
                        style=styles.header_style
                    ),
                    rx.text(
                        "Games stored in BGG:",
                        
                        size="5",
                        padding_top=Size.EXTRA_SMALL.value,
                        spacing=Size.DEFAULT.value,
                        style=styles.header_style
                    ),
                    rx.list.ordered(
                        [rx.list.item(game) for game in (generate_list())],
                        padding_top=Size.DEFAULT.value,
                    ),
            align="center",
            justify="center",        
            ),
        ),
        footer(),
    ) 