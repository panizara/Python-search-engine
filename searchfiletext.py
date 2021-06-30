import requests
from bs4 import BeautifulSoup
#import csv  #

file = open('filecode2001-3000.txt', 'r' )#You can add encoding='utf-8'
code = file.readlines()
#url = f'https://data.creden.co/company/general/{code}'

for index, line in enumerate(code):
    pam = ("https://data.creden.co/company/general/{}".format(line.strip()))
    #print(pam)
    url = pam

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')
    div   = soup.find('div',id='__layout')
    table = div.find ('table', class_="table table-striped")
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
