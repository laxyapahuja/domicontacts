import pandas, requests, json, os

final = {}

proxies = {
    'http': 'socks5h://localhost:9150',
    'https': 'socks5h://localhost:9150'
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

df = pandas.read_csv('contacts.csv')
numbers = df['Phone 1 - Value'].to_list()

throw_error = False
index = 0 # Edit this according to the value you want the program to start from
out = []
for number in numbers:
    number = str(numbers[index]).replace(' ', '').replace('+91', '').replace('-', '').replace('(', '').replace(')','').split(':::')[0]
    if number.startswith('0'):
        number = number[1::]
    for i in range(0,3):
        try:
            response = requests.get('http://slf2rrahypck3bwckpdohsnhpeqrb3nhvwznjmarmweofwnptowe4mad.onion/api/search/'+number, proxies=proxies)
            out.append(response.json())
            db_data = response.json()['db_data']
            clear()
            print('{} [{}/{}]'.format(number, index, (len(numbers)-1)))
        except:
            if i == 2:
                throw_error = True
                break
            continue
        break
    if throw_error == True:
        index += 1
        throw_error = False
        continue
    with open("data.json","w") as f:
        json.dump(out,f,indent=4)
    # Email handling
    for email in db_data['linked_emails']:
        if number not in email:
            df.loc[index, 'E-mail 1 - Type'] = 'Home'
            df.loc[index, 'E-mail 1 - Value'] = email
            df.to_csv("contacts.csv", index=False)
            print('Email added for {}.'.format(number))
    # Address handling
    for order in db_data['random_orders']:
        if order['delivery_address']:
            df.loc[index, 'Address 1 - Type'] = 'Home'
            df.loc[index, 'Address 1 - Formatted'] = order['delivery_address']
            df.to_csv("contacts.csv", index=False)
            print('Address added for {}.'.format(number))
            break
        else: 
            continue
    index += 1