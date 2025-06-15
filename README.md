# Webscrap
Web scraping is the automated process of extracting data from websites. Python is widely used for this purpose due to its simplicity and rich ecosystem of libraries. One of the most popular libraries for web scraping in Python is BeautifulSoup, which is used in combination with requests to fetch and parse HTML content.

## 📌 Project Overview
This project is a web scraping application designed to extract hotel details from [Booking.com](https://www.booking.com). It scrapes hotel information such as name, price, location, ratings, reviews, and booking links for any given city and date range, then saves the data as a CSV file in the local directory.

## 🎯 Objectives
1. **Automate Hotel Data Collection** – Extract key details from Booking.com efficiently.
2. **Flexible Scraping** – Allow users to input a URL and filename for custom searches.
3. **Data Storage** – Save extracted hotel details in a structured CSV format.
4. **Error Handling & Performance** – Implement sleep timers and request headers for smooth scraping.
5. **User-Friendly Execution** – Provide a seamless command-line experience for users.

## 🔧 Technologies & Libraries Used
- **Python 3.x**
- **BeautifulSoup4** – For parsing HTML and extracting hotel details.
- **Requests** – For sending HTTP requests to Booking.com.
- **CSV** – To store extracted data in a structured format.
- **LXML** – For fast and efficient HTML parsing.

## 📂 Features & Workflow
1. Users provide a **Booking.com search URL** and a **file name**.
2. The scraper **fetches** the page and extracts:
   - Hotel Name 🏨
   - Price 💰
   - Location 📍
   - Rating ⭐
   - Review Count 📝
   - Booking Link 🔗
3. The extracted data is **saved into a CSV file** in the local directory.
4. The program implements **random sleep intervals** to mimic human behavior and avoid blocking.

## 🚀 How to Run the Script
1. Install required dependencies:
   ```bash
   pip install beautifulsoup4 requests lxml
   ```
2. Run the script:
   ```bash
   python script.py
   ```
3. Enter the Booking.com **URL** and **file name** when prompted.
4. The data will be **scraped and saved** as a CSV file.

## 📌 Example Output (CSV Format)
```
hotel_name, locality, price, rating, score, review, link
"The Grand Hotel", "Mumbai, India", "₹5000", "4.5", "9.2", "1200 reviews", "https://booking.com/example"
...
```
Web scraping is the process of automatically extracting data from websites. Python is a popular language for web scraping due to its readability, ease of use, and powerful libraries. One of the most commonly used libraries for parsing HTML and extracting content is BeautifulSoup, often used in combination with the requests library.

BeautifulSoup is a Python library used to pull data out of HTML and XML files. It creates a parse tree for parsing HTML documents and makes it easy to search and navigate through the HTML structure.

>HOW IT WORKS:
____________________
Sending a Request:
The requests library is used to send an HTTP request to the target URL and retrieve the HTML content of the web page.

Parsing the HTML:
The HTML content returned is passed to BeautifulSoup to parse. BeautifulSoup provides methods to navigate and search through the HTML structure like DOM traversal.

Locating and Extracting Data:
BeautifulSoup allows you to extract specific data by targeting HTML tags, classes, ids, or attributes using functions like find(), find_all(), select(), etc.

Processing and Saving the Data:
The extracted data can be cleaned, formatted, and saved into files like CSV, Excel, or databases for further analysis.

>FEATURES OF BEAUTIFULSOUP:
___________________________
Simple syntax and easy to use for beginners.
Can parse broken or poorly formatted HTML.
Supports multiple parsers (html.parser, lxml, etc.).
Allows easy navigation and searching of the HTML tree.

>COMMON USE CASES:
______________________
Collecting product information from e-commerce websites.
Extracting job listings or resumes from career portals.
Scraping news articles and blog content.
Monitoring real-time data like stock prices, sports scores, etc.

>LIMITATIONS:
_________________
Cannot render or interact with JavaScript content (use Selenium or Playwright for that).
Slower than some advanced scraping frameworks like Scrapy for large-scale crawling.
Ethical and legal considerations: Always check a website’s robots.txt file and terms of service before scraping.
