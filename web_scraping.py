import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest 

job_titles = []
company_names = []
location_names = []
job_skills = []
links = []



result = requests.get("https://wuzzuf.net/search/jobs/?q=Python&a=hpb")
# This line sends a GET request to the specified URL and returns the server's response.
src = result.content
# This line gets the content of the response, which is the HTML of the webpage.
soup = BeautifulSoup(src, "lxml")
# This line parses the HTML content of the webpage using the lxml parser.
Vjobs_titles = soup.find_all("h2", {"class": "css-m604qf"})
Vcompany_names = soup.find_all("a", {"class":"css-17s97q8"})
Vlocation_names = soup.find_all("span", {"class":"css-5wys0k"})
Vjob_skills = soup.find_all("div", {"class":"css-y4udm8"})

for i in range(len(Vjobs_titles)):
    job_titles.append(Vjobs_titles[i].text)
    links.append(Vjobs_titles[i].find("a").attrs['href'])
    company_names.append(Vcompany_names[i].text)
    location_names.append(Vlocation_names[i].text)
    job_skills.append(Vjob_skills[i].text)

file_list = [job_titles, company_names, location_names, job_skills, links]
exported = zip_longest(*file_list)

with open("C:\\Learn Programming\\Web Scraping with Python\\jobstutorial.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company Name", "Location Name", "Job Skills", "Links"])
    wr.writerows(exported)



