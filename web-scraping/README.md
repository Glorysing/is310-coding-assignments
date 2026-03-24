# Fandom Wikis and Web Scraping Homework

## Overview

For this assignment, I chose to scrape the Genshin Impact Fandom Wiki. I selected the Character List page because it provides structured information about playable characters in the game, including their names, quality, element, weapon type, region, model type, release date, and game version.

I chose this wiki because Genshin Impact is a major global game with a large fan community, and its fandom wiki is an important example of how fan communities organize, document, and maintain cultural knowledge online. The character list is especially useful because it turns game information into a structured dataset that can be used for analysis.

## What I Scraped

I scraped data from the following page:

- Character List: https://genshin-impact.fandom.com/wiki/Character/List

The dataset includes the following fields for each playable character:

- name
- quality
- element
- weapon
- region
- model_type
- release_date
- version

The scraped data is saved in:

- `genshin_characters.json`

## Why This Data Matters

This data could be useful to researchers interested in digital humanities, game studies, fandom, and online knowledge production. For example, researchers could use this dataset to study:

- how game characters are categorized and presented in fan communities
- how fandom wikis transform game content into structured data
- patterns in character design across region, element, or weapon type
- how game updates introduce new characters over time

This kind of data can also support future analysis of representation, classification, and the ways fan communities document popular media.

## Scraping Ethics and Site Policy

Before scraping the site, I checked the website's `robots.txt` file to make sure I was reviewing the site's scraping rules.

- robots.txt: https://genshin-impact.fandom.com/robots.txt

This assignment only scraped publicly available information from a fandom wiki page and stored it in a small JSON file for educational use.

## Tools Used

This project uses:

- `cloudscraper` to request the webpage
- `BeautifulSoup` from `bs4` to parse the HTML
- Python's built-in `json` library to save the scraped data

## How to Run the Script

1. Navigate to the `web-scraping` directory.
2. Install the required libraries:

```bash
pip install cloudscraper beautifulsoup4
```
3. Run the script: python fandom_wiki_scraping.py

## Output

Running the script creates the following output file:

- genshin_characters.json

Files in This Folder:

- fandom_wiki_scraping.py — the Python script used to scrape the wiki
- genshin_characters.json — the scraped dataset
- README.md — explanation of the project and scraping process