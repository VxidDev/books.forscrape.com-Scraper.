# Book Scraper

A Python script that scrapes book data from [Books to Scrape](https://books.toscrape.com/) based on price and minimum rating filters. The scraped data is saved in a CSV file for easy analysis.  

---

## Features

- Scrapes book **title**, **price**, **availability**, **rating**, and **link**.
- Filter books by:
  - **Price limit** (in GBP)
  - **Minimum rating** (1–5 stars)
- Handles multiple pages automatically (up to 50 pages).
- Saves results in a clean CSV file (`results.csv`).
- Color-coded console output for better readability.

---

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `colorama`

Install dependencies with:

```bash
pip install requests beautifulsoup4 lxml colorama
```
## Usage

Clone the repository or download the script.

### Run the script:
```
python main.py
```
1. Enter the requested inputs:

2. Price limit in GBP (e.g., 20.00)

3. Minimum rating from 1 to 5 (e.g., 3)

4. Wait for the script to scrape the pages. Progress is shown in the console.

5. When finished, check results.csv for the filtered book data.

### Example Output (CSV)
```csv
A Light in the Attic , £51.77 , 3 / 5  , In stock , https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html](https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
```
### License

This project is open-source and free to use under the MIT License.
