import subprocess
import sys
from selenium import webdriver
import time

def publish(username, password):
    p2 = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
    newip = p2.stdout.decode().strip()
    html_msg='<h>'+newip + '</h>'
    print(html_msg)
    driver = webdriver.Firefox(executable_path=r'/home/riley/scripts/geckodriver')
    driver.get('https://github.com/rlgriffin2/web-ip-gen/edit/master/index.html')
    user_box=driver.find_element_by_id('login_field')
    user_box.send_keys(username)
    pass_box=driver.find_element_by_id('password')
    pass_box.send_keys(password)
    #time.sleep(1)
    login_btn=driver.find_element_by_class_name('btn-block')
    login_btn.click()
    text_box=driver.find_element_by_class_name('CodeMirror-line')
    text_box.click()
    #time.sleep(1)
    text_data=driver.find_element_by_xpath('.//span[@role = "presentation"]')
    driver.execute_script('arguments[0].style=null;', text_data)
    driver.execute_script('arguments[0].textContent = arguments[1];', text_data, newip)
    time.sleep(1)
    commit_btn=driver.find_element_by_id('submit-file')
    jss = "arguments[0].disabled = false;"
    driver.execute_script(jss, commit_btn)
    time.sleep(2)
    commit_btn.click()
    time.sleep(10)


if __name__ == '__main__':
    publish((sys.argv[1]),(sys.argv[2]))
