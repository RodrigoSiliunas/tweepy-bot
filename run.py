from app import *
from app.configuration import ConfigDevelopment

# Descomente as seções e execute o arquivo run.py para que o bot faça o seu trabalho.

if __name__ == "__main__":
    bot = TwitterBot(consumer_key=ConfigDevelopment.API_KEY,
                     consumer_secret=ConfigDevelopment.API_SECRET_KEY,
                     access_token=ConfigDevelopment.ACESS_TOKEN,
                     access_token_secret=ConfigDevelopment.ACESS_TOKEN_SECRET,
                     bearer_token=ConfigDevelopment.BEARER_TOKEN,
                     user_id=ConfigDevelopment.USER_ID)

    # bot.set_dollar_value(3.20)


    # tweet = bot.compare_dollar_with_last_value()
    # tweet = tweet + \
    #     f'\n\nA espécie de pokémon de hoje se chama: {bot.get_pokemon_name()}.'
    # bot.get_pokemon_image()
    # bot.post_new_tweet_with_image(tweet)

    # list_of_tweets = bot.get_citing_tweets_from_user(
    #     1113094855281008641, 100, ['LULA', 'CORRUPTO', 'CORRUPÇÃO', 'INTERESSE', 'INTERESSES'])

    # for tweet in list_of_tweets:
    #     print(f'\n{tweet}')
