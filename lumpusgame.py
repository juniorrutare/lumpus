from story import stories  # Import stories
from mechanics import choose_story, play_story  # Import functions from mechanics.py

def main():
    """Main function to run the program."""
    print("Welcome to Choose Your Adventure!")
    story_title = choose_story(stories)  # Use imported stories
    play_story(stories[story_title])  # Play the selected story

if __name__ == "__main__":
    main()