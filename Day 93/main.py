import requests
from bs4 import BeautifulSoup
import json
import csv
import time

# json web scraping from Realt.by

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
base_url = "https://realt.by/rent/flat-for-long/"
minsk = "%5B%7B%22townUuid%22%3A%224cb07174-7b00-11eb-8943-0cc47adabd66%22%7D%5D"

def build_url(rooms=None, price_from=None, price_to=None, has_images=False, page=1, map_polygons=None):
    # Choose base_url в зависимости от наличия mapPolygons
    if map_polygons:
        url = f"https://realt.by/belarus/rent/flat-for-long/?page={page}"
    else:
        url = f"https://realt.by/rent/flat-for-long/?addressV2={minsk}&page={page}"
    if has_images:
        url += "&hasImages=true"
    if rooms:
        for r in rooms:
            url += f"&rooms={r}"
    if price_from or price_to:
        url += "&priceType=840"
        if price_from:
            url += f"&priceFrom={price_from}"
        if price_to:
            url += f"&priceTo={price_to}"
    if map_polygons:
        url += f"&mapPolygons={map_polygons}"
    return url

def get_total_and_pages(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    total = None
    for p in soup.find_all("p"):
        if "объявлений" in p.text:
            b_tag = p.find("b")
            if b_tag:
                total = int(b_tag.text.strip())
                break
    if not total:
        print("Не удалось определить количество объявлений.")
        exit()
    per_page = 30
    pages = (total + per_page - 1) // per_page
    print(f"Всего найдено: {total} объявлений на {pages} страницах")
    return total, pages

def get_apartments(rooms=None, price_from=None, price_to=None, has_images=False, pages=1, map_polygons=None):
    all_apartments = []
    for page in range(1, pages + 1):
        url = build_url(rooms, price_from, price_to, has_images, page, map_polygons)
        print(f"Парсим страницу {page}: {url}")
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        script = soup.find("script", id="__NEXT_DATA__")
        data = json.loads(script.string)
        objects = data["props"]["pageProps"]["objects"]

        for obj in objects:
            apartment = {
                "address": obj.get("address", ""),
                "rooms": obj.get("rooms", ""),
                "price_usd": obj.get("priceRates", {}).get("840", ""),
                "price_byn": obj.get("priceRates", {}).get("933", ""),
                "area": obj.get("areaTotal", ""),
                "floor": f"{obj.get('storey', '')}/{obj.get('storeys', '')}",
                "description": obj.get("description",
 ""),
                "date": obj.get("updatedAt", obj.get("createdAt", "")),
                "link": f"https://realt.by/rent/flat-for-long/object/{obj.get('uuid', '')}"
            }
            all_apartments.append(apartment)
        time.sleep(1)
    return all_apartments

def save_csv(data, filename="apartments.csv"):
    if not data:
        print("Нет данных для сохранения!")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Сохранено {len(data)} квартир в {filename}")

# ====== Ввод фильтров ======
rooms_input = input("Введите номера комнат через запятую (например, 1,2) или оставьте пустым: ")
rooms = [int(r.strip()) for r in rooms_input.split(",") if r.strip()] if rooms_input else None

price_from_input = input("Минимальная цена (USD), если нужно: ")
price_from = int(price_from_input) if price_from_input else None

price_to_input = input("Максимальная цена (USD), если нужно: ")
price_to = int(price_to_input) if price_to_input else None

has_images_input = input("Только с фото? (y/n): ").strip().lower()
has_images = has_images_input == "y"

map_polygons = input("Вставьте значение mapPolygons из URL (или оставьте пустым): ")

# ====== Получение общего количества и страниц ======
url = build_url(rooms, price_from, price_to, has_images, page=1, map_polygons=map_polygons)
total, pages = get_total_and_pages(url)

# ====== Parsing ======
apartments = get_apartments(rooms, price_from, price_to, has_images, pages, map_polygons=map_polygons)
save_csv(apartments)

# ====== Check ======
for apt in apartments[:3]:
    print(apt)