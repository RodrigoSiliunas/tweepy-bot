from os import environ


class Config:
    USER_ID = 1485469350597472257


class ConfigDevelopment(Config):
    API_KEY = 'vQ7x7zg4nSt5uhoSimaMAgv17'
    API_SECRET_KEY = '8RKXvpoY9IRQWAhzziFEuQsgdGfEd8CPUeZFyc96hpbpiErX8w'
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAALJJbAEAAAAAwZK9OMSpuhRne38XKsZuMrq0TBY%3Dj5iPsuPq6xaaKmX2yFxKnXgOTKgE02jXcJOZgQ9ubMbDrhcQ1C'
    ACESS_TOKEN = '1485469350597472257-1gXrGoffOWoSSBfsD6vkh2pw96ytx2'
    ACESS_TOKEN_SECRET = 'G1PrxWoowfYAVNmxgkrK6Wu8GhgfBBaKQRBhjlQS7aqXO'


class ConfigProduction(Config):
    API_KEY = environ.get('API_KEY')
    API_SECRET_KEY = environ.get('API_SECRET_KEY')
    BEARER_TOKEN = environ.get('BEARER_TOKEN')
    ACESS_TOKEN = environ.get('ACESS_TOKEN')
    ACESS_TOKEN_SECRET = environ.get('ACESS_TOKEN_SECRET')