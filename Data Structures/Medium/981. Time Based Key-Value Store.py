class TimeMap:

    def __init__(self):
        self.map = {}

    def binary_search(self, times: list, target: int) -> int:
        # times = [1,4,6,10]
        l = 0
        r = len(times) - 1
        res = -1  # initialize to somethign

        while l <= r:
            m = (l + r) // 2

            if target >= times[m]:
                # choose to set res = m because evern if target is bigger than m, we can still pick m if nothing else is available.
                res = m
                # choose right section to search further
                l = m + 1
            else:
                # choose left
                r = m - 1

        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = ([], [])  # inititalize ([all times], [all values for those times])

        self.map[key][0].append(timestamp)  # append the timestamp
        self.map[key][1].append(value)  # append the value

    def get(self, key: str, timestamp: int) -> str:
        # edge case, if the key itself is not present
        if key not in self.map:
            return ""

        # get all internal keys for the main key to search
        times, values = self.map[key]

        # do binary search on it to get which value to return

        if timestamp < times[0]:
            return ""
        else:
            res = self.binary_search(times, timestamp)
            if res == -1:
                return ""

            return values[res]  # return value of time result index

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
