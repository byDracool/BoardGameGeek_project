import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Welcome to",
                    size="7"
                ),
                rx.heading(
                    "BGG boardgame finder", 
                    size="9"
                ),
                align="center"
    )