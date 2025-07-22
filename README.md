# 📊 Blinkit Data Analytics Project

An end-to-end data analytics project analyzing Blinkit's operational data using **Python**, **SQL Server**, and **Power BI**. This project explores business insights from order, delivery, and customer datasets to help improve decision-making.

---

## 🔧 Tools & Technologies

* **Python**: `pandas`, `matplotlib`, `seaborn`, `python-dotenv`, `pyodbc`
* **SQL Server**: Data extraction and transformation via SQL queries
* **Power BI**: Dashboard creation and visual analytics

---

## ❓ Business Questions Answered

* What are the top 10 most ordered products?
* How does delivery time impact customer ratings?
* Which days and times see the highest order volumes?
* What are the top-performing cities by number of orders?
* Which delivery partners have the lowest average delivery time?
* What is the distribution of customer ratings?

---

## 📁 Folder Structure

```
Blinkit_Data_Analytics_Project/
├── data/                      # Raw CSVs
├── outputs/visuals/           # Python-generated charts
├── reports/                   # Power BI files
│   └── Blinkit Dashboard.pdf
├── src/                       # Modular Python scripts
│   ├── eda/
│   │   ├── load_data.py
│   │   ├── clean_transform.py
│   │   ├── eda.py
│   │   ├── visualizations.py
│   │   └── main_csv_analysis.py
│   └── sql_analytics/
│       ├── queries_sql.py
│       ├── query_runner.py
│       ├── eda_sql.py
│       ├── visualization_sql.py
│       └── main_sql_analysis.py
├── .env.example.txt           # Sample environment variables
├── requirements.txt           # Python dependencies
├── LICENSE                    # License information
└── README.md
```

---

## 🔐 Environment Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file based on `.env.example.txt`:

```env
SERVER=your_sql_server_instance
DATABASE=your_database_name
DRIVER=your_odbc_driver_name
```

---

## ▶️ How to Run the Project

### CSV-Based Analysis:

```bash
python src/eda/main_csv_analysis.py
```

### SQL-Based Analysis:

```bash
python src/sql_analytics/main_sql_analysis.py
```

Both scripts will:

* Load data
* Clean and transform datasets
* Run EDA and generate visualizations
* Save charts to `outputs/visuals/`

---

## 📈 Power BI Dashboard

Interactive dashboard developed in Power BI to visualize:

* Top Products
* Ratings Distribution
* City-Wise Orders
* Delivery Time Insights


---

## 🧰 Sample SQL Queries

```sql
-- Average delivery time by rating
SELECT rating, AVG(delivery_time) AS avg_time
FROM orders
GROUP BY rating;

-- Top 10 ordered products
SELECT product_name, COUNT(*) AS total_orders
FROM order_items
GROUP BY product_name
ORDER BY total_orders DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;
```

---

## 📊 Sample Output Charts (Python)

* `Top_10_Products.png`
* `Delivery_Time_vs_Rating.png`
* `Citywise_Avg_Delivery_Time.png`
* `Order_Count_By_City.png`

All charts saved to `outputs/visuals/`

---

## 📄 License

© 2025 Vimlesh Gupta. This project is open-source and available under the MIT License.  
You are free to use, modify, and distribute it with proper attribution.