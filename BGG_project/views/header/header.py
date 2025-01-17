import reflex as rx
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font


def header() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Welcome to",
                    size="7",
                    color=TextColor.HEADER.value,
                    font_family=Font.TITLE
                ),
                rx.heading(
                    "BGG boardgame finder", 
                    size="9",
                    color=TextColor.HEADER.value,
                    font_family=Font.TITLE
                ),
                align="center"
    )