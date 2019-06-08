Ну, удачи.
from selenium import webdriver
safari = webdriver.Safari()
safari.get("https://www.ultimateqa.com/complicated-page/")
safari.find_elements_by_link_text("Button")[0].click()

safari.get("https://www.ultimateqa.com/complicated-page/")
safari.find_element_by_id("s").send_keys("qwerty")
safari.find_element_by_id("searchsubmit").click()

safari.get("https://www.ultimateqa.com/complicated-page/")
safari.find_element_by_name("email").send_keys("qwerty@mail.ru")
safari.find_element_by_name("jetpack_subscriptions_widget").click()

safari.get("https://www.ultimateqa.com/complicated-page/")
safari.find_element_by_name("et_pb_contact_name_0").send_keys("aliosha")
safari.find_element_by_name("et_pb_contact_email_0").send_keys("qwerty@mail.ru")
safari.find_element_by_name("et_pb_contact_message_0").send_keys("123qwerty")

safari.get("https://www.ultimateqa.com/complicated-page/")
safari.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//input[@name="log"]').send_keys("asd")
safari.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//input[@name="pwd"]').send_keys("1234567")
safari.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//button[@class="et_pb_newsletter_button et_pb_button"]').click()

safari.get("https://www.ultimateqa.com/complicated-page/")
safari.find_element_by_xpath('//div[@class="et_pb_row et_pb_row_4"]//a[@title="Follow on Twitter"]').click()
