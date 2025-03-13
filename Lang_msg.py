import time
import os
import sys

messages = [
    "Hey Lang (Zhaii/Mi amore), just a little reminder... 😊",
    "Take a deep breath and enjoy the moment. ✨",
    "You are appreciated more than you know. 💛",
    "Also, don’t forget to drink some water! 💧",
    "No matter what, I’m always here for you. 🤍",
    "Stay kind to yourself and have a wonderful day!"
]

# Clear screen function (Windows & Linux/macOS)
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Typing effect to animate text
def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Water droplet animation
def hydration_animation():
    droplets = ["💧", "💦", "🌊"]
    for _ in range(3):
        for drop in droplets:
            sys.stdout.write(f"\rHydration Reminder: {drop}   ")
            sys.stdout.flush()
            time.sleep(0.5)
    print("\rHydration Reminder: Stay hydrated! 💙  ")

if __name__ == "__main__":
    clear_screen()

    # Show messages with a typing effect
    for message in messages:
        typing_effect(message, delay=0.05)
        time.sleep(1.5)

    # Animated hydration reminder
    hydration_animation()

    # Simple hydration ASCII reminder
    hydration_reminder = """
      (  )   (   )  )
       ) (   )  (  (
       ( )  (    ) )
      ****************
      *  Stay Hydrated!  *
      ****************
    """

    typing_effect(hydration_reminder, delay=0.002)
    typing_effect("You’re never alone—I’m always here for you. 💙")
    typing_effect("Take care and remember to stay hydrated! 💧")
