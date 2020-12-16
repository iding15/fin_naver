import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class sel:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
    def ClickTool(self, Type, name):
        if Type == "id":
            return self.driver.find_element_by_id(name).click()
        if Type == "xpath":
            return self.driver.find_element_by_xpath(name).click()
    def DragDrop(self, drag, drop):
        sType = drag[0]
        sName = drag[1]
        tType = drop[0]
        tName = drop[1]
        if sType == "xpath":
            source = self.driver.find_elements_by_xpath(sName)
            s = source[0]
        if tType == "xpath":
            target = self.driver.find_elements_by_xpath(tName)
            t = target[-1]
        # if tType == "class":
        #     target = self.driver.find_element_by_class_name(tName)
        action = ActionChains(self.driver)
        return action.click_and_hold(s).move_to_element(t).release(t).perform()
    def table(self, thead, tbody, header=True):
        data = []
        if header==True:
            tableH = self.driver.find_element_by_xpath(thead)
            tr_head = tableH.find_elements_by_tag_name("tr")[0]
            th = tr_head.find_elements_by_tag_name("th")
            l_head = []
            for i in th:
                l_head.append(i.text)
            data.append(l_head)
        tableB = self.driver.find_element_by_xpath(tbody)
        tr_body = tableB.find_elements_by_tag_name("tr")
        for tr in tr_body:
            l_td = tr.find_elements_by_tag_name("td")
            l_ = []
            for td in l_td:
                l_.append(td.text)
            data.append(l_)
        return data
    def driverClose(self):
        return self.driver.close()
    
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# **drag and drop example**

# #browser exposes an executable file
# #Through Selenium test we will invoke the executable file which will then
# #invoke actual browser
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# # to maximize the browser window
# driver.maximize_window()
# #get method to launch the URL
# driver.get("https://jqueryui.com/droppable/")
# #to refresh the browser
# driver.refresh()
# # identifying the source and target elements
# source= driver.find_element_by_id("draggable");
# target= driver.find_element_by_id("droppable");
# # action chain object creation
# action = ActionChains(driver)
# # drag and drop operation and the perform
# action.drag_and_drop(source, target).perform()
# driver.close()

# **get table**
# table = driver.find_element_by_xpath("//*[@id='resultsTable']/tbody")

# for tr in table.find_elements_by_tag_name("tr"):
#     td = tr.find_elements_by_tag_name("td")
#     s = "{} , {}\n".format(td[1].text , td[2].text)
#     #print (s)
#     fp.write(s)