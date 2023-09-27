def print_data(user_data):
    for key, value in user_data.items():
        print(key.capitalize() + ": " + value)

def request(user_data):
    user_data["name"] = input("Digite o seu nome: ")
    user_data["age"] = input("Digite a seu idade: ")
    user_data["sex"] = input("Digite o seu sexo: ")
    user_data["city"] = input("Digite a sua cidade: ")
    user_data["state"] = input("Digite o seu estado: ")

def main():
    user_data = {}
    request(user_data)
    print_data(user_data)
    
main()