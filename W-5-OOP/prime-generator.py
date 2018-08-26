def genPrimes():

    primesList = []
    candidateNumber = 2
    while True:
        isPrime = True
        for n in primesList:
            if (candidateNumber % n) == 0:
                isPrime = False
                break
        if isPrime:
            primesList.append(candidateNumber)
            yield candidateNumber
        candidateNumber += 1