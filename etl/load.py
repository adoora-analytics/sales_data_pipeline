from utils.db import get_connection

def load(df, table_name: str):
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            f"""
            INSERT INTO {table_name} 
            (sale_id,
            customer_id,
            product_id,
            date_id,
            customer_name,
            email,
            region,
            quantity,
            revenue,
            product_name,
            category,
            price,
            order_date,
            order_month,
            order_year)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            [
                row["sale_id"],
                row["customer_id"],
                row["product_id"],
                row["date_id"],
                row["customer_name"],
                row["email"],
                row["region"],
                row["quantity"],
                row["revenue"],
                row["product_name"],
                row["category"],
                row["price"],
                row["order_date"],
                row["order_month"],
                row["order_year"],
            ],
        )
    conn.commit()
    conn.close()