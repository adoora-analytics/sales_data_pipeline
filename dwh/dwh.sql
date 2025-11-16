

-- dimension customer
create table dim_customer(
    customer_id int primary key,
    customer_name text,
    email text,
    region text
);
-- index creation for dim_customer
create index ux_region
on dim_customer(region);




-- dimension product
create table dim_product(
    product_id int primary key,
    product_name text,
    category text
);
-- index creation for dim_product
create index ux_category
on dim_product(category);



-- dimension date creation
create table dim_date(
    date_id int primary key,
    order_date date NOT NULL,
    order_month smallint NOT NULL check (order_month between 1 and 12),
    order_year smallint NOT NULL check (order_year between 2024 and 2025)
);




-- fact sales table creation
create table fact_sales(
    sale_id int primary key,
    customer_id int NOT NULL REFERENCES dim_customer(customer_id),
    product_id int NOT NULL REFERENCES dim_product(product_id),
    date_id int NOT NULL REFERENCES dim_date(date_id),
    quantity int NOT NULL CHECK (quantity > 0),
    revenue numeric(12,2) NOT NULL CHECK (revenue > 0),
    price numeric(12,2) NOT NULL CHECK (price > 0)
);
-- index creation for fact_sales
create index ix_customer
on fact_sales(customer_id);
create index ix_product
on fact_sales(product_id);
create index ix_date
on fact_sales(date_id);
