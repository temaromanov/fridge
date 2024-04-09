from decimal import Decimal
import datetime as dt


DATE_FORMAT = '%Y-%m-%d'

goods = {}


def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = dt.datetime.strptime(
        expiration_date, 
        DATE_FORMAT,
        ).date() if expiration_date else expiration_date
    items[title].append({'amount': amount, 'expiration_date': expiration_date})
    return items


def add_by_note(items, note):
    list_split = note.split()  # разбиваем строку note на список
    if len(list_split[-1].split('-')) == 3:
        experation_date = list_split[-1] 
        title = ' '.join(list_split[:-2])
        amount = list_split[-2]
    else:
        amount = list_split[-1]
        title = ' '.join(list_split[:-1])
        experation_date = None
    add(items, title, Decimal(amount), experation_date)
    return items


def find(items, needle):
    result = []
    needle = needle.lower()
    for key in items:
        if needle in key.lower():
            result.append(key)
        elif needle == key.lower():
            result.append(key)  
        else:
            continue   
    return result


def amount(items, needle):
    amount_count = Decimal(0)
    keys = find(items, needle)
    for title in keys:
        for part in items[title]:
            amount_count += part['amount']
    return amount_count


add(goods, 'Вода', Decimal('2.5'), '2023-12-12')
add(goods, 'Вода', Decimal('3.5'), '2023-12-12')
print(amount(goods, 'Вода'))





    
