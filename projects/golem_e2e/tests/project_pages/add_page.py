
description = 'Verify the user can create a new page from the project page'

pages = ['login',
         'common',
         'index',
         'project_pages']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Pages')

def test(data):
    store('page_name', 'page_' + random('cccc'))
    project_pages.add_page(data.page_name)
    project_pages.verify_page_exists(data.page_name)
