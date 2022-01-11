class Polybius:
    alphabet = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'k'], ['l', 'm', 'n', 'o', 'p'],
                ['q', 'r', 's', 't', 'u'], ['v', 'w', 'x', 'y', 'z'], ['j']]

    def outerloop(self, c, j, s):
        word = ""
        for k in range(len(self.alphabet)):
            l = 0
            while l < len(self.alphabet[k]):
                if self.alphabet[k][l] == c:
                    if j + 1 == s:
                        word += str(k + 1) + str(l + 1)
                    else:
                        word += str(k + 1) + str(l + 1) + " "
                    break
                l += 1
        return word

    def crypt(self, line):
        for i in range(len(line)):
            word = ""
            for j in range(len(line[i])):
                c = line[i][j]
                if c.isupper():
                    c = c.lower()
                word += self.outerloop(c, j, len(line[i]))
            line[i] = word
        return line

    def decrypt(self, line):
        for i in range(len(line)):
            word = ""
            c1 = line[i][0]
            c2 = line[i][1]
            i1 = int(c1)
            i2 = int(c2)
            word += self.alphabet[i1 - 1][i2 - 1]
            line[i] = word
        return line
