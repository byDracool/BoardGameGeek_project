import reflex as rx
from BGG_project.pages.index import index
from BGG_project.pages.owned_user_games import stored_games
import BGG_project.styles.styles as styles


app = rx.App(
    #rx.theme(color_mode="dark", accent_color="blue"),
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(index)
app.add_page(stored_games)