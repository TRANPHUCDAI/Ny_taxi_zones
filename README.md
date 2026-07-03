# NYC Taxi Data Engineering Pipeline

Dự án này xây dựng một Data Pipeline hoàn chỉnh đóng gói bằng **Docker** để tự động tải, xử lý và nạp (ingest) dữ liệu lớn từ kho dữ liệu mở **NYC TLC (New York City Taxi and Limousine Commission)** vào cơ sở dữ liệu **PostgreSQL**.

Hệ thống được tối ưu hóa hiệu năng bằng cách băm nhỏ dữ liệu dữ liệu chuyến đi lớn (`ingest_data.py`) và xử lý danh mục vùng nhanh gọn (`ingest_zones.py`) bằng thư viện Pandas kết hợp công cụ quản lý môi trường siêu tốc **`uv`**.

---

## Kiến Trúc Hệ Thống (Architecture)

1. **PostgreSQL Database:** Lưu trữ dữ liệu thô (Raw Data) tập trung, ánh xạ dữ liệu qua Docker Volume để không bị mất dữ liệu khi container tắt.
2. **pgAdmin:** Giao diện trực quan hóa dữ liệu giúp truy vấn nhanh dữ liệu đã nạp.
3. **Ingestion Engine (Docker App):** Image được build đa tầng (multi-stage) tối ưu dung lượng, chứa bộ đôi script Python tự động kết nối qua mạng nội bộ Docker (`Bridge Network`).

---

## Cấu Trúc Thư Mục Dự Án (Project Structure)

```text
├── ny_taxi_postgres_data/    # Thư mục lưu dữ liệu database (Đã thêm vào .gitignore)
├── Dockerfile                # File đóng gói môi trường chạy Pipeline với uv và Python
├── docker-compose.yaml       # Quản lý cơ sở hạ tầng (Postgres, pgAdmin, Network)
├── ingest_data.py            # Script xử lý & nạp dữ liệu chuyến đi taxi (dữ liệu lớn)
├── ingest_zones.py           # Script nạp danh mục thông tin vùng (Zones)
├── pyproject.toml            # Khai báo dependency (pandas, sqlalchemy, psycopg, click)
├── uv.lock                   # File khóa phiên bản package đồng bộ chính xác
└── README.md                 # Tài liệu hướng dẫn dự án này