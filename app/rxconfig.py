# app/rxconfig.py
import reflex as rx
import os # Gotta talk to the operating system. Spooky.

# Figure out the public URL from an environment variable.
# Defaults to 'http://localhost' if you forget to set it later.
# Use 'https://your-domain.com' for real deployments, obviously.
deploy_url = os.environ.get("DEPLOY_URL", "http://localhost")

config = rx.Config(
    app_name="my_reflex_app", # The app's glorious name.
    # Tell Reflex how the outside world sees it. Crucial. Don't skip.
    frontend_url=deploy_url,
)
