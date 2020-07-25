import urllib.request,json
from .models import Quote
from flask import jsonify


def get_quotes():
    '''
    Function that fetches the JSON object
    '''
    get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    print(get_quotes_url)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        print(get_quotes_response)
        quote_results = None

        if get_quotes_response:
            print(get_quotes_response)
            quote_results_list = get_quotes_response
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

    quote_item = quote_list

    print(quote_item)
    
    author= quote_item['author']
    id = quote_item['id']
    quote= quote_item['quote']
    url = quote_item['permalink']

        
    quote_object = Quote(author,id,quote,url)
    quote_results.append(quote_object)

    return quote_results