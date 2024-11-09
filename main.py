import time
from selenium import webdriver
from selenium_stealth import stealth

options = webdriver.ChromeOptions()

options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

print("Starting Chrome headless browser...")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://www.tiktok.com/@tiktok"

driver.get(url)

print("Waiting for msToken...")

start_time = time.time()
timeout = 30
mstoken = None

while time.time() - start_time < timeout:
    mstoken = driver.get_cookie('msToken')
    if mstoken and len(mstoken['value']) not in [108, 124, 128]: # [108, 124, 128] length msToken seems to be invalid        
        elapsed_time = time.time() - start_time
        print(f"[{len(mstoken['value'])}] Valid msToken found in {elapsed_time:.2f} seconds: {mstoken['value']}")
        # Valid mstoken length seems to be [144, 148, 152] but this is not always the case ¯\_(ツ)_/¯
        break        
    time.sleep(0.5)
else:
    print("Timeout: Could not find valid msToken within 30 seconds")

driver.quit()
