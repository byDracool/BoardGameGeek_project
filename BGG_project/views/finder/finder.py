import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.find_icons import find_icon, find_user
import BGG_project.styles.styles as styles
from BGG_project.python_code.functions import *


class FormInputState(rx.State):
    input_username: str
    owned_names_list : list
    game_name: str

    @rx.event
    def handle_username(self, username: dict):
        self.input_username = username["input"]
        #print(self.input_username)
        create_user(self.input_username)

    @rx.event
    def handle_game_name(self, game_name: dict):
        self.game_name = game_name["input"]

    def get_stored_games(self):
        get_user_stored_games(self.input_username)

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
                on_click=FormInputState.find_games(),
                reset_on_submit=True,
                align="center",
                justify="center",
                width="100%",
            ),
            # rx.divider(),
            # rx.hstack(
            #     rx.heading("Results:"),
            #     rx.text(
            #         FormInputState.game_name
            #     ),
            #    rx.text(
            #        FormInputState.owned_names_list
            #    ),
            # ),
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