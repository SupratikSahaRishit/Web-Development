class ReverseString:
    
    def reverse_words(self, text):
        words = text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

obj = ReverseString()
text = "Codingal is best for learning coding . "

print("Original String:", text)
print("Reversed String:", obj.reverse_words(text))