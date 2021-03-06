from golem import actions


description = 'Verify wait_for_element_not_present action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_element_present('#button-six')
    actions.wait_for_element_not_present('#button-six', timeout=10)
    actions.verify_element_not_present('#button-six')
    # when element does not exist no exception is thrown
    actions.wait_for_element_not_present('#this-element-does-not-exist', timeout=3)
    # wait times out and element is still present
    actions.navigate(data.env.url + 'elements/')
    try:
        actions.wait_for_element_not_present('#button-one', timeout=3)
    except Exception as e:
        assert "Timeout waiting for element #button-one to not be present" in e.args[0]
