# app/my_reflex_app/my_reflex_app.py
import reflex as rx

def index() -> rx.Component:
    """The main page. Don't expect much."""
    return rx.center(
        rx.vstack(
            rx.heading("Behold! Code in a Box!", size="8"),
            rx.text("It's probably broken somewhere else."),
            align="center",
            spacing="7", # Arbitrary spacing. 
            font_size="2em", 
        ),
        height="100vh", # fill the screen
    )

# Boilerplate to make Reflex happy.
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    ),
)
app.add_page(index, route="/") # The main page route.
