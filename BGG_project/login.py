import reflex as rx
import requests as rq
from BGG_project.styles.colors import TextColor
import BGG_project.styles.styles as styles
from BGG_project.styles.styles import Size as Size
import re


class LoginState(rx.State):
    loader:bool = False
    username:str = "example@gmail.com"
    password:str
    error = False

    #@rx.background
    @rx.event(background=True)
    async def loginService(self, data: dict):
            async with self:
                self.loader = True
                self.error = False
                response = rq.post('http://localhost:8080/auth/login', json=data, headers={"Content-Type":"application/json"})
                if response.status_code == 200:
                        self.response = response.json()
                        self.loader = False
                        return  rx.redirect('/')
                else:
                        self.loader = False
                        self.error = True


    #@rx.var
    @rx.var(cache=True)
    def user_invalid(self) -> bool:
        return not (re.match(r"[^@]+@[^@]+.[^@]+", self.username) and "example@gmail.com")
    

    #@rx.var
    @rx.var(cache=True)
    def user_empty(self) -> bool:
        return not self.username.strip()
    

    #@rx.var
    @rx.var(cache=True)
    def password_empty(self) -> bool:
        return not self.password.strip()
    

    #@rx.var
    @rx.var(cache=True)
    def validate_fields(self) -> bool:
        return (
            self.user_empty
            or self.user_invalid
            or self.password_empty
        )
          

@rx.page(route="/login", title="login")
def login() -> rx.Component:
    return rx.flex( 
        rx.vstack(
            rx.spacer(),
            rx.hstack(
                rx.image(
                        src="/login.png",
                        width="200px", 
                        height="auto",
                        align="center", 
                        justify="center",
                        padding_top=Size.EXTRA_BIG.value
                        ),
                rx.spacer(),
                rx.text(
                        "Login",
                        size="7",
                        style=styles.header_style
                    ),
                align="center",
                justify="center"    
            ),
            rx.form.root(
                rx.vstack(
                    field_form_component_general("User", "Enter your email address", "Enter a valid email address", "username", 
                                                LoginState.set_username, LoginState.user_invalid),

                    field_form_component("Password", "Enter your password", "password", 
                                                LoginState.set_password, "password"),

                    rx.form.submit(
                        rx.cond(
                            LoginState.loader,
                            rx.spinner(color="red", size="2"),
                            rx.button(
                                    "Login",
                                    disabled=LoginState.validate_fields,
                                    width="30vw"
                            ),
                        ),
                        as_child=True,
                    ),
                ),
                rx.cond(
                      LoginState.error,
                      rx.callout(
                            "A valid Email is required",
                            icon="triangle-alert",
                            color_scheme="red",
                            role="alert",
                            style={"margin_top":"10px"}
                      ),
                ),
                on_submit=LoginState.loginService,
                reset_on_submit=True,
                width="80%",
            ),
            align="center",
            justify="center",                                    
        ),
        align="center",
        justify="center"  
    )    


def field_form_component(label:str, placeholder:str, name_var:str,
                         on_change_function, type_field:str) -> rx.Component:
        return rx.form.field(
                rx.flex(
                        rx.form.label(label, color=TextColor.HEADER),
                        rx.form.control(
                            rx.input(
                                    placeholder=placeholder,
                                    on_change=on_change_function,
                                    name=name_var,
                                    type=type_field,
                                    required=True,
                            ),
                            as_child=True,
                    ),
                    rx.form.message(
                        "Field cannot be null",
                        match="valueMissing",
                        color="red",
                    ),
                    direction="column",
                    spacing="2",
                    align="stretch"
                ),
            name=name_var,
            width="30vw"      
            )


def field_form_component_general(label:str, placeholder:str, message_validate:str, name:str,
                                    on_change_function, show) -> rx.Component:
      return rx.form.field(
                rx.flex(
                        rx.form.label(label, color=TextColor.HEADER),
                        rx.form.control(
                        rx.input(
                                placeholder=placeholder,
                                on_change=on_change_function,
                                name=name,
                                required=True,
                        ),
                        as_child=True,
                        ),
                        rx.form.message(
                            message_validate,
                            name=name,
                            match="valueMissing",
                            force_match=show,
                            color="red",
                        ),
                direction="column",
                spacing="2",
                align="stretch"
                ),
                name=name,
                width="30vw"  
            )