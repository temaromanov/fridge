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
    product_amount = Decimal('0')
    keys = find(items, needle)
    for title in keys:
        for part in items[title]:
            product_amount += part['amount']
    return product_amount


def expire(items, in_advance_days=0):
    result = []
    today = dt.date.today()
    for title, parts in items.items():
        amount = Decimal('0')
        for part in parts:
            expiration_date = part.get('expiration_date')
            if expiration_date:
                days_until = (expiration_date - today).days
                if days_until <= in_advance_days:
                    amount += part['amount']
                    print(amount)
        if amount > Decimal('0'):
            result.append((title, amount))
    return result


add(goods, 'Яйца', Decimal('10'))
add(goods, 'Хлеб', Decimal('5'), '2024-04-09')
add(goods, 'Хлеб', Decimal('6'), '2024-04-10')
add(goods, 'Молоко', Decimal('5'), '2024-04-11')
print(expire(goods))





    
