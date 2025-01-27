import reflex as rx
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles
from BGG_project.styles.styles import Size as Size
from BGG_project.python_code.vars_and_consts import HOME


def navbar() -> rx.Component:
    return rx.flex(
            rx.image(
                src="/face-logo.png", 
                width="200px", 
                height="auto", 
                align="left", 
                justify="center", 
                alt="BoardGameGeek logo. Drawing of character with glasses"
                ),
            rx.spacer(),
            rx.hstack(
                rx.link(
                        "Home",
                        href=HOME,
                        size="4",
                        is_external=False,
                        style=styles.navbar_style,
                        spacing=Size.DEFAULT.value,
                        ),
                rx.spacer(),        
                ),
            width="auto",
            position= "sticky",
            z_index="999",
            top="0"
        )

