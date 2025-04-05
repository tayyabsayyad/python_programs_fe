def generate_greeting(name, occasion=None, relationship=None):

    greeting = f"Hello, {name}!"

    if relationship:
        greeting += f" My dear {relationship},"

    if occasion:
        greeting += f" wishing you a very Happy {occasion}!"

    greeting += " Have a wonderful day!"
    return greeting


print("Personalized Greeting Generator")

name = input("Enter the recipient's name: ")
occasion = input("Enter the occasion (optional): ")
relationship = input("Enter the relationship (optional): ")

greeting_message = generate_greeting(name, occasion if occasion else None, relationship if relationship else None)
print("\nGenerated Greeting:")
print(greeting_message)

