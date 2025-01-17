import reflex as rx
from BGG_project.styles.colors import TextColor as TextColor


def header() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Welcome to",
                    size="7",
                    color=TextColor.HEADER.value
                ),
                rx.heading(
                    "BGG boardgame finder", 
                    size="9",
                    color=TextColor.HEADER.value
                ),
                align="center"
    )