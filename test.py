import requests
from bs4 import BeautifulSoup
import csv  # New

#code  = '0105563002305'
code = input("Please enter a id:\n")
#oldcode = '77753'

#url = f'http://203.157.10.8/hcode_2014/query_detail.php?p=3&code={code}&oldcode={oldcode}&status=01'
url = f'https://data.creden.co/company/general/{code}'
#url = f'https://data.creden.co/company/general/0105563004847'
source = requests.get(url)

soup = BeautifulSoup(source.content, 'lxml')

div   = soup.find('div',id='__layout')
#class="table-responsive"
table = div.find ('table', class_="table table-striped")
#rows = table.find_all('tr')
#rows  = table.findChildren('tr', recursive=False)
courses = soup.find_all('td')
course_list = []

for course in courses:
    
    # Create a new variable --> obj to store 
    # only course name getting rid of unwanted tags
    obj = course.string
    
    # Append each course into a course_list variable
    course_list.append(obj)
    
print(course_list[0],course_list[3],course_list[4])

#print(course_list)
#print(table.prettify())

#pam = course_list[0],course_list[3],course_list[4]

#csv_col = [['title'], [course_list[0],course_list[3],course_list[4]]]

# Name a file, and put w as an argument to tell this is "writer" file
#f = open('2.csv', 'w')
#with f:
#    writer = csv.writer(f)

#    for row in csv_col:
#        writer.writerow(row)