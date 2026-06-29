class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self, username):
        self.page.locator("input[name='username']").fill(username)

    def enter_password(self, password):
        self.page.locator("input[name='password']").fill(password)

    def click_login(self):
        self.page.locator("button[type='submit']").click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
