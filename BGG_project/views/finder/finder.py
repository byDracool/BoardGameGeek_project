import reflex as rx


def finder() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Write the game name you are looking for:",
                    align="center",
                    size="5",
                ),
                rx.spacer(),
                rx.text_area(
                    placeholder="Type here...",
                ),
                rx.spacer(),
                rx.link(
                    rx.button(
                        "Find games",
                        rx.icon("search")
                        ),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                ),
                align="center",
    )