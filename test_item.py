import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_presence_of_add_to_basket_button(browser):
    browser.get(link)
    #time.sleep(30)
    basket_buttons = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert len(basket_buttons)==1, 'Selector is not unique.'
