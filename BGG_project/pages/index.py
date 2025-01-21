import reflex as rx
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.views.header.header import header
from BGG_project.views.finder.finder import finder
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles


class State(rx.State):
    pass


@rx.page(route="/home", title="home")
def index() -> rx.Component:  
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
    )