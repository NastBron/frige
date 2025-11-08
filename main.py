from datetime import date
from decimal import Decimal


goods = dict()

def add(items, title, amount, expiration_date=None):
    d_amount = Decimal(amount)

    if expiration_date != None:
        date_exp = date(*[int(x) for x in expiration_date.split('-')])
    else:
        date_exp = None

    if title not in items:
        items[title] = [dict(amount = d_amount, expiration_date = date_exp)]
    else:
        items[title].append(dict(amount = d_amount, expiration_date = date_exp ))

    return items

def add_by_note(items, note):

    def is_valid_date_string(s):
        try:
            numbers = s.split('-')
            if len(numbers) != 3:
                return False
            y, m, d = int(numbers[0]), int(numbers[1]), int(numbers[2]) 
            date(y, m, d)  
            return True
        except (ValueError, TypeError):
            return False


    parts = note.strip().split()

    if len(parts) < 2:
        print("Ошибка: недостаточно данных в заметке")
        return items

    if len(parts) >= 3 and is_valid_date_string(parts[-1]):
        expiration_date = parts[-1]
        amount_str = parts[-2]
        title = ' '.join(parts[:-2])

    else:
        expiration_date = None
        amount_str = parts[-1]
        title = ' '.join(parts[:-1])

    if not title or not amount_str:
        print("Ошибка: не удалось определить название или количество")
        return items

    try:
        amount_clean = amount_str.replace(',', '.').strip()
        add(items, title, amount_clean, expiration_date)
    except Exception as e:
        print(f"Ошибка при разборе заметки: {e}")
        return items


def find(items, needle):
    needle = needle.lower()
    return [name for name in items.keys() if needle in name.lower()]


def amount(items, needle):
    matching_names = find(items, needle)
    total = Decimal('0')

    for name in matching_names:
        for record in items[name]:
            total += record['amount']
            
    return total

add_by_note(goods, 'Пельмени Залупинские Блядские 0,10 13-08-2007')
print(is_valid_date_string('13-12-2007'))
print(goods)