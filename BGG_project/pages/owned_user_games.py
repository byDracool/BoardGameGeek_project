import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.python_code.constants import GAME_PRINTER
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.python_code.functions import *

# GAME = []


class FormInputState(rx.State):
    username: str
    #owned_names_list : list
    #owned_id_list: list
    owned_full_list: list[list[str, str]]
    total: int

    @rx.event
    def generate_data(self):
        username = get_username()
        self.username = username
        imported_owned_names_list = get_global_var("OWNED_NAMES_LIST")

        # print(imported_owned_names_list)

        self.owned_full_list = imported_owned_names_list
        self.total = len(imported_owned_names_list)

        imported_owned_names_list = []


class State(rx.State):

    @rx.event
    def change_page(self, game_id):
        # print(game_id)
        game = send_game_id_to_extract_info(game_id)
        # global GAME
        # try:
        #     GAME.pop()
        # except:
        #     pass
        write_game_var(game)
        # GAME.append(game)
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


def write_game_var(game):
    get_global_var("GAME")
    # print(GAME)
    empty_variable("GAME")
    GAME.append(game)
    # print(GAME)
    # for game in GAME:
    #     print(game.game_name)


@rx.page(route="/owned_games", title="Owned games", on_load=FormInputState.generate_data)
def stored_games() -> rx.Component:  
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading(
                    f"User  '{FormInputState.username}' ",
                    align="center",
                    justify="center",
                    size="7",
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
                rx.spacer(),
                # rx.text(
                #     f"(Total encountered: {FormInputState.total})",
                #     size="4",
                #     padding_top=Size.EXTRA_SMALL.value,
                #     spacing=Size.DEFAULT.value,
                #     style=styles.header_style,
                #     align="center",
                #     justify="center",
                # ),
                rx.cond(
                    (FormInputState.total != 0),
                    rx.text(
                        f"(Total encountered: {FormInputState.total})",
                        size="4",
                        padding_top=Size.EXTRA_SMALL.value,
                        spacing=Size.DEFAULT.value,
                        style=styles.header_style,
                        align = "center",
                        justify = "center",
                    ),
                    rx.text(
                        f"(Incorrect username or no games encountered)",
                        size="4",
                        color_scheme="red",
                        padding_top=Size.EXTRA_SMALL.value,
                        spacing=Size.DEFAULT.value,
                        align = "center",
                        justify = "center",
                    ),
                ),
                rx.spacer(),
                # (FormInputState.generate_list()),
                # rx.list.ordered(
                #     [rx.list.item(game) for game in FormInputState.owned_names_list],
                #     padding_top=Size.DEFAULT.value,
                # ),
                # rx.foreach(FormInputState.owned_names_list, iter_generated_name_list),
                # rx.foreach(FormInputState.owned_id_list, iter_generated_id_list),
                rx.foreach(FormInputState.owned_full_list, render_link),
                align="center",
                justify="center",
            ),
        ),
        footer(),
    ) 