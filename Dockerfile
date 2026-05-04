# Astral optimized uv image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim 

WORKDIR /app

COPY pyproject.toml ./

# install dependencies
RUN uv sync --no-install-project

# copy agent code
COPY . .

CMD ["uv", "run", "agent.py"]
