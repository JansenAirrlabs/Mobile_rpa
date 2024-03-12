import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import  TouchAction
from time import sleep,time
import os
import pdb
import random
from datetime import datetime
import csv
from datetime import datetime
import logging 
from pythonjsonlogger import jsonlogger
import json

from config import Brand

UTCcurrent_date = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

log_filename = '/home/airrlabsadmin/Desktop/mobile_rpa/logs/logs_' + UTCcurrent_date + '.txt'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 
formatter = jsonlogger.JsonFormatter()

file_handler = logging.FileHandler(log_filename)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class LazadaVisitorDaily:
    def __init__(self):
        self.driver = None


    def setUp(self):
        logger.info('Opening App')
        capabilities = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'deviceName': 'Android',
            'appPackage': 'com.sc.lazada',
            'appActivity': '.app.activity.main.MainActivity',
            'language': 'en',
            'locale': 'US',
            'noReset': True
        }
        appium_server_url = 'http://127.0.0.1:4723'

        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        sleep(random.randint(4, 6))
   
    def handle_popup(self):
        try:                                                                   
            popup = self.driver.find_element(by=AppiumBy.ID, value='com.sc.lazada:id/iv_close')
            popup.click()
        except:
            pass
        finally:
            sleep(random.randint(2,3))


    def run(self):
        for Client in Brand["Clients"]:
            action = TouchAction(self.driver)
            UV_Daily= []
            Orders_Daily=[]
            Buyer_Daily = []
            Reveue_Daily = []

            Client_Brand = Client["Brand"]
            Country = Client["Country"]
            Account_Name = Client["Name"]
            Current_timestamp_seconds = int(time())

            sleep(random.randint(2,3))
            LazadaVisitorDaily().handle_popup()

            try:
                account_dropdown = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@resource-id="com.sc.lazada:id/iv_account_arrow"]')
                account_dropdown.click()
                sleep(random.randint(2,3))
                account_name = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.sc.lazada:id/tv_shop_name" and @text="{Name}"]'.format(Name = Account_Name))
                account_name.click()
            except:
                pass
            finally:
                action.tap(x=145, y=2277).perform()
                sleep(random.randint(2,3))


            LazadaVisitorDaily().handle_popup()

            
            logger.info('Going to Bussiness Advisor')
            search_bar = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@resource-id="com.sc.lazada:id/main_bottombar"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout')
            search_bar.click()
            sleep(random.randint(5, 10))
            counter = 1
            
            while counter < 5: 
                self.driver.swipe(470, 1400, 470, 1000, 400)
                sleep(random.randint(1,2))
                counter += 1   
                print(counter)
            
            bussness_adivisor_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.sc.lazada:id/tool_name" and @text="Business Advisor"]')
            bussness_adivisor_btn.click()
            sleep(random.randint(5,8))

                
                
            #daily visitor 
            action.tap(x=380, y=622).perform() #going to daily
            sleep(random.randint(3,5))

            action.tap(x=289, y=816).perform() #cgoing to daily
            sleep(random.randint(3,5))

            action.tap(x=765, y=877).perform() #click Visitor
            sleep(random.randint(3,5))

            action.tap(x=555, y=1404).perform() #click View Chart
            sleep(random.randint(3,5))
            
            action.tap(x=983, y=1400).perform() #click table icon
            sleep(random.randint(3,5))

            action.tap(x=549, y=2100).perform() # click more
            sleep(random.randint(3,5))

            # self.driver.swipe(579, 2033, 553, 1500, 300)
            sleep(random.randint(3,5))

            self.driver.page_source
            logger.info('Extracting Data From the table')
            grid_view = self.driver.find_element(AppiumBy.XPATH, "//android.widget.GridView")
            
            grid_rows = grid_view.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
            

            current_datetime = datetime.now()
            filename = "{country}_lazada_{brand}_{time}_daily.csv".format(country = Country,brand= Client_Brand,time=Current_timestamp_seconds)
            csv_file_path = "pictures/visitor/{filename}".format(filename=filename)
            if not os.path.isfile(csv_file_path):
                with open(csv_file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)

            while grid_view:
                print(grid_view)
                self.driver.page_source

                if grid_view:
                    for row in grid_rows:
                        row_items = row.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
                        row_data = [item.text for item in row_items]
                        # print("Row Data:", row_data)
                        if row_data[0] != "Date":
                            if [row_data[0],row_data[1],row_data[2]] not in UV_Daily:
                                UV_Daily.append([row_data[0],row_data[1],row_data[2]])

                            else:
                                pass
                        else:
                            pass
                            
                    self.driver.swipe(499, 2130, 510, 1778)
                    sleep(random.randint(3,5))
                    try:
                        grid_view = self.driver.find_element(AppiumBy.XPATH,value='//android.widget.GridView')
                        grid_rows = grid_view.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
                    except:
                        grid_view = None
                else:
                    break


            self.driver.swipe(488, 428, 530, 2115)
            sleep(random.randint(3,5))





            #orders
            
        
            action.tap(x=160, y=877).perform() #click orders
            sleep(random.randint(3,5))

            action.tap(x=153, y=140).perform() 
            sleep(random.randint(3,5))

            bussness_adivisor_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.sc.lazada:id/tool_name" and @text="Business Advisor"]')
            bussness_adivisor_btn.click()
            sleep(random.randint(5,8))


            action.tap(x=380, y=622).perform() #going to daily
            sleep(random.randint(3,5))

            action.tap(x=289, y=816).perform() #cgoing to daily
            sleep(random.randint(3,5))

            action.tap(x=467, y=858).perform() #click orders
            sleep(random.randint(3,5))
        

            action.tap(x=534, y=1214).perform() #click View Chart
            sleep(random.randint(3,5))
            
            action.tap(x=1004, y=1207).perform() #click table icon
            sleep(random.randint(3,5))

            action.tap(x=525, y=1901).perform() # click more
            sleep(random.randint(3,5))


            self.driver.page_source
            logger.info('Extracting Data From the table')
            grid_view2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.GridView")
            
            grid_rows2 = grid_view2.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
            

            while grid_view2:
                print(grid_view2)
                self.driver.page_source

                if grid_view2:
                    for row in grid_rows2:
                        row_items = row.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
                        row_data = [item.text for item in row_items]
                        # print("Row Data:", row_data)
                        if row_data[0] != "Date":
                            if [row_data,row_data[1],row_data[2]] not in Orders_Daily:
                                Orders_Daily.append([row_data[0],row_data[1],row_data[2]])
                            else:
                                pass
                        else:
                            pass
                            
                    self.driver.swipe(499, 2130, 510, 1778)
                    sleep(random.randint(3,5))
                    try:
                        grid_view2 = self.driver.find_element(AppiumBy.XPATH,value='//android.widget.GridView')
                        grid_rows2 = grid_view2.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
                    except:


                        grid_view2 = None
                    
                else:
                    break

            # Perform swipe gesture
            # self.driver.swipe(488, 428, 530, 2115)

            action.tap(x=50, y=143).perform() 
            sleep(random.randint(3,5))

            bussness_adivisor_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.sc.lazada:id/tool_name" and @text="Business Advisor"]')
            bussness_adivisor_btn.click()
            sleep(random.randint(5,8))


            
            action.tap(x=380, y=622).perform() #going to daily
            sleep(random.randint(3,5))

            action.tap(x=289, y=816).perform() #cgoing to daily
            sleep(random.randint(3,5))


            action.tap(x=765, y=877).perform() #click visitor
            sleep(random.randint(3,5))

            action.tap(x=765, y=875).perform() #click buyer
            sleep(random.randint(3,5))


            action.tap(x=534, y=1214).perform() #click View Chart
            sleep(random.randint(3,5))
            
            action.tap(x=1004, y=1207).perform() #click table icon
            sleep(random.randint(3,5))

            action.tap(x=525, y=1901).perform() # click more
            sleep(random.randint(3,5))



            self.driver.page_source
            logger.info('Extracting Data From the table')
            grid_view3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.GridView")
            
            grid_rows3 = grid_view3.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
            

            while grid_view3:
                print(grid_view3)
                self.driver.page_source

                if grid_view3:
                    for row in grid_rows3:
                        row_items = row.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
                        row_data = [item.text for item in row_items]
                        # print("Row Data:", row_data)
                        if row_data[0] != "Date":

                            if [row_data[0],row_data[1],row_data[2]] not in Buyer_Daily:
                                Buyer_Daily.append([row_data[0],row_data[1],row_data[2]])
                            else:
                                pass
                        else:
                            pass
                            
                    self.driver.swipe(499, 2130, 510, 1778)
                    sleep(random.randint(3,5))
                    try:
                        grid_view3 = self.driver.find_element(AppiumBy.XPATH,value='//android.widget.GridView')
                        grid_rows3 = grid_view3.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
                    except:
                        grid_view3 = None
                    
                else:
                    break



            action.tap(x=50, y=143).perform() 
            sleep(random.randint(3,5))

            bussness_adivisor_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.sc.lazada:id/tool_name" and @text="Business Advisor"]')
            bussness_adivisor_btn.click()
            sleep(random.randint(5,8))


            action.tap(x=380, y=622).perform() #going to daily
            sleep(random.randint(3,5))

            action.tap(x=289, y=816).perform() #cgoing to daily
            sleep(random.randint(3,5))

            action.tap(x=553, y=1372).perform() 
            sleep(random.randint(3,5))

            action.tap(x=994, y=1360).perform() 
            sleep(random.randint(3,5))

            action.tap(x=538, y=2056).perform() 
            sleep(random.randint(3,5))



            self.driver.page_source
            logger.info('Extracting Data From the table')
            grid_view4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.GridView")
            
            grid_rows4 = grid_view4.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
            

            while grid_view4:
                print(grid_view4)
                self.driver.page_source

                if grid_view4:
                    for row in grid_rows4:
                        row_items = row.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
                        row_data = [item.text for item in row_items]
                        # print("Row Data:", row_data)
                        if row_data[0] != "Date":
                            
                            if [row_data[0],row_data[1],row_data[2]] not in Reveue_Daily:
                                Reveue_Daily.append([row_data[0],row_data[1],row_data[2]])
                            else:
                                pass
                        else:
                            pass
                            
                    self.driver.swipe(499, 2130, 510, 1778)
                    sleep(random.randint(3,5))
                    try:
                        grid_view4 = self.driver.find_element(AppiumBy.XPATH,value='//android.widget.GridView')
                        grid_rows4 = grid_view4.find_elements(AppiumBy.XPATH, "//android.widget.GridView/android.view.View")
                    except:
                        grid_view4 = None


                with open(csv_file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["date", "uv_today","uv_yesterday","orders_today","orders_yesterday","buyer_today","buyer_yesterday","revenuetoday","revenue_yesterday"])  
                    for item1, item2, item3,item4 in zip(UV_Daily,Orders_Daily,Buyer_Daily, Reveue_Daily):
                        
                        writer.writerow([item1[0],item1[1],item1[2],item2[1],item2[2],item3[1],item3[2],item4[1],item4[2]])


            action.tap(x=50, y=143).perform() 
            sleep(random.randint(3,5))

            action.tap(x=145, y=2277).perform() 
            sleep(random.randint(3,5))


        logger.info('terminating App')
        self.driver.terminate_app('com.sc.lazada')
            
        

if __name__ == '__main__':
    Daily = LazadaVisitorDaily()
    Daily.setUp()
    Daily.run()



