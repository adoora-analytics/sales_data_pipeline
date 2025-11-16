import psycopg2
from utils.config import load_config


def get_connection():
    cfg = load_config()
    db_cfg = cfg["db"]

    return psycopg2.connect(
        host=db_cfg['host'],
        dbname=db_cfg['dbname'],
        user=db_cfg['user'],
        password=db_cfg['password'],
        port=db_cfg['port'],
    )
    