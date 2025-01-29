import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.python_code.functions import *


class FormInputState(rx.State):
    username: str
    owned_names_list : list

    # @rx.event
    # def initialize_page(self):
    #     self.format_username()
    #     self.generate_list()

    @rx.event
    # def format_username(self):
    #     # path = "BGG_project\\txt_files\\username.txt"
    #     # with open(path, 'r') as file:
    #     #     username = file.read()
    #     username = get_username()
    #     self.username = username
    #     #print("username")
    #     #print(self.username)

    @rx.event
    def generate_data(self):
        username = get_username()
        self.username = username
        # owned_names_list = []
        print("OTRO OWNED_NAMES_LIST")
        print(OWNED_NAMES_LIST)

        for game in OWNED_NAMES_LIST:
            self.owned_names_list.append(game[1])

        print("self owned_names_list")
        print(self.owned_names_list)


def iter_generated_list(owned_names_list):
    return rx.list(owned_names_list)

    # owned_names_list = []
    # path = "BGG_project\\txt_files\\owned_names_list.txt"
    # with open(path, "r") as file:
    #     text = file.read()
    #     if text:
    #         text = text.rstrip(text[-1])
    #         owned_names_list = text.split(",")


@rx.page(route="/owned_games", title="Owned games", on_load=FormInputState.generate_data)
def stored_games() -> rx.Component:  
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                    rx.text(
                        #"AAA",
                        f"User  '{FormInputState.username}' ",
                        # "User  " + "'" + get_username() + "'"),
                        # "User  " + "'" + USER[user.username] + "'",
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
                    # (FormInputState.generate_list()),
                    # rx.list.ordered(
                    #     [rx.list.item(game) for game in FormInputState.owned_names_list],
                    #     padding_top=Size.DEFAULT.value,
                    # ),
                    rx.foreach(FormInputState.owned_names_list, iter_generated_list),
            align="center",
            justify="center",        
            ),
        ),
        footer(),
    ) 