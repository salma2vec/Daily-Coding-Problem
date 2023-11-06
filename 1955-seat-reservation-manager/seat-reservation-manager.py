import heapq

class SeatManager:

    def __init__(self, n: int):
        """
        Initializes a SeatManager object that will manage n seats numbered from 1 to n.
        
        Args:
            n (int): The total number of seats.
        """
        self.available_seats = list(range(1, n + 1))

    def reserve(self) -> int:
        """
        Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.

        Returns:
            int: The seat number of the reserved seat.
        """
        if self.available_seats:
            return heapq.heappop(self.available_seats)
        return -1  # No available seats

    def unreserve(self, seatNumber: int) -> None:
        """
        Unreserves the seat with the given seatNumber.
        
        Args:
            seatNumber (int): The seat number to unreserve.
        """
        heapq.heappush(self.available_seats, seatNumber)

# Example of usage:
# seatManager = SeatManager(5)
# seat1 = seatManager.reserve()
# seat2 = seatManager.reserve()
# seatManager.unreserve(seat2)
# seat3 = seatManager.reserve()
# ...
