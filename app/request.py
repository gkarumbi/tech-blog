import urllib.request,json
from .models import Quote


def get_quotes():
    '''
    Function that fetches the JSON object
    '''
    get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response:
            quote_results_list = get_quotes_response[]
            quote_results = process_results(quote_results_list)


    return quote_results


    