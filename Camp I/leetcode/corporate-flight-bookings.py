class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0 for _ in range(n)]
        for booking in bookings:
            seats[booking[0] - 1] += booking[2]
            if booking[1] != n:
                seats[booking[1]] -= booking[2]
        for i in range(1, n):
            seats[i] += seats[i - 1]
        return seats