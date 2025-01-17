import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.reflex_logo import reflex_logo
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles
from BGG_project.styles.styles import PORTFOLIO


def footer() -> rx.Component:
    return rx.vstack(
        rx.spacer(),
        rx.link(
                "Carlos Terrez '2025",
                href=PORTFOLIO,
                size="1",
                is_external=True,
                style=styles.footer_style
                ),
        reflex_logo(),
        margin="0",
        align="center",
        padding_top=Size.EXTRA_BIG.value
    )