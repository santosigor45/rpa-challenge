from robocorp import storage


class Variables:
    URL = "https://www.latimes.com/"

    SEARCH_PHRASE = storage.get_text("SEARCH_PHRASE")
    # SEARCH_PHRASE = "Brazil"

    MONTHS = int(storage.get_text("MONTHS"))
    # MONTHS = 2

    CATEGORIES = storage.get_text("CATEGORY").split(", ")
    # CATEGORIES = ["Soccer", "Sports"]
