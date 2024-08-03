class Xpaths:
    class Home:
        BUTTON_SEARCH = "//button[@data-element='search-button']"
        INPUT_SEARCH = "//input[@data-element='search-form-input']"
        BUTTON_SUBMIT = "//button[@data-element='search-submit-button']"

    class NewsPage:
        SPAN_SHOW_CATEGORIES = "//span[@class='see-all-text']"
        SELECT_SORT = "//select[@name='s']"
        UL_RESULTS = "//ul[@class='search-results-module-results-menu']/li"
        DIV_NEXT_PAGE = "//div[@class='search-results-module-next-page']"

    class Result:
        DATE = "p[@class='promo-timestamp']"
        TITLE = "h3[@class='promo-title']/a"
        DESCRIPTION = "p[@class='promo-description']"
        PICTURE = "img[@class='image']"
