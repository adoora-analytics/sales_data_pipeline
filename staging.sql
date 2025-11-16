create table W4D7_staging (
    sale_id bigint primary key,
    customer_id int,
    product_id int,
    date_id int,
    customer_name text,
    email text,
    region text,
    quantity int,
    revenue numeric(12,2),
    product_name text,
    category text,
    price numeric(12,2),
    order_date date,
    order_month smallint check (order_month between 1 and 12),
    order_year smallint check (order_year between 2024 and 2025)
);


