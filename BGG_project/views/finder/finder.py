import reflex as rx
# from BGG_project.python_code.user import User
from BGG_project.styles.styles import Size as Size
from BGG_project.components.find_icons import find_icon, find_user
# from BGG_project.styles.colors import TextColor as TextColor
# from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles
from BGG_project.python_code.constants import OWNED_GAMES_PAGE
from BGG_project.python_code.functions import *

class FormInputState(rx.State):
    input_username: str
    owned_names_list : list
    game_name: str #dict = {}


    @rx.event
    def handle_username(self, username: dict):
        self.input_username = username["input"]
        #print(self.input_username)
        create_user(self.input_username)
        # user = User(username["input"])
        #
        # global USERNAME
        # USERNAME.append("byDracool")
        # #print(USERNAME.items)
        # #print(USERNAME["input"])
        # for user in USERNAME:
        #      print(user.username)
        # print(USERNAME[0].username)


    @rx.event
    def handle_game_name(self, game_name: dict):
        self.game_name = game_name["input"]


    # @rx.event
    # def change_page_owned_games(self):
    #     return rx.redirect(
    #         OWNED_GAMES_PAGE,
    #         is_external=True,
    #     )


    def get_stored_games(self):
        #for value in USER:
            #print(value.username)
        get_user_games(self.input_username)
        stored_games("stored_games.xml")

        #prueba_lista = OWNED_NAMES_LIST[0].items()
        # for game in OWNED_NAMES_LIST.items:
        #     OWNED_NAMES_LIST.append(game)

        #write_txt_file("owned_names_list.txt", prueba_lista)
        #
        #FormInputState.change_page_owned_games()


    def find_games(self):
        find_games_process(self.game_name)


def game_input():
    return rx.vstack(
            rx.form.root(
                rx.vstack(
                    rx.input(
                        name="input",
                        placeholder="Enter game name...",
                        type="text",
                        required=True,
                        align="center",
                        justify="center",
                        margin_top=Size.SMALL.value
                    ),
                    find_icon(),
                    #rx.button("Submit", type="submit"),
                    width="100%",
                    align="center",
                    justify="center",
                ),
                #on_submit=Username(),
                on_submit=FormInputState.handle_game_name,
                #on_click=FormInputState.find_games(),
                reset_on_submit=True,
                align="center",
                justify="center",
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.text(
                    FormInputState.game_name
                ),
            #    rx.text(
            #        FormInputState.owned_names_list
            #    ),
            ),
            align="center",
            justify="center",
            width="100%",
            )


def username_input():
    return rx.vstack(
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="input",
                        placeholder="Enter username...",
                        type="text",
                        required=True,
                        align="center",
                        justify="center",
                        margin_top=Size.SMALL.value
                    ),
                    find_user(),
                    #rx.button("Submit", type="submit"),
                    width="100%",
                    align="center",
                    justify="center",
                ),
                #on_submit=Username(),
                on_submit=FormInputState.handle_username(),
                on_click=FormInputState.get_stored_games(),
                #on_click=rx.redirect(
                #            "http://localhost:3000/owned_games/",
                #            is_external=True,
                #        ),
                reset_on_submit=True,
                align="center",
                justify="center",
                width="100%",
            ),
            #rx.divider(),
            #rx.hstack(
            #    rx.heading("Results:"),
            #     rx.text(
            #         FormInputState.input_username
            #     ),
            #    rx.text(
            #        FormInputState.owned_names_list
            #    ),
            #),
            align="center",
            justify="center",
            width="100%",
            )


def finder() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Write the game name you are looking for:",
                    align="center",
                    size="5",
                    padding_top=Size.DEFAULT.value,
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style
                ),
                game_input(),
                rx.spacer(),
                rx.text(
                    "Looking for your BGG stored games?",
                    align="center",
                    size="5",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                    padding_top=Size.DEFAULT.value
                ),
                rx.spacer(),
                username_input(),
                align="center",
                justify="center",
                padding_top=Size.DEFAULT.value,                    
        )