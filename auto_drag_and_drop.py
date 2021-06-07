# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import pandas as pd
# from datetime import date
# from datetime import datetime
# import time
# import numpy as np
# from selenium.common.exceptions import NoSuchElementException
# from sqlalchemy import create_engine
# from dragdrop_from_local import *

# def captureTable(driver,list_df, multiPage):
#     table = driver.find_elements_by_id('main_GVLookup')
#     df = pd.read_html(table[0].get_attribute('outerHTML'))[0]
#     if multiPage:
#         df.drop(df.tail(2).index, inplace = True) 
#     list_df.append(df)

# path_to_driver ="C:\\Users\\conma\\OneDrive - Cal State Fullerton\\Work-Related Documents\\SCCWRP\\Projects\\BLM\\chromedriver.exe" 

# driver = webdriver.Chrome(
#     executable_path = path_to_driver
#                         )

# driver.get('https://ceriochecker.sccwrp.org/checker/')
# path_to_login_info  ='/html/body/div[10]/div[2]/div[1]/input'
# path_to_sign_in = '//*[@id="login_info_close"]'
# login_info = 'test@sccwrp.org'
# driver.find_element_by_xpath(path_to_login_info).send_keys(login_info)
# python_button = driver.find_elements_by_xpath(path_to_sign_in)[0]
# python_button.click()

# JS_DROP_FILE = """
#     var target = arguments[0],
#         offsetX = arguments[1],
#         offsetY = arguments[2],
#         document = target.ownerDocument || document,
#         window = document.defaultView || window;

#     var input = document.createElement('INPUT');
#     input.type = 'file';
#     input.onchange = function () {
#       var rect = target.getBoundingClientRect(),
#           x = rect.left + (offsetX || (rect.width >> 1)),
#           y = rect.top + (offsetY || (rect.height >> 1)),
#           dataTransfer = { files: this.files };

#       ['dragenter', 'dragover', 'drop'].forEach(function (name) {
#         var evt = document.createEvent('MouseEvent');
#         evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
#         evt.dataTransfer = dataTransfer;
#         target.dispatchEvent(evt);
#       });

#       setTimeout(function () { document.body.removeChild(input); }, 25);
#     };
#     document.body.appendChild(input);
#     return input;
# """
# 1/0



        
        
        
    