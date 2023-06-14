import asyncio
from playwright.async_api import async_playwright


async def get_divs(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        cookie = {
            "name": "CONSENT",
            "value": "YES+42",
            "url": "https://groceries.aldi.co.uk"
        }
        await context.add_cookies([cookie])
        div_selector = 'div[data-qa="search-results"]'
        await page.wait_for_selector(div_selector)
        div_elements = await page.query_selector_all(div_selector)
        for div_element in div_elements:
            div_html = await div_element.inner_html()
            print(div_html)
        await browser.close()

if __name__ == '__main__':
    url = 'https://groceries.aldi.co.uk/en-GB/bakery'
    asyncio.run(get_divs(url))
