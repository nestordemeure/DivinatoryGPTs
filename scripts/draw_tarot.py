import random

def draw_major_arcana(num_cards):
    major_arcana = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", 
        "The Emperor", "The Hierophant", "The Lovers", "The Chariot", 
        "Strength", "The Hermit", "Wheel of Fortune", "Justice", 
        "The Hanged Man", "Death", "Temperance", "The Devil", 
        "The Tower", "The Star", "The Moon", "The Sun", 
        "Judgement", "The World"
    ]

    if num_cards > len(major_arcana):
        print("There are only 22 Major Arcana cards.")
        return []

    return random.sample(major_arcana, num_cards)

# Example usage
#num_to_draw = 3  # change this number to draw a different number of cards
#drawn_cards = draw_major_arcana(num_to_draw)
#print("Drawn Cards:", drawn_cards)

