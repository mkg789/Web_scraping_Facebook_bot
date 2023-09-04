import praw
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# web driver instance
driver = webdriver.Edge()

# opens facebook login page
driver.get('https://www.facebook.com')

# login id
driver.find_element('id', 'email').send_keys('your email')

# password
driver.find_element('id', 'pass').send_keys('password')

# click on login button
driver.find_element('name', 'login').click()

# 5secs loading time
time.sleep(5)

# open profile page in fb account
driver.get('https://www.facebook.com/profile.php?id=your_id')

# 10secs loading time
time.sleep(10)

# finding the add photos and video button
element = driver.find_element('xpath', '//span[text()="Photo/video"]')

# to click the add pics\video button
driver.execute_script("arguments[0].click();", element)

# 2secs time
time.sleep(5)

# Initialize a Reddit instance
reddit = praw.Reddit(client_id='your client id',
                     client_secret='your client secret',
                     user_agent='your user agent')

# Access a subreddit
subreddit = reddit.subreddit('ProgrammerHumor')

# Fetch the top posts from the subreddit
top_posts = subreddit.top(limit=1)

# to check if its true or false
print(reddit.read_only)

# directory to download and save images
save_directory = r"C:\Users\mural\OneDrive\Desktop\github\Automating FaceBook Activities\reddit pics"

# to give images unique numbers
i = 0

# finding image file for input
image_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/input')

# looping the number of posts
for post in top_posts:

    # Wait for the rich text input area to be visible
    rich_text_div = driver.find_element(By.CSS_SELECTOR, ".xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x9f619.x1lliihq.x5yr21d.xh8yej3.notranslate")

    # Enter text or content into the rich text input area
    rich_text_div.send_keys(f'{post.title}')

    # url of images
    image_url = post.url

    # Download the image
    response = requests.get(f'{image_url}')
    with open(f'{save_directory}image{i}.jpg', 'wb') as f:
        f.write(response.content)
        i += 1
    time.sleep(5)
    # Find the file input element
    wait = WebDriverWait(driver, 10)


# Sleep for a short duration (optional)
    time.sleep(4)

    # Specify the file path, and send the keys
    image_path = f'{save_directory}image{i}.jpg'
    image_input.send_keys(image_path)
    time.sleep(15)

    # find the post button
    button = driver.find_element('xpath', '//span[text()="Post"]')

    # to click the Post button
    driver.execute_script("arguments[0].click();", button)
    time.sleep(25)

# exit driver
driver.quit()
print('Post Uploaded')
