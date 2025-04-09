import sqlite3

# Connect to pets.db
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# Insert persons
persons = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?);", persons)

# Insert pets
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?);", pets)

# Insert person-pet relationships
person_pet = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

cursor.executemany("INSERT INTO person_pet VALUES (?, ?);", person_pet)

# Commit and close
conn.commit()
conn.close()
