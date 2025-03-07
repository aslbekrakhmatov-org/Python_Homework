from bs4 import BeautifulSoup
import sqlite3
import requests
url = "https://realpython.github.io/fake-jobs/"
with sqlite3.connect("jobs.db") as connection:
    cursor = connection.cursor()
    query1 = ('''CREATE TABLE IF NOT EXISTS Vacancies
            (
            'Job_Title' TEXT,
            'Company_Name' TEXT,
            'Location' TEXT,
            'Description' TEXT,
            'Application_Link' TEXT,
            UNIQUE(Job_Title, Company_Name, Location)
            )
    ''')
    cursor.execute(query1)
    connection.commit()

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
vacancies_data = []
cards = soup.find_all("div", class_="card-content")
for card in cards:
    job_title = card.find("h2", class_="title is-5").text.strip()
    comp = card.find("h3", class_="subtitle is-6 company").text.strip()
    location = card.find("p", class_= "location").text.strip()
    apply_link = card.find("a", string="Apply").get("href")
    description = card.find("div", class_="content").text.strip()
    vacancies_data.append((job_title, comp, location, description, apply_link))

with sqlite3.connect("jobs.db") as con:
    cursor = con.cursor()
    query2 = ('''INSERT INTO Vacancies ('Job_Title', 'Company_Name', 'Location','Description', 'Application_Link') VALUES(?,?,?,?,?)''')
    cursor.executemany(query2, vacancies_data)

for job in vacancies_data:
    job_title, comp, location, description, apply_link = job

    cursor.execute('''
        INSERT OR IGNORE INTO Vacancies (Job_Title, Company_Name, Location, Description, Application_Link) 
        VALUES (?, ?, ?, ?, ?)
    ''', (job_title, comp, location, description, apply_link))

    cursor.execute('''
        UPDATE Vacancies
        SET Description = ?, Application_Link = ?
        WHERE Job_Title = ? AND Company_Name = ? AND Location = ?
    ''', (description, apply_link, job_title, comp, location))