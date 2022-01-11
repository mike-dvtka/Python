class Cryptographer:

    def encrypt_or_decrypt(self, fileNameIn, fileNameOut, algorithm, encrypt=True):
        fileIn = open(str(fileNameIn) + ".txt", "r")
        fileOut = open(str(fileNameOut) + ".txt", "w+")

        for line in fileIn:
            strLine = line.split()
            if encrypt:
                word = algorithm.crypt(strLine)
            else:
                word = algorithm.decrypt(strLine)
            word = strLine
            for i in range(len(word)):
                if i+1 == len(word):
                    fileOut.write(word[i])
                else:
                    fileOut.write(word[i]+" ")
            fileOut.write("\n")

        fileIn.close()
        fileOut.close()
