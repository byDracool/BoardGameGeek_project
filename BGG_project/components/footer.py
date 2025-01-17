import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.reflex_logo import reflex_logo


def footer() -> rx.Component:
    return rx.vstack(
        rx.spacer(),
        reflex_logo(),
        align="center",
        padding_top=Size.EXTRA_BIG.value
    )