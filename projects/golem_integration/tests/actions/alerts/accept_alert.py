from golem import actions


description = 'Verify accept_alert action'

def test(data):
    # alert
    actions.navigate(data.env.url+'alert/')
    actions.click('#alert-button')
    actions.verify_alert_present()
    actions.accept_alert()
    actions.verify_alert_not_present()
    actions.verify_text_in_element('#result', '1')
    # confirm
    actions.navigate(data.env.url + 'confirm/')
    actions.click('#confirm-button')
    actions.verify_alert_present()
    actions.accept_alert()
    actions.verify_alert_not_present()
    actions.verify_text_in_element('#result', 'CONFIRMED')
    # prompt
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.verify_alert_present()
    actions.accept_alert()
    actions.verify_alert_not_present()
    actions.verify_text_in_element('#result', 'EMPTY')
