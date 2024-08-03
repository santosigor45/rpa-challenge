# Web Scraping Automation - RPA Challenge

This project automates the process of web scraping to retrieve news articles based on specific search criteria. It uses the RPA Framework for browser automation, and it processes the results to generate a report in Excel format.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions and Classes](#functions-and-classes)
- [Customization](#customization)

## Features

- Opens a browser to a specified URL and performs a search for news articles.
- Selects specific categories of interest.
- Sorts the search results by the newest articles.
- Retrieves and processes news articles within a specified date range.
- Downloads images associated with news articles.
- Analyzes news content to count occurrences of search phrases and detect monetary references.
- Outputs the results into an Excel file.

## Installation

1. **Clone the Repository**
```
   git clone https://github.com/santosigor45/rpa-challenge.git
   cd rpa-challenge
```
2. **Install RCC command-line tool**
https://github.com/robocorp/rcc?tab=readme-ov-file#installing-rcc-from-the-command-line

3. **Setup Variables**
Ensure that the `Variables` and `Xpaths` modules are correctly configured with the necessary constants and XPath selectors.

## Usage
1. **Run the Script**
	Execute the main script to start the scraping process:
	```
	rcc run
	```
2. **Output**
-   Images downloaded from the articles are saved in the `output/images` directory.
-   The results are saved in an Excel file `output/result.xlsx`.

## Customization

-   **Search Criteria**: Update `Variables.SEARCH_TEXT` to change the search term.
-   **Date Range**: Modify `Variables.MONTHS` to adjust the date range for filtering articles.
-   **Categories**: Change `Variables.CATEGORIES` to select different categories during the search.
