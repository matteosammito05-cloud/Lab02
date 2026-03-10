listino = {}
with open('listino.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            city_id = parts[0]
            price = int(parts[-1])
            city_name = " ".join(parts[1:-1])
            listino[city_id] = {'name': city_name, 'price': price}