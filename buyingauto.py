import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random
import webbrowser
import threading
from selenium.webdriver.common.proxy import Proxy, ProxyType

from webtools import webanon 


def main():
    supreme()


def supreme(): 

    items = ['jackets/','sweatshirts/','shirts/','pants/','t-shirts/','hats/','bags/','accessories/','shoes/','skate/','tops-sweaters/']

    sizes = ['Medium', 'Large', 'XLarge']

    product_hrefs = [] #hrefs that are turned into urls
    products = [] #list of new product urls
    colours = []
     
    
   # url = ("https://www.supremenewyork.com/shop/all/" + items[1])   #changes which type of product


    url = ("https://www.supremenewyork.com/shop/new") #for all new products
    
    web = webanon()

    user_agent = web.agent()
    headers = {'User-Agent': user_agent}
    res = requests.get(url, headers=headers)
    supreme = BeautifulSoup(res.text, "lxml")
    new_products = supreme.findAll('div',{'class':'inner-article'})
#    print(new_products)
    
    for n_products in new_products:               #isolates the url for products
        if 'href="/shop/' + items[1] + str(n_products):
            product_hrefs.append(n_products)

 
    supreme_url_generator(product_hrefs,products,items,supreme,colours)

    #allows for multiple browsers at once

    buy_items(products,sizes,user_agent,colours)

#    browser1 = threading.Thread(target=buy_items, args=(products,sizes,user_agent))
   # browser2 = threading.Thread(target=buy_items, args=(products,sizes,user_agent))

 #   browser1.start()
  #  proxyipaddress = web.proxyip()
  #  browser2.start()

 #   buy_items(products,sizes)
    
    
def buy_items(products,sizes,user_agent,colours):
    """purchases all items until bot crashes"""
 

    web = webanon()
    user_agent = web.agent()
    headers = {'User-Agent': user_agent}
    product_colour = []
    
    for product in products:
        url = (product)
        res = requests.get(url, headers=headers)
        supreme = BeautifulSoup(res.text, "lxml")
        product_colour.append(str(supreme.select('.style.protect')))

    colour_id = tuple(zip(product_colour,colours))
    print(colour_id)



    

    


    #print(colours,)

    

#    browser = webdriver.Chrome()  
    
 #   for product in products:
  #      browser.get(product)
   #     instock = sold_out(url,browser,supreme)
    #    if instock == True:
     #       try:
      #          item_choices(browser,sizes,products,supreme)
       #         checkout(browser)
        #    except Exception:
         #       time.sleep(20)
          #      continue
            
       # elif instock == False:
       #     continue


    
            
def sold_out(url,browser,supreme):
    """Checks whether an item is in stock"""

    available = supreme.findAll('input',{'class':'button'})
    

    try:
        too_many = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "warning", " " ))]')
    except Exception:
        pass
    else:
        return False
        
    if available:
         return True
    else:
         return False
    
        
def supreme_url_generator(product_hrefs,products,items,supreme,colours):

    for hrefs in product_hrefs: #generates brand new working urls based on new product
         product_url = url_finder(hrefs,items,supreme)
         productkeys = (product_url[0:10])
         productcolour = product_url[10:19]
         colours.append(productcolour)
   #      print(productcolour)



         products.append('https://www.supremenewyork.com/shop/' + items[1] + str(product_url))
         
    
        
def item_choices(browser,sizes,products,supreme):
    """Chooses size and colour"""
    #any time a productis bought, remove the different URLS for other colours
    
    while True:
        #    colour = browser.find_element_by_css_selector('p.style.protect')
            
          #  if 'Black' or 'Grey' in colour:
            size = browser.find_element_by_name('s')
            size.send_keys('Medium')
            add_to_cart = browser.find_element_by_name('commit')
            add_to_cart.click() 
      #      else:
        #        continue 
                # 

           # print(colour)
      #  if colour == 'Black':
            
            
 #       else:
   #         continue         
  #     
  
        #remove the different colours of the products
    
    #    break

def url_finder(hrefs,items,supreme):
    """Generates supreme URLS for products"""
    urls = str(hrefs)
    for item in items:
        urls = urls.split(item)[-1]
                
    urls = urls[0:19]

   
   
    return urls
            
def checkout(browser):
    """inputs the necessary information on the checkout page"""

    while True:
        try:
                checkout_now = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "checkout", " " ))]')
                checkout_now.click()
                name = browser.find_element_by_name('order[billing_name]')
                name.send_keys('Peter Simon')
                email = browser.find_element_by_name('order[email]')
                email.send_keys('Peter@example.com')
                tel = browser.find_element_by_name('order[tel]')
                tel.send_keys('555-555-5555')
                address = browser.find_element_by_name('order[billing_address]')
                address.send_keys('blazeit road')
                address2 = browser.find_element_by_name('order[billing_address_2]')
                address2.send_keys('420')
                zipcode = browser.find_element_by_name('order[billing_zip]')
                zipcode.send_keys('M3Z1K1')
                city = browser.find_element_by_name('order[billing_city]')
                city.send_keys('Toronto')
                country = browser.find_element_by_name('order[billing_country]')
                country.send_keys('CANADA')
                province = browser.find_element_by_name('order[billing_state]')
                province.send_keys('ON')
                cardnumber = browser.find_element_by_name('credit_card[nlb]')
                cardnumber.send_keys('2394857685940304')
                cardmonth = browser.find_element_by_name('credit_card[month]')
                cardmonth.send_keys('08')
                cardyear = browser.find_element_by_name('credit_card[year]')
                cardyear.send_keys('2028')
                cvv = browser.find_element_by_name('credit_card[rvv]')
                cvv.send_keys('123')
                continue
        except Exception:
                print('Terms and Conditions')
                time.sleep(300)
                continue
        

            #Drops every thursday at 11 AM




 #   terms_and_conditions = browser.find_element_by_name('order[terms]')
 #   terms_and_conditions.send_keys(Keys.TAB)
 #   terms_and_conditions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "button", " " ))]')))
 #   terms_and_conditions.click()
  #  process_payment = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "button", " " ))]')
  #  process_payment.click()

if __name__ == "__main__":
#    try:
        main()
 #   except Exception:
  #      time.sleep(5)
         

