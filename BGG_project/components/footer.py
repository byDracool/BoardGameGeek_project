import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.reflex_logo import reflex_logo
from BGG_project.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.spacer(),
        rx.text(
                    "Carlos Terrez '2025",
                    size="2",
                    color=TextColor.FOOTER.value,
                    margin_bottom=Size.SMALL.value
                ),
        reflex_logo(),
        align="center",
        padding_top=Size.EXTRA_BIG.value,
        color=TextColor.FOOTER.value
    )