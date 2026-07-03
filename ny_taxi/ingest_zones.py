
import pandas as pd
from sqlalchemy import create_engine
import click

@click.command()
@click.option('--pg-user', default='root')
@click.option('--pg-pass', default='root')
@click.option('--pg-host', default='pgdatabase')
@click.option('--pg-port', default=5432, type=int)
@click.option('--pg-db', default='ny_taxi')
@click.option('--target-table', default='taxi_zones')

def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

    # Kết nối Database
    engine = create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    df = pd.read_csv(url)

    print(f"Đang nạp dữ liệu vào bảng {target_table}...")

    # Ghi thẳng toàn bộ file vào Postgres, nếu trùng tên bảng thì ghi đè (replace)
    df.to_sql(name=target_table, con=engine, if_exists="replace")

if __name__ == '__main__':
    run()



