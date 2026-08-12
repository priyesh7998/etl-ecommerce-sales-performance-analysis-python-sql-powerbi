# CartFlow — Synthetic E-Commerce OLTP Dataset

A synthetic-but-realistic e-commerce dataset built for an end-to-end analytics
pipeline: **Python/Pandas (clean & transform) → SQL Server (OLTP staging +
One Big Table) → Power BI (dashboard)**.

## Files & row counts
| File | Rows | Grain |
|---|---|---|
| `categories.csv` | 39 | 1 row per category (9 departments + their sub-categories) |
| `products.csv` | 600 | 1 row per product |
| `customers.csv` | 3,000 | 1 row per customer |
| `orders.csv` | ~12,070 | 1 row per order (header) |
| `order_items.csv` | ~34,150 | 1 row per line item within an order |
| `payments.csv` | ~12,500 | 1 row per payment attempt (some orders have a failed retry row) |

## Entity relationship
```
categories (1) ───< categories (self-ref: parent_category_id)  [department → sub-category]
categories (1) ───< products (category_id)
customers  (1) ───< orders (customer_id)
orders     (1) ───< order_items (order_id)
products   (1) ───< order_items (product_id)
orders     (1) ───< payments (order_id)   -- usually 1:1, occasionally 1:many (retry)
```

## Column notes (key fields only)

**categories**: `category_id`, `category_name`, `parent_category_id` (null for
top-level departments), `department`

**products**: `product_id`, `product_name`, `category_id` (FK → leaf category),
`brand`, `unit_price`, `cost_price`, `stock_quantity`, `is_active`,
`created_date`, `avg_rating`

**customers**: `customer_id`, `first_name`, `last_name`, `email` (some nulls),
`phone` (mixed formats on purpose), `gender`, `date_of_birth` (some nulls),
`city`, `state`, `country`, `signup_date`, `customer_segment` (all null —
mirrors real systems where this is computed later by an RFM/segmentation job,
not stored at signup), `is_subscribed_newsletter`

**orders**: `order_id`, `customer_id`, `order_date` (datetime), `order_status`
(Delivered/Shipped/Processing/Cancelled/Returned), `order_channel`
(Website/Mobile App/Mobile Web), `shipping_city`, `shipping_state`,
`shipping_fee`, `order_subtotal`, `order_total`

**order_items**: `order_item_id`, `order_id`, `product_id`, `quantity`,
`unit_price`, `discount_percent`, `line_total`

**payments**: `payment_id`, `order_id`, `payment_method` (UPI/Credit
Card/Debit Card/Cash on Delivery/Net Banking/Wallet), `payment_status`
(Completed/Pending/Failed/Refunded), `payment_date`, `amount`,
`transaction_fee`

## Realism built in
- **Seasonality**: order volume spikes around Republic Day sale (late Jan),
  Independence Day sale (Aug 5–15), Diwali/Big Billion Days (Oct–mid Nov,
  the biggest spike), and Dec 20–31, plus mild YoY growth 2023→2025.
- **Pareto customers**: a small share of customers place a disproportionate
  share of orders (classic 80/20 behavior).
- **Zipfian product popularity**: a handful of products account for most
  order-item volume; most products sell rarely.
- **India-flavored context**: INR price bands, Indian cities/states, UPI/COD
  alongside cards, realistic order-status and payment-method mixes.
- **Deliberate messiness for your Pandas cleaning step**: some missing
  emails/DOBs, inconsistent name casing and stray whitespace, three phone
  number formats, ~0.5–0.6% duplicate rows in `orders`/`order_items`, a
  handful of fat-fingered `order_total` outliers, and `customer_segment`
  left entirely null (you derive it — that's a great transformation step).

## Suggested pipeline
1. **Extract**: load the 6 CSVs with pandas.
2. **Transform (pandas)**: dedupe, standardize phone/name formatting, handle
   nulls, cast dates, recompute/validate `order_total`, derive
   `customer_segment` (e.g., RFM: recency/frequency/monetary), flag outliers.
3. **Load (OLTP)**: push the cleaned normalized tables into SQL Server as
   staging tables (mirrors the 6-table relational structure above).
4. **Model (One Big Table)**: in SQL Server (view/stored proc) or in pandas,
   join order_items → orders → customers → products → categories → payments
   into one denormalized `fact_sales_obt` table — one row per order line
   item, with every dimension attribute flattened in. This is what Power BI
   imports.
5. **Visualize (Power BI)**: revenue trends & seasonality, category/brand
   performance, customer segment/RFM analysis, payment method mix & failure
   rate, cancellation/return rate, channel performance (Web vs App).
