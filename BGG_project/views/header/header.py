import reflex as rx
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles


def header() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Welcome to",
                    size="7",
                    style=styles.header_title_style
                ),
                rx.heading(
                    "BGG boardgame finder", 
                    size="9",
                    style=styles.header_title_style
                ),
                align="center"
    )