def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    stack = []
    stack.append(numBottles)
    while(numBottles>=numExchange):
        stack.append(numBottles//numExchange)
        numBottles=stack[-1]+numBottles%numExchange
    return sum(stack)

# numWaterBottles(1,9,3)
print(numWaterBottles(1,15,4))