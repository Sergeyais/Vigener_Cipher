class Vco:
    """This class a Vigenere cipher by the opened text"""

    def __init__(self):
        self.chars = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, text, key):
        gamma = ""
        answer = ""
        gamma += key
        for i_gamma in range(len(text) - 1):
            gamma += text[i_gamma]
        for i_text in range(len(text)):
            answer += self.chars[
                (self.chars.find(text[i_text]) + self.chars.find(gamma[i_text])) % 26
            ]
        return print(answer)

    def decipher(self, text, key):
        gamma = ""
        answer = ""
        gamma += key
        for i_gamma in range(len(text) - 1):
            gamma += self.chars[
                (self.chars.find(text[i_gamma]) - self.chars.find(gamma[i_gamma])) % 26
            ]
        for i_text in range(len(text)):
            answer += self.chars[
                (self.chars.find(text[i_text]) - self.chars.find(gamma[i_text])) % 26
            ]
        return print(answer)
