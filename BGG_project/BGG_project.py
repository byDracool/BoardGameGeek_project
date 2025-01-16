import reflex as rx
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.views.header.header import header
from BGG_project.views.finder.finder import finder
import BGG_project.styles.styles as styles


class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(                
                    header(),
                    rx.spacer(),
                    finder(),
                    align="center",
                    margin_y=styles.Size.DEFAULT
            )
        ),
        footer(),
        rx.theme(color_mode="dark", accent_color="blue"),
        margin_y=styles.Size.SMALL
    )


app = rx.App()
app.add_page(index)
app._compile()
