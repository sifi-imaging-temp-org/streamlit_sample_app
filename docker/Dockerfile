# 参考： 
#   - multi stage build
#       - https://laid-back-scientist.com/multi-stage-build
#   - uv
#       - https://docs.astral.sh/uv/guides/integration/docker/
#       - https://qiita.com/hkzm/items/3366e09733acfc524b2b
#       - https://skydum.hatenablog.com/entry/2024/09/09/215936

ARG PYTHON_VERSION="3.12"

# building stage
FROM python:${PYTHON_VERSION}-slim AS builder
#FROM ghcr.io/astral-sh/uv:python${PYTHON_VERSION%.*}-bookworm-slim as builder

WORKDIR /app

ENV UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_CACHE_DIR=/root/.cache/uv \
    UV_LINK_MODE=copy
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=cache,target=${UV_CACHE_DIR} \
    uv export --frozen --no-dev --format requirements-txt > requirements.txt \
    && uv pip install -r requirements.txt 

# production stage
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/streamlit /usr/local/bin/streamlit

WORKDIR /app
COPY src .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py"]

