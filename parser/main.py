# login_parser.py
import asyncio
from datetime import datetime

from playwright.async_api import async_playwright

today = datetime.today().day
async def run():
    url = "https://dl.nure.ua/"
    username = ""
    password = ""

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(url)
        await page.click("a[href*='login/index.php']")
        await page.fill("#username", username)
        await page.fill("#password", password)
        await page.click("#loginbtn")
        await page.wait_for_load_state("networkidle")
        await page.click("img.userpicture")
        await page.click("a[href*='calendar/view.php']")
        selector = f".day-number-circle .day-number:text-is('{today}')"
        day_element = await page.query_selector(selector)
        if not day_element:
            print("❌ Current day was not found in calendar.")
            await browser.close()
            return

        print("✅ Found current day in calendar.")
        day_block = await day_element.evaluate_handle(
            "el => el.closest('div.d-none.d-md-block')")
        day_block_el = day_block.as_element()
        event_links = await day_block_el.query_selector_all(
            "a:has-text('Відвідування')")

        if not event_links:
            print("⚠️ No attendance events found.")
        await page.wait_for_load_state("networkidle")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(run())
