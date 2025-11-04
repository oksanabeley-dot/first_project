#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# """
# top100_zodiac.py
# Скрипт: бере топ-100 ATP (live), витягує дати народження гравців, визначає знак зодіаку,
# записує CSV і малює графік частотності.
# Примітка: може потребувати доопрацювання під структуру сайту (JS), або Selenium.
# """

import time
import csv
import re
from collections import Counter
from datetime import datetime
from typing import Optional

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# ---- Налаштування ----
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Top100ZodiacBot/1.0; +https://example.com/bot)"
}
SLEEP_BETWEEN_REQUESTS = 1.0  # сек (поважний інтервал)
OUTPUT_CSV = "top100_birthdays.csv"
OUTPUT_PLOT = "zodiac_counts.png"

# ---- Функції ----
def zodiac_sign(day: int, month: int) -> str:
    # Повертає українську назву знаку
    z = [
        ((1, 20), (2, 18), "Водолій"),
        ((2, 19), (3, 20), "Риби"),
        ((3, 21), (4, 19), "Овен"),
        ((4, 20), (5, 20), "Телець"),
        ((5, 21), (6, 20), "Близнюки"),
        ((6, 21), (7, 22), "Рак"),
        ((7, 23), (8, 22), "Лев"),
        ((8, 23), (9, 22), "Діва"),
        ((9, 23), (10, 22), "Терези"),
        ((10, 23), (11, 21), "Скорпіон"),
        ((11, 22), (12, 21), "Стрілець"),
        ((12, 22), (1, 19), "Козеріг"),
    ]
    for start, end, name in z:
        sm, sd = start
        em, ed = end
        if sm < em:
            if (month == sm and day >= sd) or (month == em and day <= ed) or (sm < month < em):
                return name
        else:  # період через рік (Козеріг: 22.12 - 19.01)
            if (month == sm and day >= sd) or (month == em and day <= ed) or (month > sm or month < em):
                return name
    return "Невідомо"

def parse_atp_top100() -> list:
    """
    Повертає список словників: [{'rank':1, 'name':'Carlos Alcaraz', 'profile_url': '...', 'country': 'ESP'}, ...]
    Спроба парсити офіційну сторінку ATP live/top-100. Може потребувати оновлення під HTML.
    """
    url = "https://www.atptour.com/en/rankings/singles"
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    players = []
    # Спроба знайти рядки таблиці — структура сайту може змінюватись
    # Шукаємо по CSS-класах, що часто використовуються: .player-cell, .rank-cell, a[href*="/en/players/"]
    rows = soup.select("tr")
    for row in rows:
        # знайти посилання на профіль
        a = row.find("a", href=re.compile(r"/en/players/"))
        rank_td = row.find("td", class_=re.compile("rank"))
        if a and rank_td:
            name = a.get_text(strip=True)
            profile_url = "https://www.atptour.com" + a['href']
            # витягнути ранг
            rank_text = rank_td.get_text(strip=True)
            try:
                rank = int(re.sub(r"\D", "", rank_text))
            except:
                rank = None
            country_td = row.find("td", class_=re.compile("country"))
            country = country_td['data-country-code'] if country_td and country_td.has_attr('data-country-code') else None
            players.append({'rank': rank, 'name': name, 'profile_url': profile_url, 'country': country})
            if len(players) >= 100:
                break
    # Якщо парсинг не вдалий (порожній), можна спробувати інші джерела (ESPN, live-tennis)
    return players

