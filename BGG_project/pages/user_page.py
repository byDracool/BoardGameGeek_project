import reflex as rx
from ..model.user_model import User
from ..service.user_service import select_all, select_all_user_service, select_user_by_email_service, create_user_service, delete_user_service
from .notify import notify_component
import asyncio


class UserState(rx.State):
    #states
    users:list[User]
    user_buscar: str
    error: str = ""

    #@rx.background
    @rx.event(background=True)
    async def get_all_user(self):
        async with self:
            self.users = select_all()

    #@rx.background
    @rx.event(background=True)
    async def get_user_by_email(self):
        async with self:
            self.users = select_user_by_email_service(self.user_buscar)


    async def handleNotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error = ""


    #@rx.background
    @rx.event(background=True)
    async def create_user(self, data: dict):
        async with self:
            try:
                self.users = create_user_service(username= data["username"], password= data["password"], name= data["name"])
            except BaseException as be:
                print(be.args)
                self.error = be.args
        await self.handleNotify()


    def buscar_on_change(self, value:str):
        self.user_buscar = value


    #@rx.background
    @rx.event(background=True)
    async def delete_user_by_email(self, email):
        async with self:
            self.users = delete_user_service(email)


@rx.page(route="/user", title="user", on_load=UserState.get_all_user)
def user_page() -> rx.Component:
    return rx.flex(
        rx.heading("Users", align="center"),
        rx.hstack(
            buscar_user_component(),
            create_user_dialogo_component(),
            justify="center",
            style={"margin_top": "30px"}
        ),
        table_use(UserState.users),
        rx.cond(
            UserState.error != "",
            notify_component(UserState.error, "shield-alert", "yellow")
        ),
        direction="column",
        style={"width": "60vw", "margin": "auto"}
    )


def table_use(list_user: list[User]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Action"),
            )
        ),
        rx.table.body(
            rx.foreach(list_user, row_table)
        )
    )


def row_table(user:User) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.username),
        rx.table.cell(rx.hstack(
            delete_user_dialogo_component(user.username)
        ))
    )


def buscar_user_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Enter email", on_change=UserState.buscar_on_change),
        rx.button("Find user", on_click=UserState.get_user_by_email)
    )


def create_user_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Name",
                name="name"
            ),
            rx.input(
                placeholder="Email",
                name="username"
            ),
            rx.input(
                placeholder="Password",
                name="password",
                type='password'
            ),
            rx.dialog.close(
                rx.button("Save", type="submit")
            ),
        ),
        on_submit=UserState.create_user,
    )


def create_user_dialogo_component() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Add user")),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Add user"),
                create_user_form(),
                justify="center",
                align="center",
                direction="column",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancel", color_scheme="gray", variant="soft")
                ),
                spacing="3",
                margin_top="16xp",
                justify="end",
            ),
            style={"width": "300px"}
        ),
    )


def delete_user_dialogo_component(username:str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon("trash-2"))),
        rx.dialog.content(
                rx.dialog.title("Delete user"),
                rx.dialog.description("Do you want to delete user: " + username),
                rx.flex(
                    rx.dialog.close(
                        rx.button("Cancel", color_scheme="gray", variant="soft")
                    ),
                    rx.dialog.close(
                        rx.button("Confirm", on_click=UserState.delete_user_by_email(username)),
                    ),
                    spacing="3",
                    margin_top="16xp",
                    justify="end",
                )        
            )
        )