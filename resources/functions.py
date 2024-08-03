from datetime import datetime
import requests
import openpyxl
import os
import re


def subtract_months(date, months):
    # Subtracts a specified number of months from a date
    if months <= 1:
        return datetime(date.year, date.month, 1).date()

    new_month = date.month - (months - 1) % 12
    new_year = date.year - (months - 1) // 12

    # Adjust the year and month if subtraction crosses year boundary
    if new_month <= 0:
        new_month += 12
        new_year -= 1

    return datetime(new_year, new_month, 1).date()


def download_image(url, img_name):
    # Downloads an image from a URL and saves it to a local folder
    images_folder = "output/images"
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)

    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(images_folder, img_name)
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f'Image downloaded successfully: {img_name}')
    else:
        print(f'Failed to download image. Status code: {response.status_code}')


def count_search_phrase(text, phrase):
    # Counts occurrences of a search phrase within a text
    words = text.lower().split()
    phrase_words = phrase.lower().split()
    count = 0

    # Compare phrase with slices of text
    for i in range(len(words) - len(phrase_words) + 1):
        if words[i:i + len(phrase_words)] == phrase_words:
            count += 1

    return count


def verify_money(text1, text2):
    # Checks if money-related terms appear in either of two texts
    pattern = r'\$(\d+\.\d+|\d{1,3}(,\d{3})*(\.\d{2})?)|\d+\s(dollars|USD)'
    if re.search(pattern, text1) or re.search(pattern, text2):
        return True
    else:
        return False


def excel_file(data):
    # Creates an Excel file from a list of dictionaries containing result data
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    headers = ["Title", "Date", "Description", "Picture Filename", "Title Occurrences", "Description Occurrences",
               "Contains Money"]
    sheet.append(headers)

    for item in data:
        row_data = [
            item["title"],
            item["date"],
            item["description"],
            item["img_name"],
            item["search_phrases_in_title"],
            item["search_phrases_in_description"],
            item["contains_money"]
        ]

        sheet.append(row_data)

    workbook.save("output/result.xlsx")
    print("Excel file created.")