class RotN:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    UP = False

    def __init__(self, number):
        self.n = number

    def crypt(self, line):
        for i in range(len(line)):
            word = ""
            for j in range(len(line[i])):
                c = line[i][j]
                if c.isupper():
                    self.UP = True
                    c = c.lower()
                for k in range(len(self.alphabet)):
                    if self.alphabet[k] == c:
                        c = self.alphabet[(k + self.n) % len(self.alphabet)]
                        if self.UP:
                            c = c.upper()
                            self.UP = False
                        break
                word += c
            line[i] = word
        return line

    def decrypt(self, line):
        for i in range(len(line)):
            word = ""
            for j in range(len(line[i])):
                c = line[i][j]
                if c.isupper():
                    self.UP = True
                    c = c.lower()
                for k in range(len(self.alphabet)):
                    if self.alphabet[k] == c:
                        if (k-self.n) >= 0:
                            c = self.alphabet[k-self.n]
                            if self.UP:
                                c = c.upper()
                                self.UP = False
                            break
                        else:
                            c = self.alphabet[(k-self.n)+len(self.alphabet)]
                            if self.UP:
                                c = c.upper()
                                self.UP = False
                            break
                word += c
            line[i] = word
        return line
