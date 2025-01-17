import reflex as rx
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles


def navbar() -> rx.Component:
    return rx.flex(
            rx.image(src="/face-logo.png", width="200px", height="auto", align="left", justify="center"),
            rx.spacer(),
            #ESTO HAY QUE CAMBIARLO POR EL LOGIN
            rx.text(
                "Aquí irá login",
                align="right",
                justify="center",
                size="4",
                color=TextColor.FOOTER.value,
                style=styles.navbar_title_style
            ),
            width="100%",
            position= "sticky",
            z_index="999",
            top="0"
        )

