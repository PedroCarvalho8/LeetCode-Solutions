class Solution(object):
    def climbStairs(self, n):
        def fatorial(numero):
            resultado = 1
            for i in range(1, numero + 1):
                resultado *= i
            return resultado

        global ways
        ways = 0

        def Combinacoes(Lista):
            global ways
            ways += int(fatorial(len(Lista))/(fatorial(Lista.count(1))*fatorial(Lista.count(2))))

        Lista = [1] * n
        times = int(n/2) + 1

        for i in range(times):
            print(Lista)
            Combinacoes(Lista)
            if len(Lista) >= 2:
                for j in range(2):
                    Lista.pop(0)
                Lista.append(2)

        return ways
