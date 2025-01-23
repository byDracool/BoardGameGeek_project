import reflex as rx
from BGG_project.styles.styles import Size as Size


def find_icon() -> rx.Component:
    return rx.link(
                    rx.button(
                        "Find games",
                        rx.icon("search")
                        ),
                    alt="Find icon",    
                    padding_top=Size.SMALL.value,
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True
                )


def find_user() -> rx.Component:
    return rx.link(
                    rx.button(
                        "Find user games",
                        rx.icon("user-search"),
                        type="submit"
                        ),
                    alt="Find BGG user",    
                    padding_top=Size.SMALL.value,
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True
                )