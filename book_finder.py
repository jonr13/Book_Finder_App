import operator
import csv
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
nyt_api_key1 = os.getenv("nyt_api_key")
rainforest_api1 = os.getenv("rainforest_api")

list_names = f"https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={nyt_api_key1}"
api_url = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={nyt_api_key1}"
def get_products(api_url):
    request_url = api_url
    response = requests.get(request_url)
    return json.loads(response.text)

def parse_json(api_url):
    response = requests.get(api_url)
    response_data = json.loads(response.text)
    return response_data

def read_date(date):
    date = str(date)
    day = date[-2:]
    if '0' in day:
        day = date[-1:]
    year = date[0: 4]
    month = date[5: 7]
    month_table = {'01':'Janurary', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
    month_name = month_table[month]
    return f"{month_name} {day}, {year}"

get_products(list_names)
nyt_list = parse_json(list_names)

nyt_list_names = []
nyt_list_info = {}
nyt_list_dict = {}
for item in nyt_list['results']:
    list_name = item['list_name']
    list_name_nyt = item['list_name_encoded']
    last_date = item['newest_published_date']
    last_updated = item['updated']
    string = f"List Name: {list_name}\nUpdated on: {last_date} Updated {last_updated}"
    nyt_list_names.append(list_name)
    nyt_list_dict[list_name] = list_name_nyt
    readable_date = read_date(last_date)
    nyt_list_info[item['list_name']] = f"The best seller list for {list_name} was last updated on {readable_date} and is typically updated {last_updated.lower()}."

#Print welcoming message to user with a description of the app
welcome_message = "\nWelcome to the Book Finder!\nIn this app you'll be able to search for a book by genre, browse best seller lists, and book purchasing options.\nAll in one place."
print(welcome_message)
#For this app you can indicate book genre, and we'll pull best selling from the NYT
prompt = "\nWhen you're ready to begin press enter.."
begin = input(prompt)
welcome_message2 = "\nLet's browse New York Times Best Seller Lists to find a book!\n"
print(welcome_message2)
#Allow the user to see what genres are available
#Prompt the user for book genre
#Print thank you, and print the genre selected
def list_browse():
    global genre
    global nyt_list_data_adj
    while True:
        prompt1 = "\nEnter in the genre of best seller list you want to browse (ex. 'Hardcover Fiction').\nIf you want to see a complete list of genres, enter 'show me'.\nEnter here: "
        genre = input(prompt1)
        if genre == 'show me':
            for lis in nyt_list_names:
                print(lis)
        elif genre in nyt_list_names:
            matching_genre = f"\nWe found a matching genre!\n{nyt_list_info[genre]}\n\nThe New York Times Top 5 Best Selling {genre} Books: \n"
            print(matching_genre)
            url_list = nyt_list_dict[genre]
            list_data_url = f"https://api.nytimes.com/svc/books/v3/lists/current/{url_list}.json?api-key=za7DPypRNtsNzAW8VGweJEJW6EHJJZSG"
            nyt_list_data = parse_json(list_data_url)
            nyt_list_data_adj = nyt_list_data['results']['books']
            break
        else:
            no_match = "   \nWe couldn't find a matching genre! Please try again"
            print(no_match)

list_browse()

#From NYT API, return a top 5 list of the best selling books within that genre for that timeframe

book_list = {}
read_list = {}

def add_books_to_list():
        prompt6 = "Enter in the book title here: "
        book_add = input(prompt6)
        prompt7 = "Enter the author here: "
        author_add = input(prompt7)
        read_list[book_add] = author_add
        add_statement = f"\n{book_add}, written by {author_add} has been added to the Read List!\n"
        print(add_statement)

def book_ranking():
    for book in nyt_list_data_adj:
        global book_list
        global author
        if book['rank'] <= 5:
            rank = book['rank']
            book_name = book['title']
            author = book['author']
            book_list[book_name] = author
            rank_statement = f"{rank}. {book_name}\nWritten by {author}\n"
            print(rank_statement)
        else:
            pass

book_ranking()

#Ask the user if he/she wants to see a book description
def book_description():
    for book in nyt_list_data_adj:
        if browse_or_read == book['title']:
            desc = book['description']
            description = f"\nDESCRIPTON: {desc}\n"
            print(description)
        else:
            pass

def more_options():
    while True:
        global browse_or_read
        prompt2 = "\nMore Actions Below:\n\n1. Would you like to see the description of a book to learn more? If so, enter the title of the book (ex. 'SULLY').\n2. Do you want to browse other book lists? If so, enter 'browse'.\n3. Do you want to add a book to your read list? If so, enter 'add'.\n \nIf you want to continue to Search on Amazon, type 'pass'.\n \nEnter here: "
        browse_or_read = input(prompt2)
        if browse_or_read =='browse':
            list_browse()
            book_ranking()
        elif browse_or_read == 'pass':
            break
        elif browse_or_read == 'add':
            add_books_to_list()
        elif browse_or_read in book_list:
            book_description()

def amazon_search_results(product_data):
    amz = product_data['search_results']
    print("\nTop 3 Amazon Search Results:")
    for a in amz:
        if a['position'] < 4:
            title = a['title']
            link = a['link']
            try: 
                rating = a['rating']
            except KeyError:
                rating = 'Rating not available'
            prime = ''
            if a['is_prime'] == True:
                prime += 'Yes'
            else:
                prime += 'No'
            prices = {}
            try:
                for l in a['prices']:
                    prices[l['name']] = l['raw']
            except KeyError:
                prices['Price Not Available'] = ''
            book_information = f"\n{title}\nAverage Rating: {rating}\nPrime Eligible: {prime}\nNavigate to Link: {link}\n   Price List:"
            print(book_information)
            for i in prices:
                price_statement = f"   {i.capitalize()} {prices[i]}"
                print(price_statement)

def search_books():
    while browse_or_read != 'done':
        prompt3 = "\nSearch and Finish Options: \n1. Would you like to search any book title on Amazon.com? If so, enter 'search'.\n2. Would you like to finish searching books? If so, enter 'done'.\n3. Would you like to continue to browse? If so, enter 'browse'.\nEnter here: "
        global search_book
        search_book = input(prompt3)
        if search_book == 'browse':
            list_browse()
            book_ranking()
            break
        elif search_book == 'done':
            if read_list:
                for read in read_list:
                    print(f"\nRead List:\n{read}, written by {read_list[read]}.\nWe're done finding books! Keep on reading!\n")
                break
            else:
                print("\nWe're done finding books! Keep on reading!")
                break
        elif search_book == 'search':
            prompt5 = "\nEnter Book Title here: "
            search_book_title = input(prompt5)
            prompt4 = "Enter Book Author here: "
            search_book_author = input(prompt4)
            search_book_title = search_book_title.replace(" ", "+")
            search_book_author = search_book_author.replace(" ", "+")
            search_term = f"{search_book_title}+{search_book_author}"
            amazon_url = f"https://api.rainforestapi.com/request?api_key={rainforest_api1}&type=search&amazon_domain=amazon.com&search_term={search_term}"
            get= get_products(amazon_url)
            amazon_search_results(get)
            break

def final_prompt():
    if search_book == 'done':
        print("\nThank you for using the book finder app! Have a great day!")
        pass 
    elif search_book != 'done':
        prompt_final = ("\nWould you like to continue to research books?\nIf so type 'yes', if no type 'done'.\nEnter here: ")
        final = input(prompt_final)
        if final == 'yes':
            more_options()
            search_books()
    else:
        print("\nThank you for using the book finder app! Have a great day!\n")

#Ask the user if he/she wants to see the book on amazon
#From Amazon API, pull in price and kindle format data
#If not on Amazon, print statement saying that not available on Amazon
#If possible, print the URL for purchase for all items on the list
while True:
    more_options()
    search_books()
    if search_book == 'done':
        break

final_prompt()

#Allow the user to browse books and search again if he/she chooses to
#End the program by printing the Read List and a thank you message

