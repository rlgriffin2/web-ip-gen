import subprocess
import sys
from selenium import webdriver
#firstIP = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode()
#p1 = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
#oldip = p1.stdout.decode()


def publish(username, password):
    p2 = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
    newip = p2.stdout.decode()
    newip.replace('\n', '')
    html_msg='<h>'+newip+'</h>'
    print(html_msg)
    #subprocess.call(['./publishIP', '-$newip', '-$username', '-$password'])
    driver = webdriver.Firefox(executable_path=r'/home/riley/scripts/geckodriver')
    driver.get('https://github.com/rlgriffin2/web-ip-gen/edit/master/index.html')
    user_box=driver.find_element_by_id('login_field')
    user_box.send_keys(username)
    pass_box=driver.find_element_by_id('password')
    pass_box.send_keys(password)
    login_btn=driver.find_element_by_class_name('btn-block')
    login_btn.click()
    text_box=driver.find_element_by_class_name('CodeMirror-line')
    text_box.click()
    #wait
    #text_data1=driver.find_element_by_css_selector('div.pre.CodeMirror-line > span')
    text_data=driver.find_element_by_xpath('.//span[@role = "presentation"]')
    #for elem in driver.find_elements_by_xpath('.//span[@role = "presentation"]'):
    #    print(elem.text)
    #    print('mmmmmmm')
    driver.execute_script("arguments[0].innerText = arguments[1]", text_data, html_msg)

if __name__ == '__main__':
    publish((sys.argv[1]),(sys.argv[2]))
