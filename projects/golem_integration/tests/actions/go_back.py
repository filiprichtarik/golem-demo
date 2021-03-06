from golem import actions
from golem import browser

description = 'Verify go_back action'

def test(data):
    actions.navigate(data.env.url)
    actions.click(('link_text', 'Elements'))
    assert browser.get_browser().current_url == data.env.url+'elements/'
    actions.go_back()
    assert browser.get_browser().current_url == data.env.url