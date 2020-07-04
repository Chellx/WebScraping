from bs4 import BeautifulSoup
import requests
import csv

    #writing to csv file
csv_file = open('scrapefile.csv', 'w')  #write results to this file
csv_write = csv.writer(csv_file)
csv_write.writerow(['Info', 'Price', 'Location']) #column names in csv file

for i in range(3): #num of pages plus 1
    source = requests.get('https://www.adverts.ie/for-sale/tickets/concerts-festivals/225/page-'+format(i)).text #retuns response object, 
    #+format(i) concatinates string &  formats the specified value(s) and insert them inside the string's placeholder.
    soup = BeautifulSoup(source, 'lxml')



    for div in soup.find_all('div', class_='item-details'):
        ticketInfo = div.find('div', class_='title').a.text
        print(ticketInfo)

        ticketPrice = div.find('div', class_='price').a.text
        print(ticketPrice)

        ticketLocation = div.find('div', class_='location').a.text
        print(ticketLocation)

        print() #blank string to separate info

        csv_write.writerow([ticketInfo, ticketPrice, ticketLocation])
 
csv_file.close() #closing csv file
