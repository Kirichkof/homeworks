def extract(data: list) -> dict:
    town, country, pop2018, pop, square = data
    result = {'country': country, 'town': town, 'population': max(pop2018, pop), 'square': square}
    return result

print(extract(["Мумбаи", "Индия", 19980000, 23645000, 881,]))
print('*'*50)
print(extract(["Циндао", "Китай", 5381000,]))