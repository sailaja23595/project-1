import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": " 69VoalPUF1wQ0rnUF2DRg", "isbns": "9781632168146"})
print(res.json())