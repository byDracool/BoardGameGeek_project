import reflex as rx
import BGG_project.styles.styles as styles


def header() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Welcome to",
                    style=styles.pretitle_style
                ),
                rx.heading(
                    "BGG boardgame finder", 
                    style=styles.title_style
                ),
                align="center"
    )