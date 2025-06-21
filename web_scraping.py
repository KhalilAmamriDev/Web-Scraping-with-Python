import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest 

job_titles = []
company_names = []
location_names = []
job_skills = []
links = []
date = []
page_number = 0

while True:
    try:
        result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=Python&start={page_number}")
        # This line sends a GET request to the specified URL and returns the server's response.
        src = result.content
        # This line gets the content of the response, which is the HTML of the webpage.
        soup = BeautifulSoup(src, "lxml")
        # This line parses the HTML content of the webpage using the lxml parser.
        page_limit = int(soup.find("strong").text)
        if page_number >= (page_limit) // 15:
            print("No more pages to scrape.")
            break
        Vjobs_titles = soup.find_all("h2", {"class": "css-m604qf"})
        Vcompany_names = soup.find_all("a", {"class":"css-17s97q8"})
        Vlocation_names = soup.find_all("span", {"class":"css-5wys0k"})
        Vjob_skills = soup.find_all("div", {"class":"css-y4udm8"})
        posted_new = soup.find_all("div", {"class":"css-4c4ojb"})
        posted_old = soup.find_all("div", {"class":"css-do6t5g"})
        posted = [*posted_new, *posted_old]

        for i in range(len(Vjobs_titles)):
            job_titles.append(Vjobs_titles[i].text)
            links.append(Vjobs_titles[i].find("a").attrs['href'])
            v_company_name_without_dash = Vcompany_names[i].text.replace("-", "")
            company_names.append(v_company_name_without_dash.strip())
            location_names.append(Vlocation_names[i].text)
            job_skills.append(Vjob_skills[i].text)
            date.append(posted[i].text)
        page_number += 1
        print("Page switched to", page_number)
    except Exception as e:
        print("An error occurred:", e)
        break

# for link in links:
#     result = requests.get(link)
#     src = result.content
#     soup = BeautifulSoup(src, "lxml")
#     Vsalary = soup.find("h2", {"class":"css-1u59jur"})
#     salarys.append(Vsalary.text.strip() if Vsalary else "1qqqjsss")

file_list = [job_titles, company_names, date, location_names, job_skills, links]
exported = zip_longest(*file_list)

with open("C:\\Learn Programming\\Web Scraping with Python\\jobstutorial.csv","w", encoding="utf-8", newline='') as myfile:
    wr = csv.writer(myfile, delimiter = ';')
    wr.writerow(["Job Title", "Company Name", "date", "Location Name", "Job Skills", "Links"])
    wr.writerows(exported)
