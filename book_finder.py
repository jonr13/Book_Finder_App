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
    nyt_list_info[display_name] = f"{display_name} was last updated on {last_date} and is typically updated {last_updated.lower()}."


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
        break
    else:
        print("               ")
        print("We couldn't find a matching genre! Please try again")


#From NYT API, return a top 5 list of the best selling books within that genre for that timeframe

#Prompt the user to type in the names of the book they want to research

#From Amazon API, pull in price and kindle format data
#If not on Amazon, print statement saying that not available on Amazon

#If possible, print the URL for purchase for all items on the list
