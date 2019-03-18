## stackoverflow-qn-scraper
Scrapes questions from [Stack Overflow](https://stackoverflow.com) based on tag and search criteria.

*Now let's search all questions in SO programmatically*. All you need is to run the code, give input parameters and that's it.

**Note: This doesn't fetch answers to questions.**
# Input

1. **Tag**: The search results are not randomised. You can fetch questions tagged with any technology (example: python).

2. **Sorted by**: This criteria helps to fetch right questions.
   Various "sorted by" options available are:
   
   a. Newest

   b. Featured

   c. Frequent

   d. Votes

   e. Active

   f. Unanswered
      
3. **Page number**: This parameter asks to fetch all questions from specified number of pages. For example: Page number 2 means all questions from first two pages of SO are queried.

# Output

This code generates an output file in the same folder which holds all questions scraped. Tag for which no questions are found, the program reports that it fetched nothing and no file will be created.

# How To

1. Download or clone this repository to your local system.

2. Change directory to where you downloaded the file.

3. Open cmd/terminal in the same location and run `python SO_question_scraper.py`.

*Feel free to make any helpful tweaks!*
