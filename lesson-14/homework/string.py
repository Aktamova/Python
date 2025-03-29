Homework JSON and Requests
Task: JSON Parsing
write a Python script that reads the students.jon JSON file and prints details of each student.
import json

# Load JSON data from file
def read_students_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            students = json.load(file)
            
            # Print student details
            for student in students:
                print(f"Name: {student.get('name', 'N/A')}")
                print(f"Age: {student.get('age', 'N/A')}")
                print(f"Grade: {student.get('grade', 'N/A')}")
                print(f"Subjects: {', '.join(student.get('subjects', []))}")
                print("-" * 30)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

# Specify the JSON file name
filename = "students.json"
read_students_json(filename)

Task: Weather API
Use this url : https://openweathermap.org/
Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests

def get_weather(city):
    base_url = "https://samples.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": "b6907d289e10d714a6e88b30761fae22", "units": "metric"}  
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        weather_data = response.json()
        
        city_name = weather_data.get("name", "N/A")
        temperature = weather_data["main"].get("temp", "N/A")
        humidity = weather_data["main"].get("humidity", "N/A")
        weather_description = weather_data["weather"][0].get("description", "N/A")
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

# Get weather data for Tashkent
city = input("Which city do you need: ")
get_weather(city)
Task: JSON Modification
Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
import json

# Function to load books from JSON file
def load_books(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save books to JSON file
def save_books(filename, books):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=4)

# Function to add a new book
def add_book(filename):
    books = load_books(filename)
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    books.append({"title": title, "author": author, "year": year})
    save_books(filename, books)
    print("Book added successfully!")

# Function to update a book
def update_book(filename):
    books = load_books(filename)
    title = input("Enter title of the book to update: ")
    for book in books:
        if book['title'].lower() == title.lower():
            book['author'] = input("Enter new author (or press Enter to keep current): ") or book['author']
            book['year'] = input("Enter new year (or press Enter to keep current): ") or book['year']
            save_books(filename, books)
            print("Book updated successfully!")
            return
    print("Book not found!")

# Function to delete a book
def delete_book(filename):
    books = load_books(filename)
    title = input("Enter title of the book to delete: ")
    books = [book for book in books if book['title'].lower() != title.lower()]
    save_books(filename, books)
    print("Book deleted successfully!")

# Main program loop
def main():
    filename = "books.json"
    while True:
        print("\nOptions:")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_book(filename)
        elif choice == '2':
            update_book(filename)
        elif choice == '3':
            delete_book(filename)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

import requests
import random

def get_movie_recommendation(genre):
    api_key = "your_api_key_here"  # Replace with your OMDB API key
    base_url = "http://www.omdbapi.com/"

       
    # Example list of movies per genre (since OMDB does not support direct genre-based search)
    genre_movies = {
        "action": ["Mad Max: Fury Road", "Gladiator", "Die Hard"],
        "comedy": ["Superbad", "Step Brothers", "The Hangover"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club"],
        "horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out"],
        "sci-fi": ["Interstellar", "Inception", "The Matrix"]
    }
    
    if genre.lower() not in genre_movies:
        print("Sorry, we don't have recommendations for this genre.")
        return
    
    movie_title = random.choice(genre_movies[genre.lower()])
    params = {"t": movie_title, "apikey": api_key}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        movie_data = response.json()
        
        if movie_data["Response"] == "True":
            print(f"\nRecommended Movie: {movie_data['Title']}")
            print(f"Year: {movie_data['Year']}")
            print(f"Genre: {movie_data['Genre']}")
            print(f"Plot: {movie_data['Plot']}")
            print(f"IMDb Rating: {movie_data['imdbRating']}")
        else:
            print("Movie not found.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie data: {e}")

# Get user input and recommend a movie
genre = input("Enter a movie genre (Action, Comedy, Drama, Horror, Sci-Fi): ")
get_movie_recommendation(genre)
