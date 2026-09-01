import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("file:///D:/Creative%20Developer%20Solo/projetos/pessoal/descobrindo/torcida-web/index.html")
        
        # Wait a bit for animations
        await page.wait_for_timeout(1000)
        
        # Screenshot Hero
        await page.screenshot(path="hero.png")
        
        # Scroll to showcase top
        showcase = page.locator("#showcase-top")
        await showcase.scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        
        # Screenshot footer element
        footer = page.locator("#footer")
        await footer.scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        await footer.screenshot(path="footer_preview.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
