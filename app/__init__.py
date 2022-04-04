import tweepy
import os
import requests
from .database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.Tweet import Tweet


# Garantindo a conexão com o banco de dados SQLITE.
engine = create_engine(
    'sqlite:///C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\tweepy-dollar-bot\\tweeter.db', echo=True)
Session = sessionmaker(engine)
session = Session()

# Criação de todos os modelos de dados no sqlite.
Base.metadata.create_all(engine)


class TwitterBot(tweepy.Client):
    def __init__(
        self, consumer_key: str, consumer_secret: str, access_token: str,
        access_token_secret: str, bearer_token: str, user_id: int
    ) -> None:

        self.__consumer_key = consumer_key
        self.__consumer_secret = consumer_secret
        self.__access_token = access_token
        self.__access_token_secret = access_token_secret
        self.__bearer_token = bearer_token
        self.__api_v1 = None
        self.user_id = user_id

        super(tweepy.Client, self).__init__(
            consumer_key=self.__consumer_key, consumer_secret=self.__consumer_secret,
            access_token=self.__access_token, access_token_secret=self.__access_token_secret,
            bearer_token=self.__bearer_token
        )

    def __repr__(self) -> str:
        return f'TwitterBot rodando no perfil com identificador: {self.user_id}'

    def __connect_api_v1(self):
        auth = tweepy.OAuthHandler(consumer_key=self.__consumer_key,
                                   consumer_secret=self.__consumer_secret)
        auth.set_access_token(self.__access_token,
                              self.__access_token_secret)
        self.__api_v1 = tweepy.API(auth)

        return self.__api_v1

    @staticmethod
    def compare_dollar_with_last_value() -> str:
        response = requests.get(
            'https://economia.awesomeapi.com.br/json/last/USD-BRL')
        querry = session.query(Tweet).first()
        last_value = querry.dollar

        if float(response.json()['USD']['ask']) > querry.dollar:
            session.query(Tweet).filter(Tweet.id == querry.id).update(
                {'dollar': float(response.json()['USD']['ask'])})
            session.commit()

            return f'😭 O dólar disparou. Ele saiu de R${last_value} e chegou em R${response.json()["USD"]["ask"][0:4]}. Foi uma variação de {response.json()["USD"]["pctChange"]} %.'
        elif float(response.json()['USD']['ask']) < querry.dollar:
            session.query(Tweet).filter(Tweet.id == querry.id).update(
                {'dollar': float(response.json()['USD']['ask'][0:4])})
            session.commit()

            return f'😂 O dólar abaixou! Hora de comprar aqueles importados. Ele caiu de R${last_value} para R${response.json()["USD"]["ask"][0:4]}. Foi uma variação de {response.json()["USD"]["pctChange"]} %.'
        else:
            return f'😐 O dólar se manteve com o valor de R${last_value:.2f}. Não é hoje que iremos comprar aquela RaspberryPi.'

    @staticmethod
    def set_dollar_value(dollar_vallue: float) -> None:
        querry = session.query(Tweet).first()
        session.query(Tweet).filter(Tweet.id == querry.id).update(
            {'dollar': dollar_vallue})
        session.commit()

    @staticmethod
    def get_pokemon_name() -> str:
        querry = session.query(Tweet).first()
        pokemon_number = str(querry.dollar).replace(".", "")

        try:
            request = requests.get(
                f'https://pokeapi.co/api/v2/pokemon/{pokemon_number[0::2]}')

            return request.json()['name'].capitalize()
        except Exception as e:
            return f'🚧 O pokémon não foi encontrado.\n⚒ Erro: {e}'

    @staticmethod
    def get_pokemon_image() -> None:
        querry = session.query(Tweet).first()
        pokemon_number = str(querry.dollar).replace(".", "")

        try:
            request = requests.get(
                f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_number[0::2]}.png', stream=True)
            filename = 'static/pokemon.jpg'

            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
        except Exception as e:
            print(
                f'🚧 A imagem do pokémon não pode ser encontrada.\n⚒ Erro: {e}')

    def post_new_tweet_with_image(self, tweet: str) -> bool:
        try:
            self.__connect_api_v1()
            path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..\static")) + "\pokemon.jpg"

            self.__api_v1.update_status_with_media(
                status=tweet, filename=path)

            print(f'✔️ Uma nova postagem acaba de ser feita no Twitter.')
            return True
        except Exception as e:
            print(
                f'🚧 Não foi possivel criar a postagem no Twitter com a imagem.\n⚒ Erro: {e}')
            return False

    def get_citing_tweets_from_user(self, profile_id: int,
                                    max_results: int, key_words: list[str]) -> list:
        list_of_tweets = self.get_users_tweets(
            id=profile_id, max_results=max_results)

        citing_tweets = []

        for tweet in list_of_tweets[0]:
            tweet = tweet.text.upper().split()

            for word in tweet:
                for key in key_words:
                    if key.upper() == word.upper():
                        tweet_to_append = ' '.join(tweet).capitalize()
                        citing_tweets.append(tweet_to_append)
                        break

        print(
            f'✨ Analisamos os últimos {max_results} tweets deste perfil. O seu alvo citou as palavras chaves em um total de {len(citing_tweets)} tweets diferentes.')

        return citing_tweets
