"""<<<Welcome to Stack Overflow Question Scraper>>>"""

import requests
from bs4 import BeautifulSoup

def find_questions(base_url, page_limit):
    """Find questions based on tag and sort by criteria."""
    print('Starting crawling...')
    questions = []
    for page_no in range(1, page_limit+1):
        source_code = requests.get(f'{base_url}&page={page_no}').text
        soup = BeautifulSoup(source_code, 'html.parser')
        print(f'Crawling page {page_no}...')
        for question_link in soup.find_all('a', {'class': 'question-hyperlink'}):
            questions.append(question_link.get_text())
    return questions

if __name__ == '__main__':
    print(__doc__)
    
    tagged = input('Questions tagged? (eg: python) : ')
    
    permissible_sort_by_values = ('newest', 'featured', 'frequent', 'votes', 'active', 'unanswered')
    sort_by = input(f'Sort questions by? (permissible values: {"/".join(permissible_sort_by_values)}) : ')
    while sort_by.lower() not in permissible_sort_by_values:
        sort_by = input(f'Please select one among the permissible values.\nSort question by? (permissible values: {"/".join(permissible_sort_by_values)}) : ')

    page_limit = int(input('Enter no. of pages to crawl : '))

    questions = find_questions(f'http://stackoverflow.com/questions/tagged/{tagged}?sort={sort_by}', page_limit)

    if questions:    
        with open(f'{sort_by}_{tagged}_questions.txt', 'w', encoding="utf-8") as f:
            f.write('\n'.join(questions))
        print(f'\nResult saved to file {sort_by}_{tagged}_questions.txt')
    else:
        print('Looks like not a correct tag. No questions found for the query.')
