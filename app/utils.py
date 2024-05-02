from urllib.parse import urlparse, parse_qs
from typing import Dict

def parse_url_arguments(url: str):
    """
    Parse the query parameters from a given URL.

    Args:
        url (str): The URL to parse.

    Returns:
        dict: A dictionary containing the parsed query parameters.

    Raises:
        ValueError: If the URL scheme is invalid or not supported,
                    if the netloc (domain) is missing,
                    or if there are no query parameters in the URL.
    """

    parsed_url = urlparse(url)
    # Check if the scheme is present and is http or https
    if not parsed_url.scheme or parsed_url.scheme not in ['http', 'https']:
        raise ValueError("Invalid URL scheme. Only 'http' and 'https' are supported.")
    
    # Check if the netloc (domain) is present
    if not parsed_url.netloc:
        raise ValueError("Invalid URL. Netloc (domain) is missing.")
    
    # Check if there are query parameters
    if not parsed_url.query:
        raise ValueError("No query parameters found in the URL.")
    
    query_params = parse_qs(parsed_url.query)

    return {key: value[0] if len(value) == 1 else value for key, value in query_params.items()}
    #TODO: Return a dictionary containing the parsed query parameters

def parse_detail(house_detail: Dict):
    """
    Parse the details of a house.

    Args:
        house_detail (Dict): A dictionary containing the details of a house.

    Returns:
        Dict: A dictionary containing the parsed details of the house.
    """
    
    # TODO: customize the return value
    return {
        "url": house_detail["shareInfo"]["url"],
    }