class Cryptographer:

    def encrypt_or_decrypt(self, fileNameIn, fileNameOut, algorithm, encrypt=True):
        fileIn = open(str(fileNameIn) + ".txt", "r")
        fileOut = open(str(fileNameOut) + ".txt", "w+")

        for line in fileIn:
            if encrypt:
                word = algorithm.crypt(line.strip())
            else:
                word = algorithm.decrypt(line.strip())

            fileOut.write(word+"\n")

        fileIn.close()
        fileOut.close()
