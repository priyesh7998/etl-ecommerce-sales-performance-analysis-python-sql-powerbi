# ETL-Ecommerce-Sales-Analysis-Python-SQL-PowerBI

**End-to-end e-commerce seller performance analytics on a synthetic dataset — Python (Pandas) ETL → SQL Server (dimensional model + One Big Table) → Power BI dashboard**

## 📑 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Tools & Technologies](#️-tools--technologies)
- [Methodology](#-methodology)
- [Key Insights](#-key-insights)
- [Dashboard](#️-dashboard)
- [How to Run This Project](#️-how-to-run-this-project)
- [Results & Conclusion](#-results--conclusion)
- [Future Work](#-future-work)
- [Author](#-author)
- [Repository Contents](#-repository-contents)

![Status](https://github.com/priyesh7998/etl-ecommerce-sales-performance-analysis-python-sql-powerbi/blob/main/dashboard_img/ecommerce_sales_analysis_dashboard.png) ![Python](https://img.shields.io/badge/Python-Pandas-blue) ![SQL Server](https://img.shields.io/badge/Database-SQL%20Server-CC2927) ![Power BI](https://img.shields.io/badge/Dashboard-Power%20BI-F2C811)

---

## 📌 Overview

This project is an end-to-end data analytics pipeline that simulates a
complete e-commerce seller performance workflow — from raw transactional
(OLTP) data all the way to an interactive executive dashboard. It was built
to demonstrate the full analytics engineer / BI analyst skill set: **data
cleaning and transformation, dimensional modeling, database loading, SQL
analysis, and dashboard storytelling.**

> **📁 About the data:** This project uses a **synthetic (artificially
> generated) dataset**, not real company or customer data. It was engineered
> in Python to statistically resemble a real e-commerce platform — including
> seasonality, skewed customer/product behavior, and realistic data-quality
> issues (duplicates, nulls, inconsistent formatting) — so the cleaning,
> modeling, and analysis steps mirror what a real analyst would do. No real
> people, businesses, or transactions are represented.

## 🎯 Problem Statement

E-commerce businesses generate transactional data across multiple
disconnected tables (customers, orders, payments, products), which makes it
hard for stakeholders to answer basic performance questions directly. This
project answers:

- What are total sales, purchases (cost), gross profit, and profit margin?
- Which states/regions drive the most revenue?
- Who are the highest-value customers, and which brands sell best?
- How does performance vary by gender and by month?
- Which customers should be flagged as high-priority accounts?

The goal was to take raw, unclean multi-table transactional data and turn it
into a single trustworthy source of truth that a business stakeholder could
explore in a live dashboard.

## 🛠️ Tools & Technologies

| Layer | Tools |
|---|---|
| Data cleaning & transformation | Python, Pandas, Jupyter Notebook |
| Database | Microsoft SQL Server (T-SQL) |
| Data modeling | Dimensional modeling (Customer & Product dimensions) + One Big Table (OBT) |
| Visualization | Power BI (DAX, interactive filters/slicers) |
| Version control | Git & GitHub |

## 🔄 Methodology

**1. Data Source**
Six related synthetic CSV tables — `customers`, `products`, `categories`,
`orders`, `order_items`, `payments` — generated in Python to carry
real-world characteristics (seasonality, Pareto-distributed customer value,
Zipfian product popularity, and intentional data-quality issues like nulls,
duplicate rows, and inconsistent formatting).

**2. Data Cleaning & Transformation (Python / Jupyter)**
- Removed duplicate records across all tables
- Handled missing values (nulls in emails, dates of birth, and other fields)
- Standardized and validated fields ahead of modeling

**3. Dimensional Modeling**
- **Customer table** — cleaned and transformed customer dimension
- **Product table** — `products` joined with `categories` on `category_id`
  to produce a single enriched product dimension
- **One Big Table (OBT)** — orders, order items, payments, and products
  joined into a single denormalized fact table optimized for fast,
  join-free reporting

**4. Loading**
- Loaded the cleaned dimension tables and the OBT into **SQL Server**
- Exported cleaned tables as CSV backups for local/offline use

**5. SQL Analysis**
- Wrote 4–5 T-SQL queries directly against SQL Server to validate metrics
  (e.g., sales by region, top customers, gross profit) before building the
  dashboard, ensuring the Power BI numbers reconcile with the database

**6. Dashboarding**
- Connected Power BI to SQL Server and built an interactive **E-Commerce
  Seller Performance Dashboard**

## 📊 Key Insights

- **Total Sales: 579.88M** against **Total Purchase (cost): 271.32M**,
  yielding a **Gross Profit of 308.55M** and a **50% profit margin**
- **Maharashtra** is the top-performing state by sales, followed by
  Gujarat, Tamil Nadu, Madhya Pradesh, Delhi, Haryana, and Assam
- **George Kakar** is the top customer by sales (40M), followed by
  Urishilla Mahal (24M) and Tanay Wali (13M)
- **Apple (192M)** and **Canon (191M)** are the leading brands by sales,
  well ahead of Nikon (66M) and TrendKart (39M)
- **Male customers (307M)** drive slightly more sales than **female
  customers (269M)**, with a small "Other" segment (4M)
- A dedicated high-priority customer table flags top accounts by total
  sales and purchase value for account management follow-up

## 🖥️ Dashboard

The final Power BI dashboard includes:
- KPI cards for Total Sales, Total Purchase, Gross Profit, and Profit Margin %
- A donut chart of sales by shipping state
- Top Customers by Sales and Top Brands by Sales bar charts
- Sales by Gender comparison
- A month slicer (Jan–Dec) for time-based filtering
- A high-priority customer detail table with sales and purchase breakdown

## ▶️ How to Run This Project

```bash
# 1. Clone the repository
git clone https://github.com/priyesh7998/etl-ecommerce-sales-performance-analysis-python-sql-powerbi.git
cd etl-ecommerce-sales-performance-analysis-python-sql-powerbi

# 2. Set up the Python environment
pip install pandas numpy faker jupyter

# 3. Run the data cleaning & transformation notebook
jupyter notebook notebooks/etl_ecommerce_sales.ipynb

# 4. Load the transformed tables into SQL Server
#    Run the scripts in /sql/ to create tables and load the cleaned CSVs
#    (or use the SQL Server Import Wizard with the exported CSVs)

# 5. Run the analysis queries
#    Execute the queries in /sql/analysis_queries.sql

# 6. Open the dashboard
#    Open dashboard/Ecommerce_Seller_Dashboard.pbix in Power BI Desktop
#    and point the SQL Server data source to your local instance
```

## ✅ Results & Conclusion

This project delivers a fully reproducible pipeline that takes raw, messy,
multi-table e-commerce data and turns it into a single governed reporting
layer (the One Big Table) plus a live executive dashboard. It demonstrates
practical, job-ready skills across the analytics stack: Python data cleaning,
relational/dimensional data modeling, SQL Server database work, and Power BI
dashboard design — the same workflow used by data analysts and BI
developers in real e-commerce companies.

## 🔮 Future Work

- Build static/exploratory dashboards directly in Python using **Matplotlib
  and Seaborn** as a lightweight, code-based alternative to the BI tool
- Extend the Power BI dashboard with **MoM (Month-over-Month) sales** and
  **YoY / same-period-last-year comparisons** for trend tracking
- Extend the dashboard with cohort/retention analysis and return-rate trends
- Migrate the OBT build step into SQL Server stored procedures for
  in-database transformation
- Deploy the dashboard to the Power BI Service for scheduled refresh and
  stakeholder sharing

## 👤 Author

**Priyesh Kumar** <br>
Email : priyesh9080@gmail.com <br>
[Linkedin](https://linkedin.com/in/priyesh7998) <br>
[Portfolio](https://lukasha.online) <br>
[GitHub](https://github.com/priyesh7998) <br>

## 📁 Repository Contents

```
ETL-Ecommerce-Sales-Analysis-Python-SQL-PowerBI/
├── data/                  # Synthetic CSVs (customers, products, categories,
├── cleaned_data_for_analytics/   # Cleaned data & OBT(One Big Table) Of sales 
├── notebook/                  # Table creation scripts + analysis queries
├── dashboard/             # Power BI .pbix file
├── dashboard_img/        # Dashboard screenshots
└── README.md
```
