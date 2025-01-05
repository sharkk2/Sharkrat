import requests
from core.logger.logger import logger

def get_ip_info(ip: str = "me") -> dict:
    """
    Get information about an IP address.

    Parameters:
        ip (str): The IP address to look up. Use 'me' to get info for your own IP.
    
    Returns:
        dict: A dictionary containing IP information.
    """
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to get IP info for {ip}: {e}")
        return {}
