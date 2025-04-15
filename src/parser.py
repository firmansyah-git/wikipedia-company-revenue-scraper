import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_html():
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_table(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all("table", class_="wikitable")[0]
    rows = table.find_all("tr")

    headers = [header.get_text(strip=True) for header in rows[0].find_all("th")]

    countries = []
    rowspans = []
    len_data = []

    for row_idx, row in enumerate(rows[2:]):
        tmp_data = []
        columns = row.find_all(['th', 'td'])

        col_cursor = 0
        for col in columns:
            while any(r['row_index'] == row_idx and r['col_index'] == col_cursor for r in rowspans):
                active = next(r for r in rowspans if r['row_index'] == row_idx and r['col_index'] == col_cursor)
                tmp_data.append(active['value'])
                if active['total_rows'] == 1:
                    rowspans.remove(active)
                else:
                    active['row_index'] += 1
                    active['total_rows'] -= 1
                col_cursor += 1

            if col.has_attr('data-sort-value'):
                value = col['data-sort-value']
            else:
                value = col.get_text(strip=True)

            tmp_data.append(value)

            if col.has_attr('rowspan'):
                rowspans.append({
                    'row_index': row_idx + 1,
                    'col_index': col_cursor,
                    'total_rows': int(col['rowspan']) - 1,
                    'value': value
                })

            col_cursor += 1

        if len(tmp_data) == len(headers):
            countries.append(tmp_data)
        else:
            print(f"[WARN] Skipped row {row_idx+2}: expected {len(headers)} columns, got {len(tmp_data)}")

    df = pd.DataFrame(countries, columns=headers)
    return df