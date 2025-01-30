class Solution:
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 9/5 + 32
        return [kelvin, fahrenheit]

solution = Solution()

result = solution.convertTemperature(25.0)


print(result)  
