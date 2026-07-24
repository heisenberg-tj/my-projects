# client
client = {
    "name": "Muhammad",
    "age": 16,
    "balance": 3000
}

print(f"Имя: {client['name']}")
print(f"Возраст: {client['age']}")
print(f'Баланс: {client['balance']}')
client["age"] = client["age"] + 1
client["balance"] = client["balance"] + 500
print(f"Обновлённый баланс {client['name']}: {client['balance']} сомони. Возраст: {client['age']}")