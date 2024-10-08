from json import load
with open('datasets/counties.json', 'r') as file:
    data = load(file)
print(data)