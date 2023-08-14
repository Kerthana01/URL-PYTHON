import string
import random
import sqlite3

# Set up a connection to the database
conn = sqlite3.connect('urls.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
             (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_url TEXT)''')
conn.commit()

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(original_url):
    short_url = generate_short_url()

    c.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
    conn.commit()

    return short_url

def get_original_url(short_url):
    c.execute("SELECT original_url FROM urls WHERE short_url=?", (short_url,))
    row = c.fetchone()
    if row:
        return row[0]
    else:
        return None

def main():
    print("URL Shortener")
    while True:
        print("\n1. Shorten URL")
        print("2. Get Original URL")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            original_url = input("Enter the original URL: ")
            short_url = shorten_url(original_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            original_url = get_original_url(short_url)
            if original_url:
                print(f"Original URL: {original_url}")
            else:
                print("Short URL not found.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    main()
