import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.find_icon import find_icon
from BGG_project.styles.colors import TextColor as TextColor
from BGG_project.styles.fonts import Font as Font
import BGG_project.styles.styles as styles


def finder() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Write the game name you are looking for:",
                    align="center",
                    size="5",
                    padding_top=Size.DEFAULT.value,
                    spacing=Size.DEFAULT.value,
                    style=styles.finder_title_style
                ),
                rx.text_area(
                    placeholder="Type here...",
                    spacing=Size.MEDIUM.value,
                    style=styles.finder_title_style
                ),
                find_icon(),
                align="center",
    )