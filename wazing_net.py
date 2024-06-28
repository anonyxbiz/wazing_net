# wazing_net.py
from httpx import AsyncClient
p = print

class Route:
    def __init__(app) -> None:
        pass
    async def get(app, url=None, headers={}, params={}, timeout=60):
        if url is None:
            return 'url is required'
        try:
            async with AsyncClient() as client:
                r = await client.get(url, headers=headers, params=params, timeout=timeout)
                return r
        except Exception as e:
            return ('wazing_net_exception', f"Error fetching {url}: {str(e)}")

    async def post(app, url=None, headers={}, data={}, json={}, timeout=60):
        if url is None:
            return 'url is required'
        try:
            async with AsyncClient() as client:
                if json != {}:
                    r = await client.post(url, headers=headers, json=json)
                else:
                    if data != {}:
                        r = await client.post(url, headers=headers, data=data)
                    else:
                        r = False
                if r:
                    return r
                
        except Exception as e:
            return ('wazing_net', f"Error fetching {url}: {str(e)}")

route = Route()

if __name__ == "__main__":
    pass
