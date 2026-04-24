
import os

# OLLAMA_API_KEY = "06990046f4be48babb1788f593ffae03.ct7o6KnCVTOiXT25_sxzlgZ0"
# os.environ["OLLAMA_API_KEY"] = OLLAMA_API_KEY

import ollama
import subprocess
import json



def osearch(term: str) -> str:
    """Returns results of an Ollama web search.

    Args:
        term: Search term/query

    Returns:
        results: JSON struct - top 5 search results
    """

    results = ollama.web_search(term)

    # print(results)
    # print("\x1b[38;5;10m" + results.json() + "\x1b[0m")
    # print("\x1b[38;5;63m" + json.dumps(json.loads(results.model_dump_json())["results"], indent=4)+ "\x1b[0m")

    return json.dumps(json.loads(results.model_dump_json())["results"], indent=0)

def ofetch(url: str) -> str:
    """Returns result of an Ollama web fetch.

    Args:
        url: Website URL
    
    Returns:
        json: struct containing {title, content, links}
    """

    result = ollama.web_fetch(url)

    # print(result)
    # print(json.dumps(json.loads(result.model_dump_json()), indent=4))

    return json.dumps(json.loads(result.model_dump_json()), indent=0)


    

__all__ = ["osearch","ofetch"]


if __name__ == "__main__":
    osearch("AAPL news")
    ofetch("bbc.com/news")
