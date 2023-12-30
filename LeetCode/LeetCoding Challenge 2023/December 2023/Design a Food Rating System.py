
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.foodByCuisine = collections.defaultdict(lambda: SortedList())
        self.foodMap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodByCuisine[cuisine].add((-rating, food))
            self.foodMap[food] = [rating, cuisine]
        

    def changeRating(self, food: str, newRating: int) -> None:

        oldRating, cuisine = self.foodMap[food]

        self.foodByCuisine[cuisine].remove((-oldRating, food))
        self.foodByCuisine[cuisine].add((-newRating, food))

        self.foodMap[food] = [newRating, cuisine]
        

    def highestRated(self, cuisine: str) -> str:
        
        return self.foodByCuisine[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
