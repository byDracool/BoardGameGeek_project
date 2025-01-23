import reflex as rx
from BGG_project.styles.styles import Size as Size
import BGG_project.styles.styles as styles
from BGG_project.components.navbar import navbar


lista_prueba = ['1911 Amundsen vs Scott', '5-Minute Dungeon', '5-Minute Dungeon: Curses! Foiled Again!', '7 Wonders Duel', '7 Wonders Duel: Pantheon', 
                'Aftermath', 'Agricola', 'Amun-Re', 'Ankh: Gods of Egypt', 'Ankh: Gods of Egypt – Guardians Set', 'Ankh: Gods of Egypt – Pantheon', 
                'Ankh: Gods of Egypt – Pharaoh', 'Ankh: Gods of Egypt – Tomb of Wonders', 'Architects of the West Kingdom', 'Asante', 'Ascension: Realms Unraveled', 
                'Azul', 'Azul: Stained Glass of Sintra', 'Bandido', 'Barony', 'Bears vs Babies']

username = "byDracool"


@rx.page(route="/owned_games", title="Owned games")
def stored_games() -> rx.Component:  
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                    rx.text(
                        "User  " + "'" + username + "'",
                        align="center",
                        justify="center",
                        size="5",
                        spacing=Size.DEFAULT.value,
                        style=styles.header_style
                    ),
                    rx.text(
                        "Games stored in BGG:",
                        align="center",
                        justify="center",
                        size="5",
                        padding_top=Size.EXTRA_SMALL.value,
                        spacing=Size.DEFAULT.value,
                        style=styles.header_style
                    ),
                    rx.list(
                        [rx.list.item(game) for game in lista_prueba],
                        padding_top=Size.DEFAULT.value,
                    ),
            ),
        )
    ) 