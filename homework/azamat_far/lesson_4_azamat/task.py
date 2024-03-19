my_dict = {
    "tuple": ("apple", "orange", "melon", 23, 35),
    "list": [12, 23, True, "fruit", "water"],
    "dict": {
        "name": "Migel",
        "password": 123,
        "user_id": 1,
        "device": "Iphone 15",
        "os_version": 17.4,
    },
    "set": {"banana", "lime", "watermelon", "poison_fruit", "kiwi"},
}

# Переменные для решения задачи
res_1 = my_dict["tuple"]
res_2 = my_dict["list"]
res_3 = res_2.append("Added")
del res_2[1]
res_4 = my_dict["dict"]
res_4["i am a tuple"] = "new_result"
del res_4["password"]
res_5 = res_2 = my_dict["set"]
res_5.add("new_object")
res_5.remove("poison_fruit")

print("Выведите на экран последний элемент из ключа 'tuple':", res_1[4])
print(my_dict)
