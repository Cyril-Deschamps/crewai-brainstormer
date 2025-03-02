import requests
import json
import os
from typing import List, Union
from dotenv import load_dotenv

load_dotenv()

def get_true_random(min_value: int, max_value: int, count: int = 1) -> Union[int, List[int]]:
    """
    Get true random numbers from random.org API
    
    Args:
        min_value (int): Minimum value (inclusive)
        max_value (int): Maximum value (inclusive) 
        count (int): Number of random numbers to generate
        
    Returns:
        Union[int, List[int]]: Single random number if count=1, otherwise list of random numbers
    """

    api_key = os.environ.get("RANDOM_ORG_API_KEY")
    if not api_key:
        raise ValueError("RANDOM_ORG_API_KEY environment variable not set")
        
    url = "https://api.random.org/json-rpc/4/invoke"
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": api_key,
            "n": count,
            "min": min_value,
            "max": max_value,
            "replacement": True
        },
        "id": 1
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        
        if "error" in result:
            raise ValueError(f"API Error: {result['error']['message']}")
            
        random_numbers = result["result"]["random"]["data"]
        return random_numbers[0] if count == 1 else random_numbers
        
    except requests.exceptions.RequestException as e:
        # Fallback to Python's random in case of API failure
        import random
        print(f"Warning: Failed to get true random numbers from random.org: {e}")
        print("Falling back to pseudo-random numbers")
        if count == 1:
            return random.randint(min_value, max_value)
        return [random.randint(min_value, max_value) for _ in range(count)] 