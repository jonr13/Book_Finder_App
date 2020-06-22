import operator
import csv
import requests
import json

list_names = "https://api.nytimes.com/svc/books/v3/lists/names.json?api-key=za7DPypRNtsNzAW8VGweJEJW6EHJJZSG"
api_url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=za7DPypRNtsNzAW8VGweJEJW6EHJJZSG"
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
for item in nyt_list['results']:
    display_name = item['display_name']
    last_date = item['newest_published_date']
    last_updated = item['updated']
    string = f"List Name: {display_name}\nUpdated on: {last_date} Updated {last_updated}"
    nyt_list_names.append(display_name)
    readable_date = read_date(last_date)
    nyt_list_info[display_name] = f"The best seller list for {display_name} was last updated on {readable_date} and is typically updated {last_updated.lower()}."


#Print welcoming message to user with a description of the app
print("               ")
print("Welcome to the Book Finder!\nIn this app you'll be able to search for a book by genre, browse best seller lists, and book purchasing options.\nAll in one place." )
#For this app you can indicate book genre, and we'll pull best selling from the NYT
print("               ")
prompt = "When you're ready to being, press enter.."
begin = input(prompt)
print("               ")
print("Let's browse New York Times Best Seller Lists to find a book!")
print("               ")


#Allow the user to see what genres are available
#Prompt the user for book genre
#Print thank you, and print the genre selected
genre = ''
def list_browse():
    global genre
    global nyt_list_data_adj
    while True:
        print("               ")
        prompt1 = "Enter in the genre of best seller list you want to browse (ex. 'Hardcover Fiction').\nIf you want to see a complete list of genres, enter 'show me'.\nEnter here: "
        genre = input(prompt1)
        if genre == 'show me' or genre == 'Show me' or genre == 'SHOW ME':
            for lis in nyt_list_names:
                print(lis)
        elif genre in nyt_list_names:
            print("               ")
            print("We found a matching genre!")
            print(nyt_list_info[genre])
            print("        ")
            print(f"The New York Times Top 5 Best Selleing {genre} Books: ")
            print("        ")
            list_data_url = f"https://api.nytimes.com/svc/books/v3/lists/current/{genre}.json?api-key=za7DPypRNtsNzAW8VGweJEJW6EHJJZSG"
            nyt_list_data = parse_json(list_data_url)
            nyt_list_data_adj = nyt_list_data['results']['books']
            break
        else:
            print("               ")
            print("We couldn't find a matching genre! Please try again")

list_browse()

#From NYT API, return a top 5 list of the best selling books within that genre for that timeframe

book_list = []
def book_ranking():
    for book in nyt_list_data_adj:
        global book_list
        if book['rank'] <= 5:
            rank = book['rank']
            book_name = book['title']
            book_list.append(book_name)
            author = book['author']
            print(f"{rank}. {book_name}\nWritten by {author} ")
            print("      ")
        else:
            pass

book_ranking()

#Ask the user if he/she wants to see a book description
def book_description():
    for book in nyt_list_data_adj:
        if browse_or_read == book['title']:
            desc = book['description']
            print("      ")
            print(f"DESCRIPTON: {desc}")
            print("      ")
        else:
            pass

while True:
    global browse_or_read
    prompt2 = "Enter the book title if want to see the description of a book.\nIf you want to browse other book lists, enter 'browse'!\nEnter here: "
    browse_or_read = input(prompt2)
    if browse_or_read =='browse':
        list_browse()
        book_ranking()
    elif browse_or_read in book_list:
        book_description()


#Ask the user if he/she wants to add a book to a list

#Ask the user if he/she wants to see the book on amazon

#From Amazon API, pull in price and kindle format data
#If not on Amazon, print statement saying that not available on Amazon

#If possible, print the URL for purchase for all items on the list