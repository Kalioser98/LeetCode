class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        limite = right + 1
        es_primo = [True] * limite
        es_primo[0] = es_primo[1] = False
        for i in range(2, int(math.sqrt(limite)) + 1):
            if es_primo[i]:
                for j in range(i * i, limite, i):
                    es_primo[j] = False

        primos = []
        for i in range(left, right + 1):
            if es_primo[i]:
                primos.append(i)

        if len(primos)<2:
            return [-1,-1]

        respuesta = [-1, -1]
        min_dif = float('inf')
        for i in range(1, len(primos)):
            dif = primos[i] - primos[i-1]
            if dif < min_dif:
                min_dif = dif
                respuesta = [primos[i-1], primos[i]]
        return respuesta
