import reflex as rx
from BGG_project.styles.styles import Size as Size
from BGG_project.components.reflex_logo import reflex_logo
from BGG_project.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.spacer(),
        rx.link(
                    "Carlos Terrez '2025",
                    href="https://carlosterrez.dev/",
                    size="2",
                    is_external=True,
                    color=TextColor.FOOTER.value
                ),
        reflex_logo(),
        align="center",
        padding_top=Size.EXTRA_BIG.value,
        color=TextColor.FOOTER.value
    )