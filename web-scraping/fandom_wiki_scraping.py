import cloudscraper
from bs4 import BeautifulSoup
import json

url = "https://genshin-impact.fandom.com/wiki/Character/List"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print("Page title:", soup.title.get_text(strip=True))

tables = soup.find_all("table")
character_table = tables[0]
rows = character_table.find_all("tr")

characters = []

def extract_quality(cell):
    text = cell.get_text(strip=True)
    if text:
        return text
    img = cell.find("img")
    if img and img.get("alt"):
        return img.get("alt").strip()
    if img and img.get("title"):
        return img.get("title").strip()
    return ""

for row in rows[1:]:
    cells = row.find_all(["td", "th"])

    if len(cells) >= 9:
        character = {
            "name": cells[1].get_text(strip=True),
            "quality": extract_quality(cells[2]),
            "element": cells[3].get_text(strip=True),
            "weapon": cells[4].get_text(strip=True),
            "region": cells[5].get_text(strip=True),
            "model_type": cells[6].get_text(strip=True),
            "release_date": cells[7].get_text(strip=True),
            "version": cells[8].get_text(strip=True)
        }
        characters.append(character)

print(f"Scraped {len(characters)} characters.\n")

for character in characters[:10]:
    print(character)

with open("genshin_characters.json", "w", encoding="utf-8") as f:
    json.dump(characters, f, ensure_ascii=False, indent=4)

print("\nSaved data to genshin_characters.json")