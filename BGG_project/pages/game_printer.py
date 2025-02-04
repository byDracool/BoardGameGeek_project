import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from .finded_games import GAME
from .owned_user_games import GAME


class FormInputState(rx.State):
    game_name: str
    image: str
    image_small: str
    description: str
    year_published: str
    min_players: str
    max_players: str
    min_playtime: str
    max_playtime: str
    min_age: str
    designers: list
    artists: list
    publishers: list

    def retrieve_game_info(self):
        for game in GAME:
            print(game.game_name)
            self.game_name = game.game_name
            self.image = game.image
            self.image_small = game.image_small
            self.description = game.description
            self.year_published = game.year_published
            self.min_players = game.min_players
            self.max_players = game.max_players
            self.min_playtime = game.min_playtime
            self.max_playtime = game.max_playtime
            self.min_age = game.min_age
            self.designers = game.designers
            self.artists = game.artists
            self.publishers = game.publishers


def render_link(link_data: rx.Var):
    return rx.list(
        link_data
        )


@rx.page(route="/game_printer", title="Game printer", on_load=FormInputState.retrieve_game_info)
def game_printer() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.text(
                FormInputState.game_name,
                align="center",
                justify="center",
                size="7",
                spacing=Size.DEFAULT.value,
                style=styles.game_title_style,
            ),
            rx.link(
                rx.image(src=FormInputState.image_small),
                href= FormInputState.image,
                is_external=True,
            ),
            rx.scroll_area(
                rx.text(
                    FormInputState.description,
                    align="center",
                    justify="center",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.game_description_style,
                ),
                padding_right="8px",
                type="always",
                scrollbars="vertical",
                style= {"width": 700, "height": 180},
                margin_top=Size.DEFAULT.value,
            ),
            rx.hstack(
                rx.text(
                    f" Year Published: ",
                    align="left",
                    justify="left",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                    text_decoration="underline",
                ),
                rx.text(
                    FormInputState.year_published,
                    align="left",
                    justify="left",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                ),
                margin_top=Size.BIG.value,
            ),
            rx.hstack(
                rx.text(
                    "NumPlayers: ",
                    align="left",
                    justify="center",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                    text_decoration="underline",
                ),
                rx.text(
                    # check_equals(FormInputState.min_players, FormInputState.max_players),
                    rx.cond(
                        (FormInputState.min_players != FormInputState.max_players),
                        rx.text(f"{FormInputState.min_players} - {FormInputState.max_players}"),
                        rx.text(f"{FormInputState.min_players}"),
                    ),
                    align="left",
                    justify="center",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                ),
                margin_top=Size.SMALL.value,
            ),
            rx.hstack(
                rx.text(
                    f"Playtime: ",
                    align="left",
                    justify="center",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                    text_decoration="underline",
                ),
                rx.text(
                    rx.cond(
                        (FormInputState.min_playtime != FormInputState.max_playtime),
                        rx.text(f"{FormInputState.min_playtime} - {FormInputState.max_playtime} min"),
                        rx.text(f"{FormInputState.min_playtime} min"),
                    ),
                    # check_equals(FormInputState.min_playtime, FormInputState.max_playtime),
                    align="left",
                    justify="center",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                ),
                margin_top=Size.SMALL.value,
            ),
            rx.hstack(
                rx.text(
                    "MinAge: ",
                    align="left",
                    justify="center",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                    text_decoration="underline",
                ),
                rx.text(
                    FormInputState.min_age,
                    align="left",
                    justify="center",
                    size="4",
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_style,
                ),
                margin_top=Size.SMALL.value,
            ),
            rx.text(
                f"Designers: ",
                align="left",
                justify="center",
                size="4",
                spacing=Size.DEFAULT.value,
                style=styles.finder_style,
                margin_top=Size.DEFAULT.value,
            ),
            rx.foreach(FormInputState.designers, render_link),
            rx.text(
                f"Artists: ",
                align="left",
                justify="center",
                size="4",
                spacing=Size.DEFAULT.value,
                style=styles.finder_style,
                margin_top=Size.DEFAULT.value,
            ),
            rx.foreach(FormInputState.artists, render_link),
            rx.text(
                "Publishers: ",
                align="left",
                justify="center",
                size="4",
                spacing=Size.DEFAULT.value,
                style=styles.finder_style,
                margin_top=Size.DEFAULT.value,
            ),
            rx.foreach(FormInputState.publishers, render_link),
        align="center",
        justify="center",
        ),
        footer(),
    )