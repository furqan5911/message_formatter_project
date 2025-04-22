 
# main.py

from message_formatter_project.message_formatter import star_border, emoji_decorator

@star_border
@emoji_decorator
def greet(message):
    return message

if __name__ == "__main__":
    print(greet("Hello, World!"))
