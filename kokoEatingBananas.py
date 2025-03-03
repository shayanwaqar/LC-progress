class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = r
        while l <= r:
            mid = (l+r) // 2
            if self.works(mid, piles, h):
                speed = min(speed, mid)
                r = mid - 1
            else:
                l = mid + 1
        return speed
        

    def works(self, k, piles, h): #k is eating speed
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
        return True if time <= h else False
