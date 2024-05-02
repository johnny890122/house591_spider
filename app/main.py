import json
import requests
from bs4 import BeautifulSoup
from house591_spider import House591Spider
import utils

def lambda_handler(event, context):
    # body = json.loads(event["body"])
    # url = body["url"]
    # sort_params = body["sort_params"]

    url = "https://rent.591.com.tw/?region=3&section=26,50,38&searchtype=1&other=cook,balcony_1&multiArea=30_40,40_50&showMore=1"
    sort_params = {
        'order': 'money',  # posttime, area
        'orderType': 'desc'  # asc
    }

    house591_spider = House591Spider()
    filter_params = utils.parse_url_arguments(url)
    total_count, houses = house591_spider.search(filter_params, sort_params, want_page=1)
    for house in houses:
        post_id = house["post_id"]
        house_detail = house591_spider.house_detail(post_id)
        break
    
    res = utils.parse_detail(house_detail)
    return {
        "statusCode": 200,
        "body": json.dumps(res),
    }
