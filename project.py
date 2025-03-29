import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def setup_driver(browser_type='chrome'):
    """
    Setting up the appropriate webdriver based on browser type.
    """
    if browser_type.lower() == 'firefox':
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager
        return webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser_type.lower() == 'chrome':
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        raise ValueError("Unsupported browser type")

def post_to_facebook(driver, image_path, caption):
    """
    Post to Facebook if you're logged in.
    """
    try:
        driver.get('https://www.facebook.com/')

        try:
            driver.find_element(By.XPATH, "//div[@aria-label='Create']")
        except NoSuchElementException:
            print("Not logged into Facebook, log in and try again")
            return False

        create_post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Create']"))
        )
        create_post_button.click()

        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_input.send_keys(os.path.abspath(image_path))

        caption_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        )
        caption_input.send_keys(caption)

        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post']"))
        )
        post_button.click()

        return True
    except Exception as e:
        print(f"Facebook upload failed: {e}")
        return False

def post_to_instagram(driver, image_path, caption):
    """
    Post to Instagram if you're logged in.
    """
    try:
        driver.get('https://www.instagram.com/')

        try:
            driver.find_element(By.XPATH, "//a[@href='/create']")
        except NoSuchElementException:
            print("Not logged into Instagram, log in and try again")
            return False

        create_post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/create']"))
        )
        create_post_button.click()

        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_input.send_keys(os.path.abspath(image_path))

        caption_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Write a caption…']"))
        )
        caption_input.send_keys(caption)

        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Share')]"))
        )
        post_button.click()

        return True
    except Exception as e:
        print(f"Instagram uploading failed: {e}")
        return False

def post_to_x(driver, image_path, caption):
    """
    Post to X (Twitter) if you're logged in.
    """
    try:
        driver.get('https://x.com/')

        try:
            driver.find_element(By.XPATH, "//a[@href='/compose/post']")
        except NoSuchElementException:
            print("Not logged into X, log in and try again")
            return False

        create_post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/compose/post']"))
        )
        create_post_button.click()

        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_input.send_keys(os.path.abspath(image_path))

        caption_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        )
        caption_input.send_keys(caption)

        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweet-button']"))
        )
        post_button.click()

        return True
    except Exception as e:
        print(f"X uploading failed: {e}")
        return False

def main():
    """
    Main function to demonstrate the usage.
    """
    driver = setup_driver()
    try:
        image_path = 'path/to/your/image.jpg'  # Change this to your image path
        caption = 'Your caption here!'  #Change this to your desired caption

        results = {
            'Facebook': post_to_facebook(driver, image_path, caption),
            'Instagram': post_to_instagram(driver, image_path, caption),
            'X': post_to_x(driver, image_path, caption)
        }

        for platform, success in results.items():
            print(f"{platform}: {'uploaded successfully' if success else 'uploading failed'}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
