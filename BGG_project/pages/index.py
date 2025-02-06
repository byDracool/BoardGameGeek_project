import reflex as rx
from BGG_project.components.navbar import navbar
from BGG_project.components.footer import footer
from BGG_project.views.header.header import header
from BGG_project.views.finder.finder import finder
from BGG_project.styles.styles import Size as Size


class State(rx.State):
    pass


class ToastState(rx.State):
    @rx.event
    async def fetch_advertisement(self):
        yield rx.toast(
            """Due to a bug in the BGG website's API, it is necessary to run queries twice for them to work correctly. 
            We will resolve the issue as soon as possible. 
            Thanks in advance""",
            position='bottom-right',
            duration=15000,
            close_button=True,
            style={
                "background-color": "transparent",
                "color": "SteelBlue",
                "border": "1px solid SteelBlue",
                "border-radius": "0.53m",
                },
            )


@rx.page(route="/", title="home", on_load=ToastState.fetch_advertisement)
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