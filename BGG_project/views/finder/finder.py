import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.find_icon import find_icon, find_user
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles
from BGG_project.my_code.functions import *


class Username:

    def __init__(self, username):
        self.username = username

    def get_user_games(self, username):
        get_user_games()


class FormInputState(rx.State):
    username: dict = {}
    owned_names_list : list

    @rx.event
    def handle_username(self, username: str):
        self.username = username

    @rx.event
    def create_owned_names_list(self, owned_names_list: list):
        self.owned_names_list = owned_names_list    


def username_input():
    return rx.vstack(
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="input",
                        placeholder="Enter text...",
                        type="text",
                        required=True,
                    ),
                    find_user(),
                    #rx.button("Submit", type="submit"),
                    width="100%",
                ),
                on_submit=Username(),
                #on_submit=FormInputState.handle_username,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.text(
                    FormInputState.username.to_string()
                ),
            ),
            align_items="left",
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
                rx.text_area(
                    placeholder="Type game here...",
                    spacing=Size.MEDIUM.value,
                    style=styles.finder_style
                ),
                find_icon(),
                rx.hstack(
                #    rx.text(
                #        "Looking for your BGG stored games?",
                #        align="center",
                #        size="5",
                #        spacing=Size.DEFAULT.value,
                #        style=styles.finder_style,
                #    ),
                #    rx.spacer(),
                    #rx.text_area(
                    #    placeholder="Enter your username...",
                    #    spacing=Size.MEDIUM.value,
                    #    style=styles.finder_style,
                    #    size="1",
                    #    justify="center",
                    #),
                #    rx.spacer(),
                #    find_user(),
                #    padding_top=Size.EXTRA_BIG.value,
                #    align="center",
                #    justify="center",
                    ),
                    username_input(),
                    align="center",
                    
        )