import reflex as rx
from BGG_project.components.reflex_logo import reflex_logo


def footer() -> rx.Component:
    return rx.hstack(
                reflex_logo(),
                #position= "sticky",
                align="end"
    )