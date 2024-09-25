from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

# إعداد Selenium
def fetch_title():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # لتشغيل Chrome بدون واجهة
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # إعداد ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # زيارة موقع ويب
    driver.get("https://example.com")
    
    # استخراج عنوان الصفحة
    title = driver.title
    driver.quit()
    return title

@app.route('/')
def home():
    # استدعاء وظيفة Selenium للحصول على عنوان الصفحة
    page_title = fetch_title()
    return f'The page title is: {page_title}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
