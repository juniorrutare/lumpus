# story.py
stories = {
    "Adventure in the Forest": {
        "start": "start",
        "nodes": {
            "start": {
                "text": "You are standing at the edge of a dark forest. Do you want to enter?",
                "choices": {"yes": "deep_forest", "no": "village"}
            },
            "deep_forest": {
                "text": "You venture deep into the forest and find a mysterious cave.",
                "choices": {"enter cave": "cave", "return": "start"}
            },
            "village": {
                "text": "You return to the village and find your friends waiting for you.",
                "ending": True
            },
            "cave": {
                "text": "Inside the cave, you discover a treasure chest filled with gold.",
                "ending": True
            },
        }
    }
}