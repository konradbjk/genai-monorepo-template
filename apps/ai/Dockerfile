FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Set working directory
WORKDIR /app

# Install the dependencies
RUN uv sync --frozen --no-cache

EXPOSE 8080

# Command to run the application
# TODO: Move dependencies installation to separate step
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
