import json


my_dict = {
    "person1":
    {
        "name": 'Dennis',
        "age": 54,
        "gender":
        {
            "Chromosome": "male"
        },
    },
    "person2":
    {
        "name": 'Lori',
        "age": 48,
        "gender":
        {
            "Chromosome": "female"
        },
    },
    "person3":
    {
        "name": 'Matthew',
        "age": 20,
        "gender":
        {
            "Chromosome": "male"
        },
    },
    "person4":
    {
        "name": 'Daniel',
        "age": 18,
        "gender":
        {
            "Chromosome": "male"
        },
    }
}
#print(my_dict)
#print(my_dict.values())

# for i in my_dict.keys():
#     #print(i)
#     for j in my_dict[i]["gender"].items():
#         #print(j)
#         for n in j:
#             print(n)

# for j, B in my_dict.items():
#     print(B["name"])

for k1, v1 in my_dict.items():   # the basic way
    temp = ""
    temp += k1
    for k2, v2 in v1.values():
        temp = str(v2)
    print(temp)
