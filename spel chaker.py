from spelchaker import spelchaker  # Make sure this module is installed and correctly named

class Spelchker:
    def __init__(self):
        self.spel = spelchaker()  # Initialize the spell checker

    def check_spelling(self, text):
        # Assuming spelchaker has a method to check spelling
        corrections = self.spel.check(text)
        return corrections

    def suggest_corrections(self, word):
        # Assuming spelchaker has a method to suggest corrections for a single word
        suggestions = self.spel.suggest(word)
        return suggestions

# Example usage
if __name__ == "__main__":
    checker = Spelchker()
    text_to_check = input("Enter a text to check spelling: ")
    corrections = checker.check_spelling(text_to_check)

    if corrections:
        print("Corrections:", corrections)
    else:
        print("No spelling errors found.")
