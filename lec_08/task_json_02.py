import json

json_text = """
[
    {
        "userId": 1,
        "id": 9,
        "title": "Shanna@melissa.tv",
        "body": "antonette@howel.com"
    },
    {
        "userId": 1,
        "id": 10,
        "title": "Victor Plains",
        "body": "Suite 879"
    },
    {
        "userId": 2,
        "id": 11,
        "title": "Proactive didactic contingency",
        "body": "synergize scalable supply-chains"
    }
]
"""

print(f'{type(json_text) = }\n{json_text = }')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')

