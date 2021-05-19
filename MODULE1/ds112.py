from typing import *
from math import fsum, sqrt
from collections import defaultdict
from random import sample
from functools import partial
from pprint import pprint

x = 10      # type: str
x: int = 10

def f(x: int, y: Optional[int], None) -> int:
    return x + y

def g(x: Sequence) -> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)


highs = [97.5, 10.2]        # type: list[float]
person = ("Raymond", 5 * 12 + 11)  #type Tuple[str, float]


d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)


#*****************************   k - mean   **************************
Point - Tuple[int, ...]
Centroid = Point

points = [(10, 41, 23),
          (22, 30, 29),
          (11, 42, 5),
          (20, 32, 4),
          (12, 40, 12),
          (21, 36, 23)]

def mean(data: Iterable[float]) -> float:
    "accurate aritmetic mean"
    data = list(data)
    return fsum(data) / len(data)

def dist(p: Point, q: Point, fsum = fsum, sqrt = sqrt, zip = zip) -> float:
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, List[Points]:
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key = partial(dist(point, centroid)))
        d[closest_centroid].append(point)
    return dict(d)

 def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
     return [tuple(map(mean, zip(*group))) for group in groups]

def k_means(data: Iterable[Point], k: int= 2, iterations: int = 50) -> List[Centroid]:
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids


#***********************************************************************
s = defaultdict(list)
# glob module, next(), list()