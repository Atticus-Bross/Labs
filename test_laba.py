"""Test Lab A:

Module testing the Lab A functions

Completed by Atticus Bross on 2024-11-12 for DS-1043"""
from typing import Callable

from laba import *

START:str = urljoin(DOMAIN, '/index.html')
EXAMPLE1:str = get(START).text
EXAMPLE2:str = get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html').text
EXAMPLE3: str = get('https://books.toscrape.com/catalogue/the-secret-garden_413/index.html').text
EXAMPLE4: str = get(
    'https://books.toscrape.com/catalogue/the-torch-is-passed-a-harding-family-story_945/index.html').text
EXAMPLE5: str = get(
    'https://books.toscrape.com/catalogue/foolproof-preserving-a-guide-to-small-batch-jams-jellies-pickles-condiments-and-more-a-foolproof-guide-to-making-small-batch-jams-jellies-pickles-condiments-and-more_978/index.html').text
SOUP1: Soup = Soup(EXAMPLE1, 'html.parser')
SOUP3: Soup = Soup(EXAMPLE3, 'html.parser')
SOUP4: Soup = Soup(EXAMPLE4, 'html.parser')
SOUP5: Soup = Soup(EXAMPLE5, 'html.parser')
TABLE3: element.Tag = SOUP3.find('table')
TABLE4: element.Tag = SOUP4.find('table')
TABLE5: element.Tag = SOUP5.find('table')
def test_error(error_type: type, f: Callable) -> None:
    """Tests if a function gives the correct error

    error_type: the type of error expected
    f: the function, should be specified as lambda: f(desired parameters)"""
    try:
        f()
        assert False
    except error_type:
        pass
def test_save_state()->None:
    """Tests the save_state function"""
    save_state('test.json',['abc','efg'],{'a':{},'b':{}})
    with open('test.json','r') as jsonfile:
        assert json.load(jsonfile) == [['abc','efg'],{'a':{},'b':{}}]
    save_state('test.json', ['abc'], {'a': {}})
    with open('test.json', 'r') as jsonfile:
        assert json.load(jsonfile) == [['abc'], {'a': {}}]
    save_state('test.json', [], {})
    with open('test.json', 'r') as jsonfile:
        assert json.load(jsonfile) == [[], {}]
    save_state('test.json', ['abc', 'efg'], {'a': {1:2,3:4}, 'b': {},'c':{1:2}})
    with open('test.json', 'r') as jsonfile:
        assert json.load(jsonfile) == [['abc', 'efg'], {'a': {'1':2,'3':4}, 'b': {},'c':{'1':2}}]
def test_load_state()->None:
    """Tests the save_state function"""
    save_state('test.json',['abc','efg'],{'a':{},'b':{}})
    assert load_state('test.json') == (['abc','efg'],{'a':{},'b':{}})
    save_state('test.json', ['abc'], {'a': {}})
    assert load_state('test.json') == (['abc'], {'a': {}})
    save_state('test.json', [], {})
    assert load_state('test.json') == ([], {})
    save_state('test.json', ['abc', 'efg'], {'a': {1:2,3:4}, 'b': {},'c':{1:2}})
    assert load_state('test.json') == (['abc', 'efg'], {'a': {'1':2,'3':4}, 'b': {},'c':{'1':2}})
def test_handle_link()->None:
    """Tests the handle_link function"""
    test_error(TimeoutError,lambda:handle_link([urljoin(START,'/asd')],1))
    assert handle_link([START])==(START, Soup(EXAMPLE1,'html.parser'))
    assert handle_link([START,'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'])==('https://books.toscrape.com/catalogue/category/books/travel_2/index.html',Soup(EXAMPLE2,'html.parser'))
    assert handle_link(['https://books.toscrape.com/catalogue/category/books/travel_2/index.html',START])==(START,Soup(EXAMPLE1,'html.parser'))


