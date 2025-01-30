import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.python_code.functions import *


# class FormInputState(rx.State):
#     finded_games_list: list[list[str]]
#
#     @rx.event
#     def generate_data(self):
#         self.finded_games_list = []
#         # print(self.finded_games_list)
#         with open("BGG_project\\json_files\\find_results.json", 'r') as file:
#             data = json.load(file)
#             for value in data:
#                 game = [str(value), str(data[value])]
#                 game[0] = 'https://boardgamegeek.com/boardgame/' + str(game[0])
#                 # print(game)
#                 self.finded_games_list.append(game)
#             # print(self.finded_games_list)
#
#
# def render_link(link_data: rx.Var):
#     """Render a single link item."""
#     return rx.list(
#         rx.link(
#             link_data[1],  # Text
#             href=link_data[0], # URL
#             is_external=True,
#         )
#     )





@rx.page(route="/game", title="Game")#, on_load=FormInputState.generate_data)
def print_game() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                    rx.text(
                        "GAME INFO",
                        align="center",
                        justify="center",
                        size="5",
                        spacing=Size.DEFAULT.value,
                        style=styles.header_style
                    ),
                    rx.center(
                        rx.text(
                            "GAME COMPONENTS: ",
                            "image_small",
                            "image",
                            "description",
                            "year_published",
                            "min_players",
                            "max_players",
                            "min_playtime",
                            "max_playtime",
                            "min_age",
                            "game_name",
                            "designers",
                            "artists",
                            "publishers",
                            align="center",
                            justify="center",
                            size="5",
                            spacing=Size.DEFAULT.value,
                            style=styles.header_style
                        ),
                        # rx.list(
                        #     # rx.foreach(FormInputState.finded_games_list),
                        #     #[rx.list.item(game) for game in (show_find_results())],
                        #     rx.foreach(FormInputState.finded_games_list, render_link),
                        #     #[rx.list.item(game) for game in FormInputState.finded_games_list],
                        #     padding_top=Size.DEFAULT.value,
                        # ),
                    ),
            align="center",
            justify="center",
            ),
        ),
        footer(),
    )