import requests
from time import sleep
from bs4 import BeautifulSoup
import sqlite3
import datetime
#establishing connection between the script and the databse
conn = sqlite3.connect("jobhunter.db")

c = conn.cursor()
c.execute("CREATE TABLE  IF NOT EXISTS  jobhunter_main (title TEXT, country TEXT ,details TEXT, path_url_lv TEXT, date integer)")

page_num_ee = 0
page_num_lv = 0    
 
# cv.ee scraping 

while page_num_ee <= 200:
    page_num_ee += 20
    url_ee = requests.get(f"https://cv.ee/search?limit=20&offset={page_num_ee}&isHourlySalary=false")
    html_ee = BeautifulSoup(url_ee.text, "html.parser")
    layer_first_ee = html_ee.find_all(class_="jsx-1471379408 vacancy-item")
# assigning each info to a var    
    for one in layer_first_ee:
        path_url_ee = one.find("a")["href"]
        instance_title_ee= one.find("span").get_text()
        instance_url_ee = f"https://cv.ee{path_url_ee}"
        instance_details_ee = one.find(class_="jsx-1471379408 vacancy-item__info").get_text()
        location_ee = one.find(class_="jsx-1471379408 vacancy-item__locations").get_text()
        instance_fetch_time = datetime.datetime.now().strftime("%y%m%d")  
        instance_ee = (instance_title_ee,'Estonia', instance_details_ee, instance_url_ee, instance_fetch_time )
# adding the data to sqlite 
        c.execute("INSERT INTO jobhunter_main VALUES(?,?,?,?,?)", instance_ee)
    print(f"page {page_num_ee} has been added to the database for Esti")
    sleep(2)
# cv.lv scraping 
while page_num_lv <= 10:    
    url_lv = requests.get(f"https://www.cv.lv/darba-sludinajumi/visi?page={page_num_lv}")
    html_lv = BeautifulSoup(url_lv.text, "html.parser")
    first_layer_lv = html_lv.find_all(class_="cvo_module_offer_box offer_content")
#assigning the data to vars
    for instace in first_layer_lv:
        path_url_lv = instace.find("a")["href"]
        instance_title_lv = instace.find("a").get_text()
        add_info_lv = instace.find(class_="offer-primary-meta clearfix").get_text()
        add_info_lv = add_info_lv.replace("\n", " ").replace("   ", " ")
        instance_fetch_time = datetime.datetime.now().strftime("%y%m%d") 
        location_lv =instace.find(class_="offer-location").get_text()
        instance_details_lv = f"{location_lv} {add_info_lv}"

        instance_lv = (instance_title_lv, 'Latvia', instance_details_lv, path_url_lv, instance_fetch_time )
# adding the data to the same database
        c.execute("Insert into jobhunter_main Values(?,?,?,?,?)",instance_lv)
    print(f"page {page_num_lv} has been added to the database for Latvia")
    page_num_lv += 1
    





    #gentle scraping, not runing anywhere      
    sleep(5)
conn.commit()

conn.close()



# DELETE FROM jobhunter_main  where rowid not in (select rowid from jobhunter_main GROUP by path_url_lv);








    




