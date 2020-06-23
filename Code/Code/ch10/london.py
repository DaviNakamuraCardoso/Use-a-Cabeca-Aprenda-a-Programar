current = {'location': {'UK': {'city': 'London', 'temperature': 67.2, 'precip_prob': '40%'}}}

loc = current['location']['UK']

print('In', loc['city'] + ', ', 'it is', loc['temperature'], 'degrees')


