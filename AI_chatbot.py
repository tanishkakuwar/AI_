import random

# Animal database
animals = {
    "lion": {
        "type": "Mammal",
        "diet": "Carnivore",
        "habitat": "Savannas and grasslands",
        "sound": "Roar",
        "fact": "Lions are known as the king of the jungle."
    },
    "elephant": {
        "type": "Mammal",
        "diet": "Herbivore",
        "habitat": "Forests and grasslands",
        "sound": "Trumpet",
        "fact": "Elephants are the largest land animals."
    },
    "dog": {
        "type": "Mammal",
        "diet": "Omnivore",
        "habitat": "Domestic",
        "sound": "Bark",
        "fact": "Dogs are known as man's best friend."
    },
    "cat": {
        "type": "Mammal",
        "diet": "Carnivore",
        "habitat": "Domestic",
        "sound": "Meow",
        "fact": "Cats sleep for around 12-16 hours a day."
    },
    "cow": {
        "type": "Mammal",
        "diet": "Herbivore",
        "habitat": "Farms",
        "sound": "Moo",
        "fact": "Cows have four stomach compartments."
    },
    "tiger": {
        "type": "Mammal",
        "diet": "Carnivore",
        "habitat": "Forests",
        "sound": "Roar",
        "fact": "Tigers have striped skin, not just striped fur."
    }
}

fun_facts = [
    "Octopuses have three hearts!",
    "A giraffe’s neck has the same number of bones as a human.",
    "Dolphins are very intelligent and can recognize themselves in mirrors.",
    "Penguins cannot fly but are excellent swimmers."
]

def greet():
    print("  Animal ChatBot: Hi! Ask me anything about animals.")
    print("Type an animal name or ask something like:")
    print("- What does a lion eat?")
    print("- Where does an elephant live?")
    print("- Tell me a fun fact")
    print("Type 'exit' to quit.\n")

def get_animal_from_input(user_input):
    for animal in animals:
        if animal in user_input:
            return animal
    return None

def get_response(user_input):
    text = user_input.lower()

    # Exit
    if text in ["exit", "bye", "quit"]:
        return "exit"

    # Greetings
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello!  Ask me about any animal!"

    # Fun fact
    if "fun fact" in text:
        return random.choice(fun_facts)

    animal = get_animal_from_input(text)

    if animal:
        info = animals[animal]

        if "eat" in text or "diet" in text:
            return f"A {animal} is a {info['diet']}."

        elif "live" in text or "habitat" in text:
            return f"A {animal} lives in {info['habitat']}."

        elif "sound" in text or "noise" in text:
            return f"A {animal} makes a '{info['sound']}' sound."

        elif "type" in text:
            return f"A {animal} is a {info['type']}."

        elif "fact" in text:
            return info["fact"]

        else:
            return (f"Here’s some info about {animal}:\n"
                    f"- Type: {info['type']}\n"
                    f"- Diet: {info['diet']}\n"
                    f"- Habitat: {info['habitat']}\n"
                    f"- Sound: {info['sound']}\n"
                    f"- Fun Fact: {info['fact']}")

    # Help
    if "help" in text:
        return ("You can ask:\n"
                "- Diet of animals\n"
                "- Habitat\n"
                "- Sounds\n"
                "- Fun facts\n"
                "Example: 'What does a tiger eat?'")

    return "I don't know that animal yet  . Try another one!"

def chatbot():
    greet()
    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        if response == "exit":
            print("  Animal ChatBot: Goodbye!  ")
            break

        print("  Animal ChatBot:", response)


# Run chatbot
if __name__ == "__main__":
    chatbot()
