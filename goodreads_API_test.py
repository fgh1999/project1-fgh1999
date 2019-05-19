import requests

res = requests.get("https://www.goodreads.com/book/review_counts.json",
                   params={"isbns": "0441172717"})
# postman里不加key也可以得到结果，但是这里面无论是否加上key都不能得到结果……
print(res.json())
