from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://instagram.com')
time.sleep(3)

username = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
username.send_keys("username")

password = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
password.send_keys("password")

login = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
login.click()

time.sleep(8)

driver.get('https://www.instagram.com/explore/tags/cakes')
time.sleep(10)

post = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]")
post.click()

time.sleep(3)

like = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
like.click()

time.sleep(3)

save_post = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button")
save_post.click()

time.sleep(3)

comments = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
comments.click()

time.sleep(2)

comments = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
comments.click()
comments.send_keys("Amazing!!")

time.sleep(2)

post = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div[2]/div")
post.click()

time.sleep(2)

next_post = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button")
next_post.click()

time.sleep(2)
for i in range(1,5):
    like = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
    like.click()

    time.sleep(2)

    save_post = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button")
    save_post.click()

    time.sleep(2)

    comments = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
    comments.click()

    time.sleep(2)

    comments = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
    comments.click()
    comments.send_keys("Amazing!!")

    time.sleep(2)

    post = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div[2]/div")
    post.click()

    time.sleep(2)

    next_post1 = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
    next_post1.click()

driver.quit()

