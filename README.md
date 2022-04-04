# Tweepy Pokédoll Bot

### Sobre o projeto

Tweepy Pokédoll Bot é uma aplicação que consome dados de outras APIs como [Awesome](https://docs.awesomeapi.com.br/api-de-moedas) e [PokéAPI](https://pokeapi.co/) e que retorna de forma divertida e simples de entender atualizações diárias sobre as variações que o dólar sofre em um determinado perfil no Twitter.

### Tecnologias Utilizadas

O projeto utiliza várias tecnologias por de baixo dos panos, eu listarei **apenas** as principais, incluindo bibliotecas.

> 1. Python
> 2. [Twitter API V2](developer.twitter.com/)
> 3. SQLAlchemy
> 4. Tweepy
> 5. Requests

### Rodando o Projeto

O código principal fica na pasta raiz desse repositório, `run.py`. Antes de executar o código você deve se certificar que tem o Python em sua versão minima `3.10.1` instalada em sua máquina.

Se estiver cumprindo os requisitos basta abrir o terminal/powershell na pasta raiz do projeto e ativar a venv com o comando:

    enviroment/Scripts/activate

As bibliotecas seram carregadas e você pode simplesmente executar o comando:

    python run.py

### Configurando o Projeto

É importante para que o projeto rode livre de quaisquer problemas que você tenha se cadastrado previamente no Twitter como um desenvolvedor, e que tenha acesso a API Twitter API V2 em sua versão extendida.

Caso contrário, o código simplesmente não irá cumprir o prometido e não executará sem as informações personalizadas que você deve adulterar em `app/configuration.py`.

Também vale a pena ressaltar que caso você esteja pensando em mandar isso para produção, a configuração a ser utilizada é a `ConfigProduction`. Você deve armazenar as informações de autenticação cedidas pelo Twitter no servidor, por precaução e por boas práticas.

### Observações Importantes! ⚠️

Esse projeto não tem uma documentação para seus métodos, e também não há uma pretenção de criar uma página com Swagger para isso até o presente momento. O código foi escrito pensando na legibilidade. Caso você tenha alguma dúvida pertinente sobre o projeto ou seus autores não deixe de nos procurar nas redes sociais.

Co-criador Discord: Rodrigo X#7737

### Considerações Finais

Antes de executar o arquivo `run.py` verifique os exemplos já escritos nesse mesmo arquivo. Se necessário descomente ou comente parte do código e adultere livremente até chegar ao resultado desejado. Esse foi um projeto muito divertido de ser criado do início ao fim do desenvolvimento. Obrigado por dispor seu tempo para ler até aqui. ❤


##### Participantes do projeto

    Luiza Vitória Araujo,
    Rodrigo Siliunas,
    Silvio Carvalho,
    Beatriz Santos,
    Thiago Falcão,
    Thais Goneli,
    Andre Dimas