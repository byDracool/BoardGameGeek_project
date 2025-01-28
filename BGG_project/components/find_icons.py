import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.python_code.constants import FINDED_GAMES_PAGE, OWNED_GAMES_PAGE


def find_icon() -> rx.Component:
    return rx.link(
                    rx.button(
                        "Find games",
                        rx.icon("search"),                   
                        type="submit",
                        align="center",
                        justify="center",
                        on_click=rx.redirect(
                           FINDED_GAMES_PAGE, 
                           is_external=False,
                           )
                        ),
                    alt="Find icon",    
                    padding_top=Size.SMALL.value,
                    is_external=True
                )


def find_user() -> rx.Component:
    return rx.link(
                    rx.button(
                        "Find user games",
                        rx.icon("user-search"),
                        type="submit",
                        align="center",
                        justify="center",
                        on_click=rx.redirect(
                            OWNED_GAMES_PAGE, 
                            is_external=False,
                            )
                        ),
                    alt="Find BGG user",    
                    padding_top=Size.SMALL.value,
                    is_external=True,
                    align="center",
                    justify="center",
                )