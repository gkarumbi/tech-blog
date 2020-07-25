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


def process_results(quote_list):
    '''
    Function  that processes the Quote result and transform them to a list of Objects

    Args:
        Quote_list: A dictionary that contains quote details

    Returns :
        Quote_results: A list of QQuote objects
    '''
    quote_results = []
    for quote_item in quote_list:
        author= quote_item.get('author')
        id = quote_item.get('id')
        quote= quote_item.get('quote')
        url = quote_item.get('permalink')

        
        quote_object = Quote(author,id,quote,url)
        quote_results.append(quote_object)

    return quote_results