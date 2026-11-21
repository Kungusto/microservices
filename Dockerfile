# Запускать в контексте корневой папки всего проекта
FROM python:3.12.9
ARG SERVICE

WORKDIR /app/$SERVICE

# Установка uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# Добавление shared библиотеки
COPY $SERVICE/pyproject.toml $SERVICE/uv.lock ./
COPY shared/ /app/shared/
# Исходники приложения
COPY ${SERVICE}/src/ ./src/


RUN uv sync --locked

ENV PYTHONPATH=/app
ENV PATH="/app/${SERVICE}/.venv/bin:$PATH"

CMD ["python", "src/main.py"]
