import random

def get_response(message: str) -> str:
  p_message = message.lower()

  if p_message == "hello":
    return "Hello there!"

  if p_message == "hello there":
    return "General Kenobi, hahaha *coughs* ugh.. ah haha... you are a bold one!"
    
  if p_message == "who's a good boy":
    return "Dogo!"

  if message == "roll":
    return str(random.randint(0, 100))

  if p_message == "!help":
    return "`Asking for help? You're weakness disguists me.`"

  return "I don't get the message. Try typing '!help'."
