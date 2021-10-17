from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv

driver = webdriver.Chrome(executable_path='C:\\Users\\rizwa\\Downloads\\chromedriver_win32\\chromedriver.exe')
class hotel:
    def __init__(self,name,price,reviews,rating):
        self.name=name
        self.price=price
        self.reviews=reviews
        self.rating=rating

driver.get("https://www.tripadvisor.com/Hotels-g34439-Miami_Beach_Florida-Hotels.html")
content = driver.page_source
soup = BeautifulSoup(content)
array_list=[]
for a in soup.findAll('div',attrs={'class':'ui_column is-8 main_col allowEllipsis'}):
    name=a.find('a' ,attrs={'class':'property_title prominent'})
    price=a.find('div',attrs={'class':'price __resizeWatch'})
    reviews=a.find('a',attrs={'class':'review_count'})
    
    rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_50'})
    if rating==None:
        rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_45'})
        if rating==None:
            rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_40'})
            if rating==None:
                rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_35'})
                if rating==None:
                    rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_30'})
                    if rating==None:
                        rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_25'})
                        if rating==None:
                            rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_20'})
                            if rating==None:
                                rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_15'})
                                if rating==None:
                                    rating=a.find('a',attrs={'class':'ui_bubble_rating bubble_10'})
    rating=rating["alt"]
    rating=rating.replace(' of 5 bubbles','')
    
    h=hotel(*name,*price,*reviews,rating)
    array_list.append(h)
    
header = ['Name', 'Price', 'Reviews','Rating','City']
with open("hotels.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
for i in array_list:
    data=[i.name,i.price,i.reviews,i.rating,"Florida"]
    with open("hotels.csv", "a", newline='',encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)
    