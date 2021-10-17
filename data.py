import requests
DATA_PARAMS = {
    'amount': 10,
    'type' : 'boolean'
}


class Question_data:
    def __init__(self):
        self.question_data = requests.get(url="https://opentdb.com/api.php", params= DATA_PARAMS).json()['results']


    
