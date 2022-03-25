import random

RESPONSES = ['Outlook is good', 'Ask again later', 'Yes', 'No', 'Most likely no',
'Most likely yes', 'Maybe', 'Outlook is not good']
Magic_Response = random.choice(RESPONSES)

Player_Response = input("What would you like to ask the magic 8 ball? >")
print(f"The Magic 8 ball says {Magic_Response}")