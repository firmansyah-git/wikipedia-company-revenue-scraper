# wikipedia-company-revenue-scraper

# 🌍 Largest Companies by Revenue – Wikipedia Table Scraper

This project scrapes and parses the list of the world's largest companies by revenue from [Wikipedia](https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue), handling complex HTML structures such as `rowspan` and `data-sort-value` to build a clean and structured dataset.

---

## 🔍 Background

Wikipedia tables often include cells that span multiple rows (`rowspan`) or contain hidden values for sorting (`data-sort-value`). These make web scraping non-trivial and prone to misaligned data.

This project demonstrates how to accurately:
- Handle HTML table structures with `rowspan`
- Extract and normalize `data-sort-value` where applicable
- Construct a well-aligned, complete dataset with `pandas`

---

## 🛠️ Tech Stack

- Python 3
- BeautifulSoup (bs4)
- pandas
- requests (optional, if fetching live data)

---

## 🛠️ Requirements

Install required packages with:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
beautifulsoup4
pandas
requests
```

---

## 🚀 Usage
Run the scraper using:

```bash
python main.py
```

---

## 📁 Project Structure
```
largest-company-revenue-scraper/
├── main.py
├── src/
│   └── parser.py
├── requirements.txt
└── README.md
```


## 📊 Output Sample

| Rank | Company | Industry | Revenue | Profit | Employees | Country | State-Owned | Reference |
|------|---------|----------|---------|--------|-----------|---------|-------------|-----------|
| 1    | Walmart | Retail   | $680B   | $19B   | 2.1M      | USA     | No          | [1]       |

---

## 🔎 Key Implementation Details

- **Dynamic Insertion with Rowspan Handling**:  
  The script dynamically tracks cell positions affected by `rowspan` and inserts data into the correct column even when row-spanning cells are present.

- **Smart Column Alignment**:  
  Missing cells are filled based on historical context from previous rows.

- **Data Sorting Attribute Extraction**:  
  If a cell contains a `data-sort-value`, it’s used instead of the visible text, ensuring data consistency (e.g., with numbers and dates).

---

## 💡 Lessons Learned

- HTML tables on Wikipedia aren't straightforward; handling `rowspan` properly is essential for accuracy.
- Building a `rowspan memory` system (by tracking affected rows and columns) ensures reliable data integrity.
- `data-sort-value` can help us get cleaner raw data than what’s visually displayed.