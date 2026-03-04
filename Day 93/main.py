import requests
import json
import re
import csv
from bs4 import BeautifulSoup
import time


def get_data(url):
    """Gets total count and list of apartments"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Total count
    total = 0
    for b in soup.find_all('b'):
        if b.text.isdigit():
            total = int(b.text)
            break

    # Apartments from JSON
    apartments = []
    match = re.search(r'"objects":\s*(\[.*?\])\s*,\s*"pagination"', response.text, re.DOTALL)
    if match:
        apartments = json.loads(match.group(1))

    return total, apartments


# === INPUT PARAMETERS ===

print("Выберите комнаты (от 1 до 6)")
print("Примеры: 1 или 1,2,3 (Enter - все)")
rooms_input = input("Комнаты: ").strip()

print("\nЦена в USD (Enter - пропустить)")
price_from = input("Цена от: ").strip()
price_to = input("Цена до: ").strip()

# === BUILD BASE URL ===

base_url = "https://realt.by/rent/flat-for-long/"
minsk_id = "%5B%7B%22townUuid%22%3A%224cb07174-7b00-11eb-8943-0cc47adabd66%22%7D%5D"

params = [f"addressV2={minsk_id}"]

if rooms_input:
    rooms = [r.strip() for r in rooms_input.split(",")]
    for r in rooms:
        params.append(f"rooms={r}")

if price_from:
    params.append(f"priceFrom={price_from}")
if price_to:
    params.append(f"priceTo={price_to}")
if price_from or price_to:
    params.append("priceType=840")

# === GET FIRST PAGE ===

first_url = f"{base_url}?{'&'.join(params)}&page=1"
total, apartments = get_data(first_url)

print(f"\n{'=' * 50}")
print(f"Всего объявлений: {total}")
print(f"{'=' * 50}")

all_apartments = apartments
pages = (total // 28) + 1  # ~28 ads per page

print(f"Страниц: {pages}")
print(f"Страница 1/{pages} - собрано {len(all_apartments)} объявлений")

# === PARSE REMAINING PAGES ===

for page in range(2, pages + 1):
    url = f"{base_url}?{'&'.join(params)}&page={page}"
    _, apartments = get_data(url)
    all_apartments.extend(apartments)
    print(f"Страница {page}/{pages} - собрано {len(all_apartments)} объявлений")
    time.sleep(0.5)  # Delay to avoid overloading the site

# === SAVE TO CSV ===

filename = "apartments.csv"

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Headers
    writer.writerow(['USD Price', 'Rooms', 'Square м²', 'Floor', 'Total floors', 'Address'])

    # Data
    for apt in all_apartments:
        writer.writerow([
            apt.get('priceRates', {}).get('840', 0),
            apt.get('rooms', ''),
            apt.get('areaTotal', ''),
            apt.get('storey', ''),
            apt.get('storeys', ''),
            apt.get('address', '')
        ])

print(f"\n{'=' * 50}")
print(f"✅ Done! Saved {len(all_apartments)} ads")
print(f"📁 File: {filename}")
print(f"{'=' * 50}")