def test_rows() -> None:
    """Tests the rows function"""
    assert rows([1, 2], 1) == [[1, 2]]
    assert rows([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert rows([1, 2, 3, 4, 5, 6], 3) == [[1, 2], [3, 4], [5, 6]]
    assert rows([1, 2, 3, 4, 5, 6], 2) == [[1, 2, 3], [4, 5, 6]]


def test_extract_table() -> None:
    """Tests the extract_table function"""
    assert extract_table(TABLE3)[:3] == [['UPC', 'abbb492978ff656d'], ['Product Type', 'Books'],
                                         ['Price (excl. tax)', '£15.08']]
    assert extract_table(TABLE4)[4:7] == [['Tax', '£0.00'], ['Availability', 'In stock (16 available)'],
                                          ['Number of reviews', '0']]
    assert extract_table(TABLE5)[3] == ['Price (incl. tax)', '£30.52']


def test_extract_data() -> None:
    """Tests the extract_data function"""
    test3: dict = extract_data(SOUP3)
    assert test3['Title'] == 'The Secret Garden'
    assert test3['Category'] == 'Classics'
    assert test3['UPC'] == 'abbb492978ff656d'
    test4: dict = extract_data(SOUP4)
    assert test4['Title'] == 'The Torch Is Passed: A Harding Family Story'
    assert test4['Category'] == 'Add a comment'
    assert test4['Availability'] == 'In stock (16 available)'
    test5: dict = extract_data(SOUP5)
    assert test5[
               'Title'] == 'Foolproof Preserving: A Guide to Small Batch Jams, Jellies, Pickles, Condiments, and More: A Foolproof Guide to Making Small Batch Jams, Jellies, Pickles, Condiments, and More'
    assert test5['Category'] == 'Food and Drink'
    assert test5['Price (incl. tax)'] == '£30.52'
    assert len(test3) == len(test4) == len(test5) == 9
    assert test3.keys() == test4.keys() == test5.keys()


def test_update() -> None:
    """Tests the extract_update function"""
    data_test: dict[str, dict[str, Any]] = {}
    to_visit_test: list[str] = [START]
    link_test, soup_test = handle_link(to_visit_test)
    sub_data_test: dict = extract_data(soup_test)
    data_test[link_test] = sub_data_test
    update(link_test, to_visit_test, data_test, soup_test)
    assert sorted(to_visit_test) == sorted(
        ['http://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html',
         'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
         'http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html',
         'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
         'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html',
         'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
         'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
         'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
         'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
         'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
         'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
         'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
         'http://books.toscrape.com/catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html',
         'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
         'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
         'http://books.toscrape.com/catalogue/set-me-free_988/index.html',
         'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
         'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
         'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
         'http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html',
         'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
         'http://books.toscrape.com/catalogue/the-black-maria_991/index.html',
         'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
         'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
         'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
         'http://books.toscrape.com/catalogue/the-requiem-red_995/index.html',
         'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
         'http://books.toscrape.com/catalogue/category/books_1/index.html',
         'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
         'http://books.toscrape.com/catalogue/sharp-objects_997/index.html',
         'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html',
         'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
         'http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html',
         'http://books.toscrape.com/catalogue/olio_984/index.html', 'http://books.toscrape.com/catalogue/page-2.html',
         'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
         'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
         'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
         'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
         'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
         'http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html',
         'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
         'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
         'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
         'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
         'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
         'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
         'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
         'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
         'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
         'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
         'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
         'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html',
         'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
         'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
         'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
         'http://books.toscrape.com/catalogue/soumission_998/index.html',
         'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
         'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
         'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
         'http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html',
         'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
         'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
         'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
         'http://books.toscrape.com/catalogue/category/books/crime_51/index.html',
         'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
         'http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html',
         'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
         'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
         'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html',
         'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
         'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'])
    internal_test: Soup = Soup('<a href="#test">test</a><a href="#art">test</a><a href="#*&5uer45^)">tes</a>"',
                               'html.parser')
    update('test', to_visit_test, data_test, internal_test)
    assert sorted(to_visit_test) == sorted(
        ['http://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html',
         'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
         'http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html',
         'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
         'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html',
         'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
         'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
         'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
         'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
         'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
         'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
         'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
         'http://books.toscrape.com/catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html',
         'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
         'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
         'http://books.toscrape.com/catalogue/set-me-free_988/index.html',
         'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
         'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
         'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
         'http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html',
         'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
         'http://books.toscrape.com/catalogue/the-black-maria_991/index.html',
         'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
         'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
         'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
         'http://books.toscrape.com/catalogue/the-requiem-red_995/index.html',
         'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
         'http://books.toscrape.com/catalogue/category/books_1/index.html',
         'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
         'http://books.toscrape.com/catalogue/sharp-objects_997/index.html',
         'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html',
         'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
         'http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html',
         'http://books.toscrape.com/catalogue/olio_984/index.html', 'http://books.toscrape.com/catalogue/page-2.html',
         'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
         'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
         'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
         'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
         'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
         'http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html',
         'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
         'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
         'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
         'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
         'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
         'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
         'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
         'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
         'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
         'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
         'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
         'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html',
         'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
         'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
         'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
         'http://books.toscrape.com/catalogue/soumission_998/index.html',
         'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
         'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
         'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
         'http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html',
         'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
         'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
         'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
         'http://books.toscrape.com/catalogue/category/books/crime_51/index.html',
         'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
         'http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html',
         'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
         'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
         'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html',
         'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
         'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'])
    link_test, soup_test = handle_link(to_visit_test)
    sub_data_test: dict = extract_data(soup_test)
    data_test[link_test] = sub_data_test
    update(link_test, to_visit_test, data_test, soup_test)
    assert sorted(to_visit_test) == sorted(
        ['http://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html',
         'http://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html',
         'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
         'http://books.toscrape.com/catalogue/foolproof-preserving-a-guide-to-small-batch-jams-jellies-pickles-condiments-and-more-a-foolproof-guide-to-making-small-batch-jams-jellies-pickles-condiments-and-more_978/index.html',
         'http://books.toscrape.com/catalogue/americas-cradle-of-quarterbacks-western-pennsylvanias-football-factory-from-johnny-unitas-to-joe-montana_974/index.html',
         'http://books.toscrape.com/catalogue/sharp-objects_997/index.html',
         'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
         'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
         'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
         'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
         'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
         'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html',
         'http://books.toscrape.com/catalogue/category/books_1/index.html',
         'http://books.toscrape.com/catalogue/chase-me-paris-nights-2_977/index.html',
         'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
         'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
         'http://books.toscrape.com/catalogue/wall-and-piece_971/index.html',
         'http://books.toscrape.com/catalogue/the-four-agreements-a-practical-guide-to-personal-freedom_970/index.html',
         'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
         'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
         'http://books.toscrape.com/catalogue/in-her-wake_980/index.html',
         'http://books.toscrape.com/catalogue/page-1.html',
         'http://books.toscrape.com/catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html',
         'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
         'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
         'http://books.toscrape.com/catalogue/category/books/classics_6/index.html',
         'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html',
         'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
         'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
         'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
         'http://books.toscrape.com/catalogue/sophies-world_966/index.html',
         'http://books.toscrape.com/catalogue/soumission_998/index.html',
         'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
         'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
         'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
         'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html',
         'http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html',
         'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
         'http://books.toscrape.com/catalogue/behind-closed-doors_962/index.html',
         'http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html',
         'http://books.toscrape.com/catalogue/the-requiem-red_995/index.html',
         'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
         'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
         'http://books.toscrape.com/catalogue/birdsong-a-story-in-pictures_975/index.html',
         'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
         'http://books.toscrape.com/catalogue/the-bear-and-the-piano_967/index.html',
         'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
         'http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html',
         'http://books.toscrape.com/catalogue/the-five-love-languages-how-to-express-heartfelt-commitment-to-your-mate_969/index.html',
         'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
         'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
         'http://books.toscrape.com/catalogue/black-dust_976/index.html',
         'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
         'http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html',
         'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
         'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
         'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
         'http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html',
         'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
         'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
         'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
         'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
         'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
         'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
         'http://books.toscrape.com/catalogue/penny-maybe_965/index.html',
         'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
         'http://books.toscrape.com/catalogue/olio_984/index.html',
         'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
         'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
         'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
         'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
         'http://books.toscrape.com/catalogue/the-black-maria_991/index.html',
         'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
         'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
         'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
         'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
         'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
         'http://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html',
         'http://books.toscrape.com/catalogue/how-music-works_979/index.html',
         'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
         'http://books.toscrape.com/catalogue/you-cant-bury-them-all-poems_961/index.html',
         'http://books.toscrape.com/catalogue/aladdin-and-his-wonderful-lamp_973/index.html',
         'http://books.toscrape.com/catalogue/maude-1883-1993she-grew-up-with-the-country_964/index.html',
         'http://books.toscrape.com/catalogue/the-elephant-tree_968/index.html',
         'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
         'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
         'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
         'http://books.toscrape.com/catalogue/category/books/crime_51/index.html',
         'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html',
         'http://books.toscrape.com/catalogue/page-3.html',
         'http://books.toscrape.com/catalogue/set-me-free_988/index.html',
         'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
         'http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html'])
test_save_state()
test_load_state()
test_handle_link()
test_rows()
test_extract_table()
test_extract_data()
test_update()
