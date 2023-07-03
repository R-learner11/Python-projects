from bs4 import BeautifulSoup
import requests

# In this project i am will be scraping data from web and creating a list og 50 must watch movies as given by imdb.com

response = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
movies_data = response.text
soup = BeautifulSoup(response.text, "html.parser")

movie_numbers = soup.find_all(name='span', class_="lister-item-index unbold text-primary")

# list comprehension
movie_number_list = [numbers.getText() for numbers in movie_numbers]

movie_name_span = soup.find_all(name='h3', class_="lister-item-header")

# list comprehension
movies_name_list = [movie.a.getText() for movie in movie_name_span]

movies_list = [number+name for number,name in zip(movie_number_list, movies_name_list)]
print(movies_list)

with open('movies.txt', mode='w') as file:
    for movies in movies_list:
        file.write(f"{movies}\n")



