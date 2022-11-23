import json

with open('text.txt', 'r') as file:
    data = file.read().splitlines()

print(data)

dictionary_medical_terms = {

}

for words_definitions in data:
    components = words_definitions.split("-")
    word = components[0].split()[0]
    definitions = components[-1]
    print(definitions)
    dictionary_medical_terms.update({word:definitions})


print(dictionary_medical_terms)
print(json.dumps(dictionary_medical_terms))