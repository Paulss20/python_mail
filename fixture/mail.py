
from selenium.webdriver.support.ui import Select
#from model.add_new import AddNew
import re


class MailHelper:

     def __init__(self, app):
          self.app = app

     def open_add_new_page(self):
          wd = self.app.wd
          wd.find_element_by_link_text("add new").click()

     def change_field_contact_value(self, field_name, text):
          wd = self.app.wd
          if text is not None:
               wd.find_element_by_name(field_name).click()
               wd.find_element_by_name(field_name).clear()
               wd.find_element_by_name(field_name).send_keys(text)

#     contact_cache = None

     def fill_contact_form(self, add_new):
          wd = self.app.wd
          self.change_field_contact_value("firstname", add_new.my_f_name)
          self.change_field_contact_value("middlename", add_new.my_m_name)
          self.change_field_contact_value("lastname", add_new.my_l_name)
          self.change_field_contact_value("nickname", add_new.my_nickname)
          self.change_field_contact_value("company", add_new.my_company)
          self.change_field_contact_value("address", add_new.work_address)
          self.change_field_contact_value("home", add_new.my_h_telefon)
          self.change_field_contact_value("mobile", add_new.my_mobile)
          self.change_field_contact_value("work", add_new.my_work_telefon)
          self.change_field_contact_value("fax", add_new.my_fax)
          self.change_field_contact_value("email", add_new.my_company_mail)
          self.change_field_contact_value("email2", add_new.my_second_mail)
          self.change_field_contact_value("email3", add_new.my_third_mail)
          self.change_field_contact_value("homepage", add_new.my_homepage)
          wd.find_element_by_name("bday").click()
          Select(wd.find_element_by_name("bday")).select_by_visible_text("7")
          wd.find_element_by_xpath("//option[@value='7']").click()
          wd.find_element_by_name("bmonth").click()
          Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
          wd.find_element_by_xpath("//option[@value='August']").click()
          self.change_field_contact_value("byear", add_new.my_byear)
          self.change_field_contact_value("address2", add_new.my_home_address)
          self.change_field_contact_value("phone2", add_new.my_secondary_phone)
          self.change_field_contact_value("notes", add_new.my_notes)

     def create_contact(self, add_new):
          wd = self.app.wd
          self.open_add_new_page()
          self.fill_contact_form(add_new)
          # submit add_new creation
          wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
#          self.return_to_home_page()
          self.open_home_tab()
          self.contact_cache = None

     def open_home_tab(self):
          wd = self.app.wd
          if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
               wd.find_element_by_link_text("home").click()

     def select_first_contact(self):
          wd = self.app.wd
          wd.find_element_by_name("selected[]").click()

     def select_contact_by_index(self, index):
          wd = self.app.wd
          wd.find_elements_by_name("selected[]")[index].click()

     def select_contact_by_id(self, id):
          wd = self.app.wd
          wd.find_element_by_css_selector("input[value='%s']" % id).click()

     def delete_first_contact(self):
          self.delete_contact_by_index(0)