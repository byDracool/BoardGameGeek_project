import reflex as rx
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.views.header.header import header
from BGG_project.views.finder.finder import finder
from BGG_project.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(                
                    header(),
                    finder(),
                    align="center",
                    margin_y=Size.DEFAULT.value
            )
        ),
        footer(),
        #rx.theme(color_mode="dark", accent_color="blue"),
        margin_y=Size.SMALL.value
    )


app = rx.App()
app.add_page(index)
app._compile()
