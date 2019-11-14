from selenium import webdriver

class WhatsappBot:
    def __init__(self):
        path="/Users/vaibhav/Downloads/chromedriver"
        url="https://web.whatsapp.com/"
        self.driver = webdriver.Chrome(path)
        self.driver.get(url)
        
    def send_message(self, name, msg, count):
        self.name = name
        self.msg = msg
        self.count = count   

        user = self.driver.find_element_by_xpath("//span[@title = '{}']".format(name))
        user.click()

        msg_box = self.driver.find_element_by_class_name('_3u328')

        for i in range(count):
            msg_box.send_keys(msg)
            button = self.driver.find_element_by_class_name('_3M-N-')
            button.click()  

name = input('Enter name of contact : ')
msg = input('Enter message : ')
count = int(input('enter count of msgs : '))
wb = WhatsappBot()
input('enter anything please after scannning qr code : ')
wb.send_message(name, msg, count)