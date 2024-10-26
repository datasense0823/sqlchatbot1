import pandas as pd
import sqlite3

# Load the CSV file into a DataFrame
csv_file_path = '/Users/fnusatvik/Desktop/genai_ds/bollywood_movie.csv'  # Replace with the actual path
df = pd.read_csv(csv_file_path)

# Connect to SQLite (creates a new database file if it doesn't exist)
conn = sqlite3.connect('bollywood_movies.db')
cursor = conn.cursor()

# Create a new table in SQLite to hold the movie data
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
    Title TEXT,
    Type TEXT,
    Release_Year INTEGER,
    Genre TEXT,
    Director TEXT,
    Production_House TEXT,
    Lead_Actors TEXT,
    Language TEXT,
    Budget_Millions REAL,
    Box_Office_Millions REAL,
    OTT_Platform TEXT,
    Runtime_Minutes INTEGER,
    No_of_Episodes INTEGER,
    IMDb_Rating REAL,
    Audience_Score INTEGER,
    Critics_Score INTEGER,
    Awards_Nominations INTEGER,
    Awards_Won INTEGER,
    Social_Media_Mentions INTEGER,
    User_Reviews_Count INTEGER,
    Viewership_Hours_Million REAL
)
''')

# Insert data from DataFrame into the SQLite table
df.to_sql('movies', conn, if_exists='replace', index=False)

# Commit changes
conn.commit()

# Sample Query: Retrieve top 5 movies with the highest IMDb rating
sample_query = '''
SELECT Title, IMDb_Rating, Audience_Score, Box_Office_Millions
FROM Movies
ORDER BY IMDb_Rating DESC
LIMIT 5
'''
# Execute the sample query
result = cursor.execute(sample_query).fetchall()

# Display the result
print("Top 5 Movies by IMDb Rating:")
for row in result:
    print(row)

# Close the connection
conn.close()
