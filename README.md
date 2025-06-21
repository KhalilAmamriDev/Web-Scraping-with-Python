# Web Scraping with Python – Wuzzuf Job Listings

This project demonstrates how to use Python for web scraping, specifically to collect job listings related to Python from [Wuzzuf.net](https://wuzzuf.net/). The script extracts job titles, company names, locations, skills, posting dates, and links, then saves the data into a CSV file.

## Features

- Scrapes multiple pages of job listings automatically
- Extracts key job information: title, company, location, skills, date, and link
- Saves the data in a CSV file for easy analysis
- Uses `requests` for HTTP requests and `BeautifulSoup` for HTML parsing

## Requirements

- Python 3.7 or higher
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `csv` (built-in)
  - `itertools` (built-in)

Install the required libraries with:

```bash
python -m pip install requests beautifulsoup4 lxml
```

## How It Works

1. The script sends HTTP requests to Wuzzuf’s job search page for Python jobs.
2. It parses the HTML content using BeautifulSoup and the lxml parser.
3. For each job listing, it extracts:
    - Job title
    - Company name
    - Location
    - Skills required
    - Posting date
    - Job link
4. The script loops through all available pages until there are no more jobs to scrape.
5. All collected data is saved to `jobstutorial.csv`.

## Usage

1. Clone this repository or download the script.
2. Make sure you have the required libraries installed.
3. Run the script:

```bash
python web_scraping.py
```

4. After running, check the `jobstutorial.csv` file for the results.

## Example Output

The output CSV file will look like this:

| Job Title                | Company Name | Date        | Location         | Job Skills                | Links                  |
|--------------------------|--------------|-------------|------------------|---------------------------|------------------------|
| Backend Engineer (Python)| Darsel       | 2 days ago  | Cairo, Egypt     | Python, backend, APIs ... | https://...            |
| ...                      | ...          | ...         | ...              | ...                       | ...                    |

## Notes

- This script is for educational purposes. Always respect website terms of service and robots.txt when scraping.
- The website structure may change, which could break the script. Update the selectors if needed.

## License

This project is open source and free to use for learning and non-commercial purposes.

---

Happy scraping! 🚀