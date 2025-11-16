
-- dim customer population
insert into dim_customer (customer_id, customer_name, email, region)
select distinct
    customer_id,
    customer_name,
    email,
    region
from  W4D7_staging
where customer_id is not null
on CONFLICT (customer_id) DO UPDATE
    set customer_name = EXCLUDED.customer_name,
        email         = EXCLUDED.email,
        region        = EXCLUDED.region;


-- dim product population
insert into dim_product (product_id, product_name, category)
select distinct 
    product_id,
    product_name,
    category
from  W4D7_staging
where product_id is not null
on CONFLICT (product_id) DO UPDATE
    set product_name = EXCLUDED.product_name,
        category     = EXCLUDED.category;



-- dim date population
insert into dim_date (date_id, order_date, order_month, order_year)
select distinct
    date_id,
    order_date,
    order_month,
    order_year
from  W4D7_staging
where date_id is not null
on CONFLICT (date_id) DO UPDATE
    set order_date  = EXCLUDED.order_date,
        order_month = EXCLUDED.order_month,
        order_year  = EXCLUDED.order_year;


-- fact sales population
insert into fact_sales (sale_id, customer_id, product_id, date_id, quantity, revenue, price )
select
    sale_id,
    customer_id,
    product_id,
    date_id,
    quantity,
    revenue,
    price
from  W4D7_staging
where sale_id is not null
on CONFLICT (sale_id) DO NOTHING;