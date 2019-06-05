from selenium import webdriver


def browser_init(context):
    """
    :param context: Behave context
    :param url: root url of the pages
    """
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--window-size=1280,720")
    options.add_argument("--disable-gpu")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    #options.add_argument("headless")
    #context.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
    context.driver = webdriver.Chrome(chrome_options=options)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

# def Background (Logged_in as a site owner)
# (/ Users / margarita / Downloads / automation_example - master / features / steps / fountain_login_first.py)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
