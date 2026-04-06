import httpx
import time
import asyncio

async def test_proxy_connection(proxy_url: str):
    """
    Async logic to test a proxy URL and return detailed metadata.
    Used by the Admin Hub to verify active proxies.
    """
    results = {
        'success': False,
        'response_ms': 0,
        'ip': '',
        'location': 'Unknown',
        'error': None
    }
    
    if not proxy_url:
        results['error'] = "Empty proxy URL"
        return results

    if not proxy_url.startswith('http'):
        proxy_url = f"http://{proxy_url}"

    start_time = time.perf_counter()
    try:
        async with httpx.AsyncClient(proxies=proxy_url, timeout=10.0, verify=False) as client:
            # We use an IP reflection service to get the proxy's real outbound IP
            resp = await client.get("https://api.ipify.org?format=json")
            if resp.status_code == 200:
                results['success'] = True
                results['ip'] = resp.json().get('ip', 'Unknown')
                results['response_ms'] = int((time.perf_counter() - start_time) * 1000)
                
                # Optional: Deep location lookup
                try:
                    loc_resp = await client.get(f"https://ipapi.co/{results['ip']}/json/", timeout=5.0)
                    if loc_resp.status_code == 200:
                        data = loc_resp.json()
                        results['location'] = f"{data.get('city', 'Unknown')}, {data.get('country_name', 'Unknown')}"
                except:
                    pass
            else:
                results['error'] = f"HTTP {resp.status_code}"
    except Exception as e:
        results['error'] = str(e)
        
    return results
