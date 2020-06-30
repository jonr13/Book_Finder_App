# Book_Finder_App

Use the steps below to setup an Anaconda Virtual Environment:
1. conda create -n book-env python=3.7 # (first time only)
2. conda activate book-env

Use the steps below to install all packages used in the applications:
* Requests Package:
    1. pip install requests
* JSON Package:
    1. pip install json
* DOTENV Package:
    1. pip install python-dotenv
* OS MOdule:
    1. May not need to install, should alrady be installed with Python

To begin Application:
    1. Open the commanbd prompt on your computer
    2. Locate the directory where file 'book_finder.py' is saved.
    3. Type in the following python command: 'python book_finder.py'
    4. The application will then start - all following commands are not python specific

API Usage:
* The Best Read Discovery App is powered by the New York Times Books API and the Rainforest Amazon Product API

The following is a README file for the instructions on how to use the executive dashboard generator

Setup: The user should run "book_finder.py" to run the program

Steps:
1. The user is first welcomed to the Best Read Discovery App and prompted to press enter to proceeed.

2. Next, the user is then given the opportunity to browse best seller lists from the New York Times. The user has the option to
type in a genre or select 'show me' to see the genres available.
* If the user types in 'show me', a list of all available genres will appear. 
* Error checking: The user must type in the genre with the correct spelling or he/she will receive an error message.
* Error checking: If a genre is unavailable, the user will be notified.

3. When the user types in a valid genre, the user is notified that the genre is in fact valid:
    * The user then receives the top 5 best selling books from that genre, in order.

4. Next, the user has 3 additional options.
    Options:
    * The user can see a description of a book by entering the title of the book.
    * The user can browse other best seller lists by typing 'browse' and beginning step 2 again.
    * The user can add a book to the Read List by typing 'add' and entering the title and the author of the book
    * The user can also select pass, and skip on to searching a book no Amazon.com.

5. The Read List: The purpose of the Read List is to record book titles that may be interesting to the user for viewing once done using the application.

6. Next, after the user types in 'pass', the user can now search a book on Amazon.com for product price, ratings, etc.
    Options:
    * The user can search any book title on Amazon.com by entering 'search'
    * The user can browse other best seller lists by typing 'browse' and beginning step 2 again.
    * The user can skip to the end of the application by simply typing 'done'.

7. If the user enters 'search' to search Amazon.com, he/she must enter the title and the author to search.
    * After entering title and author information, the user then receives the top 3 Amazon search results.
    * Amazon search results contain title, average book rating, prime eligibility, the link to the page,
    and the different prices and format of the book.
    * After search results are given, the user is the given the options again from step 4.

8. As stated in step 7, the application will allow the user to start over from step 4 again with the following options listed below.
The options will continue on until the user indicates that he/she is done researching by typing in 'pass' in step 4 and 'done' in step 6.
Options:
    * The user can see a description of a book by entering the title of the book.
    * The user can browse other best seller lists by typing 'browse' and beginning step 2 again.
    * The user can add a book to the Read List by typing 'add' and entering the title and the author of the book
    * The user can also select pass, and skip on to searching a book no Amazon.com.

9. Search & Finish Options - after the user indicates 'pass' in step 4 and 'done in step 6, he/she will be given a final set of options below:
    Options:
    * Search a book title again on Amazon.com by selecting 'search'.
    * Enter 'done' to finish researching and end the application.
    * Enter 'browse' to browse more books.

10. Search & Finish Respnses:
    * If the user enters 'search', step 7 will be repeated so the user can search more books on Amazon.com.
    * If the users enters 'browse', step 2 will be repeated so the user can browse best seller lists from the New York Times.
    * If the user enters 'done', The application will end with a Thank You message and the Read List will be printed.
    