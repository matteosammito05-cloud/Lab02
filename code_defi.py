def main():
    listino = {}
    with open('listino.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            city_id = parts[0]
            price = int(parts[-1])
            city_name = " ".join(parts[1:-1])
            listino[city_id] = (city_name, price)

    perc = {}
    tot_dist = {'a': 0}
    with open('distanze.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            cit, dist = line.split(':')
            p, a = cit.split('-')
            dist = int(dist)
            perc[a] = (p, dist) 
            tot_dist[a] = tot_dist[p] + dist

    print("Città direttamente connesse a Los Angeles:")
    for a, (p, dist) in perc.items():
        if p == 'a':
            print(listino[a][0])
            
    best_offer_city_id = max(listino.keys(), key=lambda k: listino[k][1])
    best_offer_name = listino[best_offer_city_id][0]
    best_offer_dist = tot_dist[best_offer_city_id]
    print(f"Per raggiungere l'offerta migliore, {best_offer_name}, servono: {best_offer_dist} km")
    
    worst_ratio_city_id = None
    worst_ratio = float('inf')
    for k in listino.keys():
        if k !='a':
            ratio = listino[k][1] / tot_dist[k]
            if ratio < worst_ratio:
                worst_ratio = ratio
                worst_ratio_city_id = k
            
    worst_ratio_name = listino[worst_ratio_city_id][0]
    print(f"La citta' con il peggior rapporto è {worst_ratio_name}")
    
    best_offer_within_4000_id = None
    max_offer = -1
    for k in listino.keys():
        if tot_dist[k] <= 4000:
            if listino[k][1] > max_offer:
                max_offer = listino[k][1]
                best_offer_within_4000_id = k
    if best_offer_within_4000_id is not None:
        best_4000_name = listino[best_offer_within_4000_id][0]
        print(f"La migliore offerta entro 4000 km è a {best_4000_name}")

main()