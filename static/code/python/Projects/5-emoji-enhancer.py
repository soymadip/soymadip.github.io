"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

from helpers import ask

emoji_map: dict = {
    "happy": "😊",
    "love": "💗",
    "code": "💻",
    "tea": "🍵",
    "smile": "⌣",
    "food": "🍔",
}

punctuations = ".,!;"

# raw_text = ask("Enter Your message")
raw_text = "i am soumadip Das, i am a Happy coder, coding a shit and taking a smile.\nI love to smile and be happy"

enhanced_text = ""

for word in raw_text.split(" "):
    cleaned_word = word.strip(punctuations).lower()

    if cleaned_word in emoji_map:
        new_word = f"{word} {emoji_map[cleaned_word]}"
        enhanced_text += new_word
    else:
        enhanced_text += word


# NEED TO LEARN REGEX (RE MODULE), will do later
