import random
from datetime import datetime, timedelta

def generate_story_with_ai(date):
    locations = [
        "a mystical forest", "a bustling medieval town", "a far-future city with flying cars", 
        "an ancient library buried under the desert", "a mysterious island", "a haunted castle"
    ]
    
    characters = [
        "a wise old sage", "a young adventurer", "a pirate captain", "a lost time traveler", 
        "a curious scholar", "a band of rebels fighting for freedom"
    ]
    
    conflicts = [
        "searching for a legendary artifact", "trying to solve an ancient riddle", 
        "escaping from a powerful enemy", "discovering a hidden truth that could change the world", 
        "facing a mysterious force that threatens the land", "seeking redemption for a past mistake"
    ]
    
    twists = [
        "only to discover that the artifact was a trap", "and in the end, you realize you've been the enemy all along", 
        "and as you succeed, the world starts to unravel in unexpected ways", "only to learn that time itself is the greatest enemy",
        "and you find a version of yourself, older and wiser, warning you about the consequences of your actions",
        "and the world around you begins to fade, leaving you with just memories of a past that never existed"
    ]
    
    location = random.choice(locations)
    character = random.choice(characters)
    conflict = random.choice(conflicts)
    twist = random.choice(twists)
    
    story = (
        f"On {date}, you traveled back in time and found yourself in {location}. "
        f"There, you met {character}, who was {conflict}. "
        f"As you journeyed together, you faced unexpected challenges {twist}."
    )
    
    return story

now = datetime.now()
delta = int(input("How many days do you want to travel back from now? "))
new_time = now - timedelta(days=delta)
print(f"\n{'-'*20}")
print(f"Time travel completed. Today is {new_time.strftime('%Y-%m-%d %H:%M:%S')}.")

print(f"\nStory for your journey:")
print(generate_story_with_ai(new_time.date()))