import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
                rx.image(src="/face-logo.png", width="200px", height="auto", align="left", justify="center"),
                #ESTO HAY QUE CAMBIARLO POR EL LOGIN
                rx.text(
                    "Aquí irá login",
                    align="right",
                    justify="center",
                    size="4",               
                ),
                position= "sticky",
                z_index="999",
                top="0"
    )