import random

# Utility Functions / Code Cleanliness

def eight_ball() -> str:
    responses = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now', 'Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
    return random.choice(responses)

def roll_dice(message) -> str:
    # Dice format should be in the format of "<number> 🎲 <number>"
    # e.g. "2 🎲 3"
    try:
        num_1, num_2 = message.split("🎲")
        return int(num_1) * random.randrange(1, int(num_2) + 1)
    except:
        return message.content
