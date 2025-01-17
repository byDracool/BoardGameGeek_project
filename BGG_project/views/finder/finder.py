import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.find_icon import find_icon


def finder() -> rx.Component:
    return rx.vstack(
                rx.text(
                    "Write the game name you are looking for:",
                    align="center",
                    size="5",
                    padding_top=Size.MEDIUM.value,
                    spacing=Size.MEDIUM.value
                ),
                rx.text_area(
                    placeholder="Type here...",
                    spacing=Size.SMALL.value
                ),
                find_icon(),
                align="center",
    )