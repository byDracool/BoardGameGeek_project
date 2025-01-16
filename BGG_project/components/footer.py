import reflex as rx


def footer() -> rx.Component:
    return rx.vstack(
                rx.logo(),
                align="end",
    )