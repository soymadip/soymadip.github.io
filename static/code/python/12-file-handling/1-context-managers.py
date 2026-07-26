class TagWrapper:
    def __init__(self, tag_name):
        # This saves the argument passed when creating the object
        self.tag = tag_name

    def __enter__(self):
        # 1. Setup Phase: Print the opening tag
        print(f"<{self.tag}>")
        return self  # This lets us use the 'as' keyword if we want to

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 2. Cleanup Phase: Print the closing tag
        print(f"</{self.tag}>")
        # Returning None (or nothing) lets any errors crash normally


# Call

# When this line hits, __enter__ runs immediately
with TagWrapper("bold"):
    # This is the inside block
    print("This text is inside the bold tags!")
    print("Still inside...")

# The moment we indent back out, __exit__ runs automatically!
print("We are completely outside now.")
