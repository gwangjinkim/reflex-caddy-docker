# app/Dockerfile

# Start with a basic Python box. 'Slim' means fewer toys included.
FROM python:3.12-slim

# Environment variables to make Python slightly less annoying in Docker.
ENV PYTHONDONTWRITEBYTECODE 1 # No useless .pyc files.
ENV PYTHONUNBUFFERED 1       # Logs appear faster, maybe.

# => Install uv globally by copying the binary from the official container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory before copying!
WORKDIR /app

# Now copy all of your brilliant code.
COPY . .

# Install system stuff needed because 'slim' is TOO slim.
# Reflex needs 'unzip' and 'curl' to install its JavaScript friend 'bun'.
# Yes, the Python framework needs JavaScript tools. Don't ask.
RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    curl \
    # Clean up afterward to keep the box slightly less bloated.
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN uv venv \
    && echo "Checking if .venv was created:" \
    && ls -la /app/.venv


# Install your dependencies inside that venv
RUN uv pip install --system -r requirements.txt

# Tell Docker which ports the app *inside* the box will try to use.
# 3000 for the web page part (frontend), 8000 for the Python brain (backend).
EXPOSE 3000
EXPOSE 8000

# The command to run when the container starts.
# This starts Reflex in 'dev' mode (slow, but reloads code changes).
CMD ["reflex", "run", "--frontend-port", "3000", "--backend-port", "8000"]
