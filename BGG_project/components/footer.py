import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.reflex_logo import reflex_logo
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles
from BGG_project.python_code.vars import PORTFOLIO, GITHUB_REPO


def footer() -> rx.Component:
    return rx.vstack(
        rx.spacer(),
        rx.hstack(
            rx.link(
                    rx.image(
                        src="/github.svg",
                        width=Size.MEDIUM.value,
                        height=Size.MEDIUM.value, 
                    ),
                    href=GITHUB_REPO,
                    is_external=True
                    ),
            rx.link(
                    "Carlos Terrez '2025",
                    href=PORTFOLIO,
                    size="1",
                    is_external=True,
                    style=styles.footer_style
                    ),
        ),    
        reflex_logo(),
        margin="0",
        align="center",
        padding_top=Size.BIG.value,
        padding_bottom=Size.DEFAULT.value
    )