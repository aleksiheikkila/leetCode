""" 
2353. Design a Food Rating System
MEDIUM
https://leetcode.com/problems/design-a-food-rating-system/

Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. 
The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.

void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the 
given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order,
 that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes 
 before y[i] in alphabetic order.

"""

from sortedcontainers import SortedSet
from collections import defaultdict
from typing import List

"""
Data structures
cuisines {food -> cuisine}
ratings {food -> rating}
by_cuisine {cuisine -> SortedSet with (-rating, food) tuples}

Better to use-rating and return the smallest value, because in case of tied rating, need to return lexicogr. first food

"""

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = {}
        self.ratings = {}
        self.foodinfo_by_cuisine = defaultdict(SortedSet)
        # sortedset values are (-rating, food) tuples
        
        for fo, cu, ra in zip(foods, cuisines, ratings):
            self.cuisines[fo] = cu
            self.ratings[fo] = ra
            self.foodinfo_by_cuisine[cu].add((-ra, fo))

    def changeRating(self, food: str, newRating: int) -> None:
        prevRating, self.ratings[food] = self.ratings[food], newRating
        
        by_cuisine = self.foodinfo_by_cuisine[self.cuisines[food]]
        by_cuisine.discard((-prevRating, food))
        by_cuisine.add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        by_cuisine = self.foodinfo_by_cuisine[cuisine]
        return by_cuisine[0][1] if len(by_cuisine) > 0 else None
        

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)