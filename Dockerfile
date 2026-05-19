FROM python:3.14-slim

WORKDIR /app

# Install runtime dependencies
COPY pyproject.toml uv.lock ./
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir "uvicorn[standard]>=0.23.0" \
    && pip install --no-cache-dir "mcp[cli]>=1.27.1" \
    && pip install --no-cache-dir "uv>=0.11.0"

COPY . .

ENV PORT=8080
EXPOSE 8080

CMD ["python", "server.py"]
