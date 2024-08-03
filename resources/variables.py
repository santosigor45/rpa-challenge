from robocorp import storage


class Variables:
    URL = "https://www.latimes.com/"

    SEARCH_TEXT = storage.get_text("SEARCH_PHRASE")
    # SEARCH_TEXT = "Brazil"

    MONTHS = int(storage.get_text("MONTHS"))
    # MONTHS = 2

    CATEGORIES = storage.get_text("CATEGORY").split(", ")
    # CATEGORIES = ["Soccer", "Sports"]
