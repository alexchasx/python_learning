
```bash
# Установите Scrapy:
pip install scrapy

# Создайте новый проект:
scrapy startproject new_project
cd new_project

# Сгенерируйте паука с помощью команды:
scrapy genspider <имя_паука> <домен>

# Например
scrapy genspider products example-shop.com 
```

Пример базового паука:

```py
import scrapy

class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['example-shop.com']
    start_urls = ['https://example-shop.com/products']

    def parse(self, response):
        # Извлекаем все карточки товаров
        for product in response.css('div.product-card'):
            yield {
                'name': product.css('h3.product-title::text').get().strip(),
                'price': product.css('span.price::text').get().strip()
            }
```