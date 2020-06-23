users = {}
movie = []
users['Kim'] = {'email': 'kim@oreilly.com', 'gender': 'f', 'age': 27, 'friends': ['Josh', 'John']}
users['Josh'] = {'email': 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim']}
users['John'] = {'email': 'john@abc', 'gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}

def user_average(user):
    friends = users[user]['friends']
    ages = []

    for friend in friends:
        ages.append(users[friend]['age'])
    average = sum(ages) / (len(ages))

    print('A média de idade dos amigos de', user, 'é', average)

def usuario_mais_antissocial(users):
    max = 10000
    for name in users:
        user = users[name]
        friends = user['friends']
        if len(friends) < max:
            most_antissocial = name
            max = len(friends)

    print(most_antissocial, 'é o usuário mais antissocial')

user_average('Kim')
user_average('Josh')
user_average('John')

usuario_mais_antissocial(users)