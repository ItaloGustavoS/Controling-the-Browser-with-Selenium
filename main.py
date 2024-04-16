from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://nostarch.com/automatestuff2")

elem = browser.find_element_by_css_selector(
    "div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
)

elems = browser.find_elements_by_css_selector("p")

searchElem = browser.find_elements_by_selector(
    "div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
)

searchElem.send_keys("Ola")
searchElem.submit()

browser.quit()
