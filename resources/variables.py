from RPA.Robocorp.WorkItems import WorkItems


class Variables:
    URL = "https://www.latimes.com/"

    library = WorkItems()
    library.get_input_work_item()
    variables = library.get_work_item_variables()

    SEARCH_PHRASE = variables["SEARCH_PHRASE"]

    MONTHS = int(variables["MONTHS"])

    CATEGORIES = variables["CATEGORIES"].split(", ")
