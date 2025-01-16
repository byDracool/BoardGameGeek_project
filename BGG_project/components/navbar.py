import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
                rx.image(src="/face-logo.png", width="200px", height="auto", align="start", justify="center"),
                rx.text(
                    "Aquí irá login",
                    align="right",
                    justify="center",
                    size="4",               
                ),
                position= "sticky",
                z_index="999"
    )