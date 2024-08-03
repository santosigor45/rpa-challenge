from robocorp import storage


class Variables:
    URL = "https://www.latimes.com/"

    # SEARCH_TEXT = storage.get_text("SEARCH_PHRASE")
    SEARCH_TEXT = "Messi"

    # MONTHS = int(storage.get_text("MONTHS"))
    MONTHS = 3

    # CATEGORY = storage.get_text("CATEGORY").split(", ")
    CATEGORIES = ["Soccer", "Sports"]
