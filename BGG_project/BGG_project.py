import reflex as rx
from BGG_project.pages.index import index
from BGG_project.pages.owned_user_games import stored_games
from BGG_project.pages.finded_games import finded_games
from BGG_project.python_code.constants import *
import BGG_project.styles.styles as styles


app = rx.App(
    #rx.theme(color_mode="dark", accent_color="blue"),
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(index)
app.add_page(stored_games)
app.add_page(finded_games)