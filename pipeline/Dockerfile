# Bắt đầu với image Python 3.13-slim
FROM python:3.13.10-slim

# Sao chép file thực thi uv từ image uv chính thức (mô hình build đa tầng - multi-stage build)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Đặt thư mục làm việc
WORKDIR /app

# Thêm môi trường ảo (virtual environment) vào biến PATH để có thể sử dụng các package đã cài đặt
ENV PATH="/app/.venv/bin:$PATH"

# Sao chép các file cấu hình dependency trước (giúp Docker cache layer tốt hơn)
COPY "pyproject.toml" "uv.lock" ".python-version" ./
# Cài đặt các dependency từ file lock (đảm bảo tính tái lặp chính xác của bản build)
RUN uv sync --locked

# Sao chép mã nguồn ứng dụng vào sau
COPY pipeline.py pipeline.py

# Thiết lập điểm lệnh đầu vào
ENTRYPOINT ["uv", "run", "python", "pipeline.py"]

# Bước mượn công cụ: Bạn kéo ảnh "ghcr.io/astral-sh/uv:latest" về để copy file thực thi /uv vào thư mục /bin/ của Container (COPY --from=...).


# Bước setup môi trường nền: Bạn dùng bản "python:3.13.10-slim" làm nền để Container vừa nhẹ vừa bảo mật.

# Bước khóa thư viện: Câu lệnh "RUN uv sync --locked" đã đồng bộ hóa và cài đặt chính xác các thư viện được khai báo trong file uv.lock của bạn. Nhờ vậy, thư viện pandas đã được cài tự động vào trong Image.

# Bước đóng gói: Cuối cùng, bạn copy file code chính "COPY pipeline.py pipeline.py" vào thư mục /app.

# Image cuối cùng đã được lưu thành công trên máy của bạn với tên mã: "docker.io/library/test:pandas".