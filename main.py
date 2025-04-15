from src.parser import fetch_html, parse_table

if __name__ == "__main__":
    html = fetch_html()
    df = parse_table(html)
    print(df.head())
    # df.to_csv("largest_companies_by_revenue.csv", index=False)
    # print("\n✅ Data berhasil disimpan ke 'largest_companies_by_revenue.csv'")
