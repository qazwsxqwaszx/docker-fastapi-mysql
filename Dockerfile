# 
# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app

# 安装编译依赖
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps -w wheels -r requirements.txt
COPY . .

# Stage 2: Runtime
FROM python:3.11-slim AS runtime
WORKDIR /app

# （可选）创建非 root 用户
RUN groupadd -r appgroup \
 && useradd -r -g appgroup appuser

# 复制并安装 wheel
COPY --from=builder /app/wheels wheels
RUN pip install --no-cache-dir wheels/*

# 复制应用代码
COPY --from=builder /app/app app

# 日志目录与权限
RUN mkdir -p logs \
 && chown -R appuser:appgroup /app

USER appuser

# 暴露端口 & 健康检查
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# 启动
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
