import asyncio
from itertools import count
from multiprocessing.connection import wait
from threading import Thread
from time import sleep
from pyppeteer import launch
import tweepy
import keyboard


async def main(country_code,city_code):
    # launch chromium browser in the background
    browser = await launch({"headless": False})
    # open a new tab in the browser
    page = await browser.newPage()
    
    # add URL to a new page and then open it
    await page.goto("https://fazilettakvimi.com/namaz-vakitleri/")
    await page.waitFor(2000)
    
   
    
    print(country_code)
    await page.type("div.Bolge_ulke__3t04j select",country_code)
    await page.keyboard.press("Enter")
    await page.waitFor(1000)
    
    #await page.select("div.Bolge_ulke__3t04j select",country_code)
    
    #await page.select("div.Bolge_sehir__1Gle0 select",city_code)
    print(city_code)
    await page.type("div.Bolge_sehir__1Gle0 select",city_code)
    await page.keyboard.press("Enter")

    
    await page.waitFor(1000)
    # create a screenshot of the page and save it
    await page.screenshot({"path": "python.png"})
    #await page.waitFor(20000)
    # close the browser
    await browser.close()





auth = tweepy.OAuth1UserHandler(
   "H6Lj8ynPiwzyTPX3QoNMN8zYV", "sR37yoPDkPga4tYNsoZ7NdAHLHnhmehE9FguljNzubHGNwVsQ5", "1555137243253194752-FvlD5enmUBXwCWjLQSekkL0pMqRrvv", "PoTbwiIzOEPujavJdk0bQzfqNXDMJUAX8K7Icax3er6lM"
)

with open("used.txt", "r") as f:
    data = f.read()
    f.close()
    print("DATA")
    print(str(data))
    

print("Starting...")
loop = asyncio.get_event_loop()



api = tweepy.API(auth)

#for status in tweepy.Cursor(api.user_timeline).items():
            #try:
                #api.destroy_status(status.id)
                #print("Deleted:", status.id)
            #except Exception:
                #traceback.print_exc()
                #print("Failed to delete:", status.id)



i = 0
j=0
while i == 0:
    if keyboard.is_pressed("q"):
        break
    tweets = api.search_tweets(q = "@BotFazilet", result_type ="recent", count=10,tweet_mode="extended")
    for j in range(0,len(tweets)):
     if(tweets[j] != []):
      tweetid = tweets[j].id
      print(tweetid)
     
     print("LOL")
     if(str(tweetid) in data):
        print("DUPLICATE")
        sleep(5)
     else:
        try:
         temp = tweets[j].full_text.split("#")
         loop.run_until_complete(main(temp[1],temp[2]))
         api.update_status_with_media('your reply',"python.png", in_reply_to_status_id = tweetid , auto_populate_reply_metadata=True)
         data = data+ str(tweetid)
         print(data)
         print(str(tweetid))
         with open("used.txt", "w+") as f:
          temp = data
          f.write(temp)
          f.write("-")
          f.write(str(tweetid))
          f.flush()
          f.close()
         sleep(5) 
         print("replied")
        except Exception:
            print("ERROR IN INPUT")

    





        

    


