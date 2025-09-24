from typing import List

nums: List[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# result = 49


def area(h1, h2, p1, p2) -> int:
    return min(h1, h2) * (p2 - p1)


def max_area(height: List[int]) -> int:
    left: int = 0
    right: int = len(height) - 1

    max_ar: int = area(height[left], height[right], left, right)
    while left < right:
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        max_ar = max(max_ar, area(height[left], height[right], left, right))
    return max_ar


print(max_area(nums))