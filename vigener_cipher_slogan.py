class Vcs:
    """This class a Vigenere cipher by the slogan"""

    def __init__(self):
        self.chars = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, text, key):
        gamma = ""
        answer = ""
        for i_gamma in range(len(text)):
            gamma += key[i_gamma % len(key)]
        for i_text in range(len(text)):
            answer += self.chars[
                (self.chars.find(text[i_text]) + self.chars.find(gamma[i_text])) % 26
            ]
        return print(answer)

    def decipher(self, text, key):
        gamma = ""
        answer = ""
        for i_gamma in range(len(text)):
            gamma += key[i_gamma % len(key)]
        for i_text in range(len(text)):
            answer += self.chars[
                (self.chars.find(text[i_text]) - self.chars.find(gamma[i_text])) % 26
            ]
        return print(answer)
