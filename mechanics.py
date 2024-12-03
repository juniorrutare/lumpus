def choose_story(stories):
    """Prompt the user to choose a story."""
    print("Available stories:")
    for i, title in enumerate(stories.keys(), 1):
        print(f"{i}. {title}")
    while True:
        try:
            choice = int(input("Choose a story by entering the number: ")) - 1
            if 0 <= choice < len(stories):
                return list(stories.keys())[choice]
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def play_story(story):
    """Play the chosen story."""
    current_node = story["start"]
    while True:
        node = story["nodes"][current_node]
        print("\n" + node["text"])
        
        if "ending" in node:
            print("The End!")
            break
        
        print("\nOptions:")
        for option, next_node in node["choices"].items():
            print(f"- {option.capitalize()}")
        
        choice = input("What do you do? ").lower()
        if choice in node["choices"]:
            current_node = node["choices"][choice]
        else:
            print("Invalid choice. Please try again.")
            