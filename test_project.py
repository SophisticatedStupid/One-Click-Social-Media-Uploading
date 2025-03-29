import pytest
import os
from project import setup_driver, post_to_facebook, post_to_instagram, post_to_x
from PIL import Image

@pytest.fixture
def test_image():
    """
    Create a test pic for posting.
    """
    test_image_path = 'test_image.jpg'
    test_image = Image.new('RGB', (100, 100), color='red')
    test_image.save(test_image_path)
    yield test_image_path
    # Clean up
    if os.path.exists(test_image_path):
        os.remove(test_image_path)

@pytest.fixture
def driver():
    """
    Set up browser's webdriver for testing.
    """
    driver = setup_driver()
    yield driver
    driver.quit()

def test_setup_driver():
    """
    Test driver setting-up function.
    """
    driver = setup_driver()
    assert driver is not None
    driver.quit()

def test_post_to_facebook(driver, test_image):
    """
    Test Facebook uploading functionality.
    """
    result = post_to_facebook(driver, test_image, 'Test Facebook post')
    assert isinstance(result, bool)

def test_post_to_instagram(driver, test_image):
    """
    Test Instagram uploading functionality.
    """
    result = post_to_instagram(driver, test_image, 'Test Instagram post')
    assert isinstance(result, bool)

def test_post_to_x(driver, test_image):
    """
    Test X(Twitter) uploading functionality.
    """
    result = post_to_x(driver, test_image, 'Test X post')
    assert isinstance(result, bool)
