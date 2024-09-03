# Import necessary Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Make browser open in background
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create the webdriver object
browser = webdriver.Chrome(options=options)

# List of Google Map URLs
urls = [
    "https://www.google.com/maps/place/Wazwan+Restaurant,+JKTDC/data=!4m7!3m6!1s0x391e85c5e713a921:0x1b10640828209a!8m2!3d32.7291722!4d74.8649185!16s%2Fg%2F11szjw9yls!19sChIJIakT58WFHjkRmiAoCGQQGwA?authuser=0&hl=en&rclk=1",
    "https://www.google.com/maps/place/Lucky+Dhaba/@30.653792,76.8165233,17z/data=!3m1!4b1!4m5!3m4!1s0x390feb3e3de1a031:0x862036ab85567f75!8m2!3d30.653792!4d76.818712"
]

def get_element_text(browser, by, value, default="Not available"):
    """Utility function to get the text of an element or return a default message if not found."""
    try:
        return browser.find_element(by, value).text
    except:
        return default

def scrape_google_maps(url):
    """Scrape information from a Google Maps page."""
    browser.get(url)

    # Scraping required details
    title = get_element_text(browser, By.CLASS_NAME, "DUwDvf")
    stars = get_element_text(browser, By.CLASS_NAME, "F7nice")
    description = get_element_text(browser, By.CLASS_NAME, "tAiQdd")
    address = get_element_text(browser, By.CLASS_NAME, "Io6YTe")
    
    # Assuming the contact number might be the second last 'Io6YTe' element
    phone = get_element_text(browser, By.CLASS_NAME, "Io6YTe", default="Not available")
    
    # Gather all reviews
    reviews = browser.find_elements(By.CLASS_NAME, "jftiEf")
    reviews_text = "\n".join([review.text for review in reviews])

    return {
        "Title": title,
        "Stars": stars,
        "Description": description,
        "Address": address,
        "Contact Number": phone,
        "Reviews": reviews_text
    }

# Loop through each URL and scrape data
for i, url in enumerate(urls, start=1):
    data = scrape_google_maps(url)
    print(f"{i} - {data['Title']}")
    print(f"The stars of the restaurant are: {data['Stars']}")
    print(f"Description: {data['Description']}")
    print(f"Address: {data['Address']}")
    print(f"Contact Number: {data['Contact Number']}")
    print("------------------------ Reviews --------------------")
    print(data['Reviews'])
    print("\n")

# Close the browser after scraping
browser.quit()
