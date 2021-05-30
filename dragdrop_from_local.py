from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import os.path

# JavaScript: HTML5 File drop
# source            : https://gist.github.com/florentbr/0eff8b785e85e93ecc3ce500169bd676
# param1 WebElement : Drop area element
# param2 Double     : Optional - Drop offset x relative to the top/left corner of the drop area. Center if 0.
# param3 Double     : Optional - Drop offset y relative to the top/left corner of the drop area. Center if 0.
# return WebElement : File input
JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"

def drop_files(element, files, offsetX=0, offsetY=0):
    driver = element.parent
    isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
    paths = []
    
    # ensure files are present, and upload to the remote server if session is remote
    for file in (files if isinstance(files, list) else [files]) :
        if not os.path.isfile(file) :
            raise FileNotFoundError(file)
        paths.append(file if isLocal else element._upload(file))
    
    value = '\n'.join(paths)
    elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

WebElement.drop_files = drop_files

def auto_submit(path_to_chrome_driver, checker_web, login, path_to_files):
    driver = webdriver.Chrome(
    executable_path = path_to_chrome_driver
                        )
    driver.get(checker_web)
    driver.find_element_by_id("checker_login_email").send_keys(login)
    python_button = driver.find_element_by_id("login_close")
    python_button.click()
    dropzone = driver.find_elements_by_xpath("/html/body")[0]
    if len(path_to_files) > 1:
        dropzone.drop_files(path_to_files)
    else:
        dropzone.drop_files(path_to_files[0])

if __name__ == '__main__':
    #Give path to chrome driver
    path_to_chrome_driver ="C:\\Users\\conma\\OneDrive - Cal State Fullerton\\Work-Related Documents\\SCCWRP\\Projects\\BLM\\chromedriver.exe" 
    checker_web = 'https://ceriochecker.sccwrp.org/checker/'
    login = 'test@sccwrp.org'
    path_to_files = ["C:\\Users\\conma\\OneDrive\\Desktop\\fromDarrin-rptCerioDataSheet.xlsx"]
    auto_submit(path_to_chrome_driver, checker_web, login, path_to_files)



    
############################# USAGE EXAMPLE #############################

# driver = webdriver.Chrome()

# driver.get("https://react-dropzone.js.org/")
# dropzone = driver.find_element_by_css_selector("[data-preview='Basic example'] [style]")

# # drop a single file
# dropzone.drop_files("C:\\temp\\image1.png")

# # drop two files
# dropzone.drop_files(["C:\\temp\\image1.png", "C:\\temp\\image2.png"])

# # drop a file by offset
# dropzone.drop_files("C:\\temp\\image1.png", offsetX=25, offsetY=25) 