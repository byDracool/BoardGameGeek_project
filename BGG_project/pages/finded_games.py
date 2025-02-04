import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.python_code.constants import GAME_PRINTER
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.python_code.functions import *

GAME = []


class FormInputState(rx.State):
    finded_games_list: list[list[str]]

    @rx.event
    def generate_data(self):

        ##### Old method #####
        # self.finded_games_list = []
        # # print(self.finded_games_list)
        # with open("BGG_project\\json_files\\find_results.json", 'r') as file:
        #     data = json.load(file)
        #     for value in data:
        #         game = [str(value), str(data[value])]
        #         game[0] = 'https://boardgamegeek.com/boardgame/' + str(game[0])
        #         # print(game)
        #         self.finded_games_list.append(game)
        #     # print(self.finded_games_list)

        ##### New method (without saving local data) #####

        self.finded_games_list = []
        # print(self.finded_games_list)
        #print(FIND_RESULTS_DICT)


        for value in FIND_RESULTS_DICT:
            game = [str(value), str(FIND_RESULTS_DICT[value])] # [id, game name])
            self.finded_games_list.append(game)

        # print(self.finded_games_list)


class State(rx.State):

    @rx.event
    def change_page(self, game_id):
        # print(game_id)
        game = send_game_id_to_extract_info(game_id)
        global GAME
        try:
            GAME.pop()
        except:
            pass
        GAME.append(game)
        # print(GAME)
        return rx.redirect(
            GAME_PRINTER,
            # is_external=True,
        )


def render_link(link_data: rx.Var):
    """Render a single link item."""
    return rx.list(
        rx.link(
            link_data[1],  # Text
            # href=link_data[0], # Game id
            on_click= State.change_page(link_data[0]),
            is_external=False,
        ),
    )


# def render_link(link_data: rx.Var):
#     """Render a single link item."""
#     return rx.list(
#         rx.link(
#             link_data[1],  # Text
#             href=link_data[0], # URL
#             is_external=True,
#         ),
#     )


@rx.page(route="/finded_games", title="Finded_games", on_load=FormInputState.generate_data)
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
                            rx.foreach(FormInputState.finded_games_list, render_link),
                            padding_top=Size.DEFAULT.value,
                        ),
                    ), 
            align="center",
            justify="center",        
            ),
        ),
        footer(),
    ) 