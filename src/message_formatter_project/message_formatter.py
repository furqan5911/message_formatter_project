 
# src/message_formatter_project/message_formatter.py

def star_border(func):
    """
    Decorator that adds a border of stars around the message.
    """
    def wrapper(message):
        border = '*' * (len(message) + 4)
        return f"{border}\n* {message} *\n{border}"
    return wrapper

def emoji_decorator(func):
    """
    Decorator that adds emojis before and after the message.
    """
    def wrapper(message):
        return f"🎉 {func(message)} 🎉"
    return wrapper
