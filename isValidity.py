def runValidity():

    nameFASTA = []

    def readFASTA(fileName):
        with open(fileName, 'r') as file:
            v = []
            genome = ''
            for line in file:
                if line[0] != '>':
                    genome += line.strip()
                else:
                    nameFASTA.append(line.replace('\n', ''))
                    v.append(genome)
                    genome = ''
            v.append(genome)
            del v[0]
            return v


    def fetchX():
        import os
        this_folder = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(this_folder,'sample.txt')
        X = readFASTA(filename)
        return X


    def isValid(x):
        for base in x:
            if not base in {'A','C','G','T'}:
                return 'Invalid'
        return 'Valid'


    X_newbie = []
    Y_newbie = []
    X = fetchX()

    Verdict = []

    for x in X:
        x = x.upper().replace(' ', '')

        if isValid(x) == 'Invalid' or len(x)<16:
            Verdict.append('Invalid FASTA')
        else:
            Verdict.append('Valid FASTA')
            X_newbie.append(x)
            Y_newbie.append(-100)

    return X_newbie, Y_newbie, nameFASTA, Verdict

# def validity():
#     for verdity in Verdict:
#         if verdity == 'Invalid FASTA':
#             return 'Invalid'
#     return 'Valid'
#
#
# def run():
#     if validity() == 'Invalid':
#         return ensure
#     else:
#         return ensure, X_newbie, Y_newbie

# print(runValidity())
