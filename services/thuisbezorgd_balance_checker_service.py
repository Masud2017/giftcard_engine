from bs4 import BeautifulSoup
import requests

from playwright.sync_api import sync_playwright



class ThuisbezorgdBalanceChecker:
    def __init__(self):
        self.card_number_input = r"//input[@method='replace' and @name='number']"
        self.pin_input = r"//input[@method='replace' and @name='pin']"
        
    def scrap(self):
        try:
            with sync_playwright() as p:
                        browser = p.chromium.launch(headless=False)
                        page = browser.new_page()
                        page.goto("https://www.thuisbezorgd.nl/en/gift-cards/saldocheck")
                        page.locate(f"xpath = {self.card_number_input}").fill(2432322)
                        page.wait_for_selector("replace")
                        input("shdfds")
                        print(page.title())
                        page.wait_for_selector("div")
                        browser.close()
        except Exception as e:
            import traceback; traceback.format_exception(e);            
# import asyncio; asyncio.run(ThuisbezorgdBalanceChecker().scrap())
ThuisbezorgdBalanceChecker().scrap()