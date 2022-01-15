class Polybius:
    alphabet = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'k'], ['l', 'm', 'n', 'o', 'p'],
                ['q', 'r', 's', 't', 'u'], ['v', 'w', 'x', 'y', 'z'], ['j', ' ']]

    def outerloop(self, c):
        word = ""
        for k in range(len(self.alphabet)):
            l = 0
            while l < len(self.alphabet[k]):
                if self.alphabet[k][l] == c:
                    word += str(k + 1) + str(l + 1) + " "
                    break
                l += 1
        return word

    def crypt(self, strLine):
        line = ""
        strLine = strLine.lower()
        for i in range(len(strLine)):
            word = ""
            c = strLine[i]
            word += self.outerloop(c)
            line += word
        return line

    def decrypt(self, strLine):
        line = strLine.split()
        for i in range(len(line)):
            word = ""
            c1 = line[i][0]
            c2 = line[i][1]
            i1 = int(c1)
            i2 = int(c2)
            word += self.alphabet[i1 - 1][i2 - 1]
            line[i] = word
        line = "".join(line)
        return line