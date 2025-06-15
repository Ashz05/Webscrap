#This app for Web scrapping 


import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time 
import random


#url_text="https://www.booking.com/searchresults.html?ss=New+Delhi&ssne=New+Delhi&ssne_untouched=New+Delhi&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Av7PtcIGwAIB0gIkNGJhYTRjMjAtYjBmOS00NGY5LTk4MzUtNGJmNDM4N2ZhZTcz2AIF4AIB&sid=c6875ebb136d9b44a015abaafe60323b&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2106102&dest_type=city&checkin=2025-07-01&checkout=2025-07-02&group_adults=2&no_rooms=1&group_children=0"



def web_scrapper1(web_url, file_name):
    #greetings
    print("Thank you for sharing the url and file name!\nStarting the Web scrapping\nReading the content from the url\n please wait...\n")
    
    
    num = random.randint(3,7)

    time.sleep(num) #Adding delay of 5 seconds





    #headers
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}





    response=requests.get(web_url, headers=header)




    if response.status_code == 200:
        print("Request was successfull")
        html_content=response.text
    

        #creating soup
        soup= BeautifulSoup(html_content, 'lxml')

    #print(soup.prettify())
    #main container
        hotel_divs=soup.find_all('div', role="listitem")


        with open(f'{f_name}.csv','w',encoding='utf-8')as file_csv:
            writer = csv.writer(file_csv)


        #adding header
            writer.writerow(['hotel_name', 'location', 'price', 'rating', 'score', 'review', 'link'])
    

        #Iterating all hotel lists
            for hotel in hotel_divs:
                hotel_name=hotel.find('div', class_="b87c397a13 a3e0b4ffd1").text.strip()
                hotel_name if hotel_name else "NA"

                location=hotel.find('span', class_="d823fbbeed f9b3563dd4").text.strip()
                location if location else "NA"

            #price
                price=hotel.find('span', class_="b87c397a13 f2f358d1de ab607752a2").text.replace('₹ ', '')
                if price:
                    price
                else:
                    "NA"

                rating=hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63").text
                rating if rating else "NA"


                score=hotel.find('div',class_="f63b14ab7a dff2e52086").text.strip().split(' ')[-1]
                score if score else "NA"


                review=hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
                review if review else "NA"

            #getting link 
                link = hotel.find('a',href=True).get('href')
                link if link else "NA"

            #Saving file as csv
                writer.writerow([hotel_name, location, price, rating, score, review, link])


            # print(hotel_name)
            # print(location)
            # print(price)
            # print(rating)
            # print(score)
            # print(review)
            # print(link)
            # print('')
        print("Web scrapping completed")


    else:
        print("Request was not successfull")

#if using this script directly than below task will be executed
if __name__ == "__main__":

    url=input("Please enter the url!: ")
    f_name=input("Please give file name!: ")

    #calling function
    web_scrapper1(url,f_name)
