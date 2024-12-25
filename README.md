# Web Scraping: Flipkart Smartphones Data

## Project Description
This project involves web scraping to extract smartphone data from Flipkart. The dataset includes details such as brand, model, price, specifications, ratings, and reviews. This repository contains the scripts used for scraping the data, the cleaned dataset, and exploratory analysis to provide insights into the smartphone market.

## Technologies Used
- **Python**: The main programming language used to implement the web scraping and data processing.
- **BeautifulSoup**: A Python library used for parsing HTML and extracting relevant data from Flipkart’s website.
- **Requests**: A Python library for sending HTTP requests to retrieve the web pages for scraping.
- **OS**: The `os` module is used to handle file and directory operations during the scraping process.

## Features
- **Data Extraction**: Extracts data such as brand, model, price, specifications, ratings, and reviews from smartphone product pages on Flipkart.
- **JSON File**: The cleaned data is stored in a JSON file for further analysis.

## Installation

### Prerequisites
Make sure you have the following libraries installed:
- `requests`
- `beautifulsoup4`
- `pandas` (for data cleaning and analysis)

You can install them using pip:
```bash
pip install requests beautifulsoup4 pandas
