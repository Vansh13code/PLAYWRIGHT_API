from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        viewport={"width": 1400, "height": 900},
        ignore_https_errors=True
    )

    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.reload()

    page.go_back()

    page.go_forward()

    page.wait_for_load_state("networkidle")

    print(page.title())
    print(page.url)

    page.screenshot(path="login.png")

    page.screenshot(
        path="login_full.png",
        full_page=True
    )

    page.locator("input[name='username']").fill("Admin")

    page.locator("input[name='password']").fill("admin123")

    page.locator("button[type='submit']").hover()

    page.locator("button[type='submit']").click()

    page.wait_for_load_state("networkidle")

    print(page.title())

    page.screenshot(path="dashboard.png")

    page.locator("a").first.hover()

    page.locator("a").last.hover()

    page.locator("a").nth(2).hover()

    page.keyboard.press("PageDown")

    page.keyboard.press("PageUp")

    page.keyboard.press("Control+L")

    page.mouse.move(300, 300)

    page.mouse.click(300, 300)

    page.mouse.dblclick(300, 300)

    page.mouse.wheel(0, 800)

    page.locator("span.oxd-userdropdown-tab").click()

    page.locator("text=About").click()

    page.keyboard.press("Escape")

    page.locator("span.oxd-userdropdown-tab").click()

    page.locator("text=Support").click()

    page.go_back()

    page.locator("span.oxd-userdropdown-tab").click()

    page.locator("text=Change Password").click()

    page.go_back()
   context.clear_cookies()

    browser.close()
