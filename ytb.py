from selenium import webdriver
import time
import datetime
import random

driver = webdriver.Chrome("C:\\Users\Homer\\Downloads\\chromedriver.exe")

videos = ["https://www.youtube.com/watch?v=xhmYX-1GeTs",
          "https://www.youtube.com/watch?v=2ZGFIaZiQ04",
          "https://www.youtube.com/watch?v=PpnEbPBk5ik",
          "https://www.youtube.com/watch?v=NHk7YpINS9I",]

for i in range(1000):
    print("Running the Videos for {} times".format(i))
    
    now = datetime.datetime.now()
    seconds = now.second
    r_start_time = seconds + random.randint(10, 900)

    driver.get(videos[random.randint(0, 3)] + "&t=" + str(r_start_time) )

    while seconds > 30:
        seconds -= 30
    rnum = random.randint
    sleep_time = random.randint(30 + seconds, seconds + 45)
    time.sleep(sleep_time)
    
    print("Watch from {} to {}".format(r_start_time, r_start_time + sleep_time))

driver.quit()
    
    

