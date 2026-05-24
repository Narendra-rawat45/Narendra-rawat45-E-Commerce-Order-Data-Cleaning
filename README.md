# Narendra-rawat45-E-Commerce-Order-Data-Cleaning
🛒 E-Commerce Order Data Cleaning — Pandas
This project focuses on cleaning a raw e-commerce order dataset using Python and the Pandas library. The dataset contains orders from October 2025, including returns, RTO (Return to Origin) cases, and incomplete entries.

📁 Dataset Overview
ColumnDescriptionOrder IDUnique order identifier (e.g. ORID00001)SKU IDStock Keeping Unit IDArticle IDArticle/product identifierOrder DateDate when the order was placedOrder MonthMonth of the orderQuantityQuantity orderedReturn QtyQuantity returnedNet QtyActual delivered quantity (Quantity - Return Qty)Net SalesActual sales amount after returns (₹)Gross SalesTotal sales amount before returns (₹)Return ReasonReason for return (RTO / Return / blank)StatusOrder status (C = Completed, F = Fulfilled, RTO = Return to Origin)
Total Records: 37000+ orders 

🧹 Data Cleaning Steps
The following steps were performed using Pandas:

Standardizing Column Names — Replaced spaces with underscores and converted to lowercase
Fixing Date Columns — Converted Order Date and Order Month to proper datetime format
Handling Missing Values — Identified null values in Return Reason and Status columns
Correcting Data Types — Ensured numeric columns (Net Sales, Gross Sales) are in float format
Checking for Duplicates — Checked for duplicate entries based on Order ID
Separating Return vs Non-Return Orders — Filtered orders using Return Qty > 0
Net Sales Validation — Verified that orders with Return Qty = 1 have zero Net Sales


🛠️ Tech Stack

Language: Python 3.x
Library: Pandas
Environment: Jupyter Notebook / VS Code


🚀 How to Run
bash# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Install dependencies
pip install pandas

# 3. Run the script
python data_cleaning.py

📊 Key Insights (Post Cleaning)

Total Gross Sales: 47.5M+ (approx.)
Return Orders: 20+ orders returned (RTO + Customer Returns)
RTO Cases: Several orders were sent back before delivery
Most Active Period: Higher order volume observed in early October


📂 Project Structure
📦 your-repo-name
 ┣ 📄 data_cleaning.py       # Main cleaning script
 ┣ 📄 raw_data.csv           # Original dataset
 ┣ 📄 cleaned_data.csv       # Cleaned output file
 ┗ 📄 README.md              # This file

🤝 Contributing
Pull requests are welcome! Feel free to open an issue for any suggestions or improvements.