def extract_dob_from_atp_profile(profile_url: str) -> Optional[str]:
    """Повертає дату у форматі YYYY-MM-DD або None."""
    try:
        r = requests.get(profile_url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        # На сторінці ATP дата часто у блоці bio, наприклад: <div class="table-birthday">22 May 1987</div>
        # Зробимо гнучкий пошук
        text = soup.get_text(separator=" ", strip=True)
        # Витягнемо перший збіг дати формату '22 May 1987' або 'May 22, 1987' або '22/05/1987'
        m = re.search(r'(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{4})', text, re.IGNORECASE)
        if m:
            day = int(m.group(1))
            mon_str = m.group(2)
            year = int(m.group(3))
            month = datetime.strptime(mon_str[:3], "%b").month
            return f"{year:04d}-{month:02d}-{day:02d}"
        # інші формати:
        m2 = re.search(r'([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})', text)
        if m2:
            mon = m2.group(1)
            day = int(m2.group(2))
            year = int(m2.group(3))
            month = datetime.strptime(mon[:3], "%b").month
            return f"{year:04d}-{month:02d}-{day:02d}"
        # цифрові формати dd/mm/yyyy або yyyy-mm-dd
        m3 = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)
        if m3:
            return f"{m3.group(1)}-{m3.group(2)}-{m3.group(3)}"
        m4 = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', text)
        if m4:
            day = int(m4.group(1)); month = int(m4.group(2)); year = int(m4.group(3))
            return f"{year:04d}-{month:02d}-{day:02d}"
    except Exception as e:
        # print("Error fetching profile:", e)
        return None
    return None

def extract_dob_wikipedia(name: str) -> Optional[str]:
    """Проста спроба витягти DOB із Wikipedia (англ)."""
    try:
        search_url = "https://en.wikipedia.org/wiki/" + name.replace(" ", "_")
        r = requests.get(search_url, headers=HEADERS, timeout=15)
        if r.status_code != 200:
            return None
        soup = BeautifulSoup(r.text, "html.parser")
        # дата в інфобоксі: <span class="bday">1987-05-22</span>
        b = soup.find("span", class_="bday")
        if b:
            return b.get_text(strip=True)
        # інакші варіанти: пошук за текстом "Born"
        txt = soup.get_text(" ", strip=True)
        m = re.search(r'born\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})', txt, re.IGNORECASE)
        if m:
            dt = datetime.strptime(m.group(1), "%d %B %Y")
            return dt.strftime("%Y-%m-%d")
    except Exception:
        return None
    return None

# ---- Основна логіка ----
def main():
    print("Парсінг списку топ-100 (спроба з ATP)...")
    players = parse_atp_top100()
    if not players:
        print("Не вдалося отримати список з ATP. Будь ласка, перевір сайт або використай запасне джерело.")
        return

    results = []
    for i, p in enumerate(players, start=1):
        name = p['name']
        profile = p.get('profile_url')
        dob = None
        source = None
        if profile:
            dob = extract_dob_from_atp_profile(profile)
            if dob:
                source = "ATP profile"
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        if not dob:
            # запасний варіант: Wikipedia
            dob = extract_dob_wikipedia(name)
            if dob:
                source = "Wikipedia"
        # якщо знайшли дату — розберемо в день/місяць/рік і знак
        zodiac = None
        if dob:
            try:
                dt = datetime.strptime(dob, "%Y-%m-%d")
                zodiac = zodiac_sign(dt.day, dt.month)
            except Exception:
                zodiac = "Невідомо"
        results.append({
            "rank": p.get('rank'),
            "name": name,
            "country": p.get('country'),
            "profile_url": profile,
            "dob": dob,
            "zodiac": zodiac,
            "source": source
        })
        print(f"{i:3d}. {name} | dob: {dob} | zodiac: {zodiac} | src: {source}")

    # Зберегти CSV
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')
    print(f"CSV збережено у: {OUTPUT_CSV}")

    # Порахувати частоти та побудувати графік
    counts = Counter([r['zodiac'] or "Невідомо" for r in results])
    # Перетворимо у DataFrame для зручності
    cdf = pd.DataFrame(sorted(counts.items(), key=lambda x: x[1], reverse=True), columns=['zodiac','count'])
    print("\nСтатистика по знаках:")
    print(cdf.to_string(index=False))

    # Малюємо графік
    plt.figure(figsize=(10,6))
    plt.bar(cdf['zodiac'], cdf['count'])
    plt.xlabel("Знак зодіаку")
    plt.ylabel("Кількість гравців")
    plt.title("Знаки зодіаку серед топ-100 ATP")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(OUTPUT_PLOT, dpi=150)
    print(f"Графік збережено у: {OUTPUT_PLOT}")
    plt.close()

if __name__ == "__main__":
    main()


