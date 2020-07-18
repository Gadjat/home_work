import time

link = "http://selenium1py.pythonanywhere.com"
mail_pass = str(time.time()) + "@stepik.ru"


def test_registration_successfully(browser):
    browser.get(link)
    browser.find_element_by_id("login_link").click()
    browser.find_element_by_css_selector("#id_registration-email").send_keys(mail_pass)
    browser.find_element_by_css_selector("#id_registration-password1").send_keys(mail_pass)
    browser.find_element_by_css_selector("#id_registration-password2").send_keys(mail_pass)
    browser.find_element_by_name("registration_submit").click()
    welcome_text = browser.find_element_by_class_name("alertinner.wicon").text
    assert "Thanks for registering!" == welcome_text, "Authorization failed"
