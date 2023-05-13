import asyncio
from pprint import pprint as print

import httpx


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, urls: list[str]) -> None:
        if ExchangeRates._initialized:
            return
        self.data = []
        self._fetch_from_api(urls)

        ExchangeRates._initialized = True

    def _fetch_from_api(self, urls: list[str]) -> None:
        asyncio.run(self._async_fetch(urls))

    async def _async_fetch(self, urls: list[str]):
        async with httpx.AsyncClient() as client:
            tasks = []
            for url in urls:
                tasks.append(client.get(url))

            results = await asyncio.gather(*tasks)
            self.data = [res.json() for res in results]


url_1 = (
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
    "from_currency=USD&to_currency=UAH&apikey=0L61B1J5AP1II49E"
)
url_2 = (
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
    "from_currency=GBP&to_currency=UAH&apikey=0L61B1J5AP1II49E"
)
url_3 = (
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
    "from_currency=EUR&to_currency=UAH&apikey=0L61B1J5AP1II49E"
)

urls = [url_1, url_2, url_3]

er = ExchangeRates(urls)
print("=== FIRST CALL ===")
print(er.data)

er_2 = ExchangeRates(urls)
print("=== SECOND CALL ===")
print(er_2.data)
