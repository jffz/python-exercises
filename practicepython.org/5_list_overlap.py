import random

__author__ = "Geoffrey Bachelot"

list1 = list(range(1, random.randint(1, 30)))
list2 = list(
    range(1, random.randint(random.randint(1, 5), random.randint(5, 30)))
)


def retrieveIntersections(*lists):
    intersections = set()
    for l in lists:
        intersections = (intersections.intersection(l)
                         if intersections else set(l))
    return list(intersections)


print(retrieveIntersections(list1, list2))
