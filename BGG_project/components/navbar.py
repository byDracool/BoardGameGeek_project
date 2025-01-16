import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
                rx.image(src="/face-logo.png", width="200px", height="auto", align="left", justify="center"),
                rx.text(
                    "Aqui ira login",
                    align="right",
                    justify="center",
                    size="4",               
                ),
                position= "sticky",
                z_index="999"
    )