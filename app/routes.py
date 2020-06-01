from yggdrasil_client import ygg_client, generate_client_args

from . import app


@app.route('/')
def index():
    data = {"target": "https://mp.weixin.qq.com/s/QcYfBAZy0pV2nQXFGeWaWQ"}
    # client = spider_client
    client = ygg_client.get("ss")
    print(f"get client: <{client}>")
    if not client:
        client = ygg_client.create_client("ss", host='qunluo-apis-test-01.guokr.com')
        ygg_client.set_header_callback('ss', generate_headers)
    print(f"client: {client}")
    resp = client.spider.v1.scraping.post(data=data)
    # resp = spider_client.spider.v1.scraping.post(data=data)
    print(f"resp client: {client}")
    print(f"from ygg_client: {ygg_client.ss}")
    print(f"from ygg_client access: {ygg_client['ss']}")
    print(f"dir of ygg_client:\n{dir(ygg_client)}")
    print(resp)
    return "OK", 200


def generate_headers():
    headers = {
        'User-Agent': 'pycharm/flask'
    }
    return headers
