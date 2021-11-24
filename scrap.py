import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import math
import re

baseUrl= 'https://www.amazon.com/'
url='https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1603803269&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
TIMEOUT = 2
PageNumber= 101

class BookScraper():
    #this is for making driver
    def headlessDriver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--window-size=1920, 900")
        chrome_options.add_argument("--hide-scrollbars")
        driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver86.exe")
        return driver
    def headDriver(self):
        options = Options()
        options.headless = False
        options.add_argument("--window-size=1920,1200")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver86.exe")
            return driver
        except:
            print("You must install chrome 86!")
            return 0
    def scrape(self):
        # write csv headers
        if os.path.exists('result.csv'):
            os.remove('result.csv')
        columns=['Title', 'Price', 'Star', 'Rating', 'Genre', 'Badge', 'Url', 'ASIN']
        df = pd.DataFrame(columns = columns)
        df.to_csv('result.csv', mode='x', index=False, encoding='utf-8')

        driver= self.headDriver()
        for i in range(PageNumber):
            if i==0:
                driver.get(url)
                time.sleep(TIMEOUT)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # finding book field
            bookDoms= soup.find_all('div', attrs={'class':'a-section a-spacing-medium'})
            books= []
            # getting data of each book
            for bookDom in bookDoms:
                if bookDom!=None:
                    titleDom= bookDom.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
                    if titleDom!=None:
                        title= titleDom.text
                    else:
                        title= "Empty"
                    star_ratingDom= bookDom.find('div', attrs={'class':'a-section a-spacing-none a-spacing-top-micro'})
                    if star_ratingDom!= None:
                        starDom= star_ratingDom.find('span', attrs={'class':'a-icon-alt'})
                        if starDom!= None:
                            star= starDom.text
                        else:
                            star= "Empty"
                        ratingDom= star_ratingDom.find('span', attrs={'class':'a-size-base'})
                        if ratingDom!= None:
                            rating= ratingDom.text
                        else:
                            rating= "Empty"
                    priceDom= bookDom.find('span', attrs={'class':'a-offscreen'})
                    if priceDom!= None:
                        price= priceDom.text
                    else:
                        price= "Empty"
                    badgeDom= bookDom.find('span', attrs={'class':'a-badge-text'})
                    if badgeDom!= None:
                        badge= badgeDom.text
                    else:
                        badge= "Empty"
                    genreDom= bookDom.find('span', attrs={'class':'a-badge-supplementary-text a-text-ellipsis'})
                    if genreDom!= None:
                        genre= genreDom.text
                    else:
                        genre= "Empty"

                    # for get url
                    elem = bookDom.find('a', attrs={'class':'a-link-normal s-no-outline'})
                    alink = elem.attrs['href']
                    bookurl= baseUrl+alink
                    # for get ASIN
                    asin= bookurl.split("/dp/", 1)[1].split("/ref=")[0]
                    # for get ASIN
                    # driver.get(bookurl)
                    # time.sleep(TIMEOUT)
                    # booksoup = BeautifulSoup(driver.page_source, 'html.parser')
                    # detailDom= booksoup.find('div', attrs={'id':'audibleProductDetails'})
                    # asin= 'Empty'
                    # if detailDom!= None:
                    #     asinDom= detailDom.find('tr', attrs= {'id':'detailsAsin'})
                    #     if asinDom!= None:
                    #         asin= asinDom.find('td').text
                    # else:
                    #     detailDom= booksoup.find('div', attrs= {'id': 'detailBulletsWrapper_feature_div'})
                    #     if detailDom!= None:
                    #         asinDom= detailDom.find('div', attrs= {'id': 'detailBullets_feature_div'}).find_all('li')[-1]
                    #         if asinDom.find('span').find('span').text.find('ASIN')!= -1:
                    #             asin= asinDom.text
                    new= {'Title': title, 'Price': price, 'Star': star, 'Rating': rating, 'Genre': genre, 'Badge': badge, 'Url': bookurl, 'ASIN': asin}
                    # driver.execute_script("window.history.go(-1)")
                    books.append(new)
            # writing in csv file
            df = pd.DataFrame(books, columns = columns)
            print("Now "+str(i+1)+"page writed in csv file!")
            df.to_csv('result.csv', mode='a', header=False, index=False, encoding='utf-8')
            try:
                driver.find_element_by_xpath("//li[@class='a-last']").click()
            except:
                time.sleep(TIMEOUT*4)
                driver.find_element_by_xpath("//li[@class='a-last']").click()
            time.sleep(TIMEOUT)
        print("Done!")
if __name__ == '__main__':
    scraper = BookScraper()
    scraper.scrape()





    try:
        javascript1 = "document.getElementsByClassName('otFlat bottom')[0].setAttribute('style', 'display: none;');"
        browser.execute_script(javascript1)
    except:
        pass
    try:
        browser.find_element_by_xpath("//button[@id='showNumberButton']").click()
    except:
        sleep(1)
        # browser.find_element_by_xpath("//button[@id='showNumberButton']").click()
    sleep(0.2)
    phone1= "***"
    # try:
    # 	javascript1 = "document.getElementsByClassName('otFlat bottom')[0].setAttribute('style', 'display: none;');"
    # 	browser.execute_script(javascript1)
    # except:
    # 	pass
    print(browser.find_element_by_xpath("//div[@class='PostCallSurvey-header']").find_element_by_tag_name('div').text)
    print(phone1)
    input('1')
    browser.find_element_by_xpath("//span[@class='PostCallSurvey-close']").click()
    input('2')
    sleep(0.1)


    DesktopMessagingHeader-toggleIcon