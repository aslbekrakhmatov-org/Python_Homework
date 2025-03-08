from bs4 import BeautifulSoup
import sqlite3
import requests
import csv

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
    description = " ".join(card.find("div", class_="content").text.split())
    vacancies_data.append((job_title, comp, location, description, apply_link))

with sqlite3.connect("jobs.db") as con:
    cursor = con.cursor()
    query2 = '''
    INSERT OR REPLACE INTO Vacancies 
    (Job_Title, Company_Name, Location, Description, Application_Link) 
    VALUES (?, ?, ?, ?, ?)
    '''
    
    cursor.executemany(query2, vacancies_data)
    con.commit()

def filter_jobs(location=None, company=None):
    with sqlite3.connect("jobs.db") as con:
        cursor = con.cursor()
        query = "SELECT * FROM Vacancies WHERE 1=1"
        params = []

        if location:
            query += " AND Location = ?"
            params.append(location)

        if company:
            query += " AND Company_Name = ?"
            params.append(company)

        cursor.execute(query, params)
        return cursor.fetchall()
    
def export_to_csv(file_name = "jobs.csv", location=None, company =None):
    jobs = filter_jobs(location, company)
    if not jobs:
        print("No jobs are found with given filter!")
        return 
    
    headers = ["Job Title", "Company Name", "Location", "Job Description", "Application Link"]
    with open("jobs.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(jobs)

export_to_csv(company="Kim-Miles")