import asyncio
from playwright.async_api import async_playwright


async def get_image_sources(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)

        # Wait for the cookie banner to appear
        await page.wait_for_selector('#onetrust-button-group')

        # Click the "Accept All Cookies" button
        await page.click('#onetrust-accept-btn-handler')

        # Wait for the cookie banner to disappear
        await page.wait_for_selector('#onetrust-button-group', state='hidden')

        # Get the div element by its id
        div_data_pages = page.locator('div[class="pagination-dropdown"]').nth(0)

        # Get the value of the data-pages attribute
        data_pages = await div_data_pages.get_attribute('data-pages')

        # Collect image sources
        for i in range(1, int(data_pages)):
            div_selector = 'div[data-qa="search-results"]'
            await page.wait_for_selector(div_selector)
            div_elements = await page.query_selector_all(div_selector)
            for div_element in div_elements:
                img_element = await div_element.query_selector('img')
                img_src = await img_element.get_attribute('src')
                with open('aldi-api-image.txt', 'a') as f:
                    img_src = img_src.replace("_M.jpg", "_XL.jpg")
                    f.write(img_src + '\n')
            next_button = await page.query_selector('a.btn-nav.bg-white[title="Next"]')
            if not next_button:
                break
            await next_button.click()
            await asyncio.sleep(2)
        await browser.close()

if __name__ == '__main__':
    url = 'https://groceries.aldi.co.uk/en-GB/bakery'
    asyncio.run(get_image_sources(url))
