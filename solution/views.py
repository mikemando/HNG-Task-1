import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NumberClassificationView(APIView):
    def get(self, request):
        try:
            number =  int(request.query_params.get('number'))
            numbersAPI = f'http://numbersapi.com/{number}/math'

            funFact = requests.get(numbersAPI).text
        except:
            return Response(
                {'number': 'alphabet', 'error': True}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        digitSum = 0
        tempNum = str(number)
        for i in range(len(tempNum)):
            digitSum += int(tempNum[i])

        def isPrime(number):
            num = int(number)
            if num <= 1:
                return False
            for i in range(2, num):
                if (num % i) == 0:
                    return False         
            return True
    
        def isPerfectNumber(number):
            if number < 6:
                return False
            divisorSum = 0
            for i in range(1, number):
                if (number % i) == 0:
                    divisorSum += i
            
            return True if (divisorSum == number) else False
        
        def propertiesField(number):
            result = []

            num = str(number)
            numLen = len(num)
            armstrongNum = 0
            for i in range(numLen):
                armstrongNum += (int(num[i]) ** numLen)
            
            if armstrongNum == number:
                result.append('armstrong')

            if (number % 2) == 0:
                result.append('even')
            
            if (number % 2) != 0:
                result.append('odd')
        
            return result

        return Response(
            {
                "number": number,
                "is_prime": isPrime(number),
                "is_perfect": isPerfectNumber(number),
                "properties": propertiesField(number),
                "digit_sum": digitSum,
                "fun_fact": funFact,
            },
            status= status.HTTP_200_OK
        )
