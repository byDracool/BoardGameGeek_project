"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


image = "https://cf.geekdo-images.com/W3Bsga_uLP9kO91gZ7H8yw__original/img/xV7oisd3RQ8R-k18cdWAYthHXsA=/0x0/filters:format(jpeg)/pic2419375.jpg"


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    
    return (
        rx.image(src="/bgg-logo.jpg", width="400px", height="auto", align="center", justify="center"),
        rx.image(src="/bgg-banner.png", width="auto", height="auto", align="center", justify="center"),
        rx.container(
            rx.theme(color_mode="dark", accent_color="blue"),
            
            rx.vstack(
                rx.text(
                    "Welcome to",
                    align="center",
                    size="7",
                ),
                rx.heading("BGG boardgame finder", size="9", align="center"),
                rx.image(src=image, width="100px", height="auto"),
                rx.text(
                    "Get started by editing ",
                    rx.code(f"{config.app_name}/{config.app_name}.py"),
                    align="center",
                    size="5",
                ),
                rx.link(
                    rx.button("Check out our docs!"),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True,
                ),
                spacing="5",
                align="center",
                justify="center",
                min_height="5vh",
            ),
            rx.logo(),
        )
    )

app = rx.App()
app.add_page(index)
app._compile()
