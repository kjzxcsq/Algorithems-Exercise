class ModifiedMergeSort:
    def __init__(self, data):
        # Initialize class attributes
        self.data = list(set(data))  # Remove duplicates and store as list
        self.pieces = []  # To store the sub-pieces during sorting

    def __make_atoms(self):
        # Break the data into individual elements as sublists
        self.pieces = [[item] for item in self.data]

    def __combine(self):
        # Combine sub-pieces to create sorted pieces
        if len(self.pieces) % 2 != 0:
            # Ensure length is divisible by 2 by merging the last two sub-pieces
            self.pieces[-2].extend(self.pieces[-1])
            self.pieces.pop()

        updated_pieces = []  # Store the combined sorted sub-pieces
        for i in range(0, len(self.pieces), 2):
            left = self.pieces[i]
            right = self.pieces[i + 1]
            # Combine and sort the sub-pieces
            combined = self.__subpiece_sort(left + right)
            updated_pieces.append(combined)
        self.pieces = updated_pieces

    def __subpiece_sort(self, subpiece):
        # Sort the subpiece using basic comparison logic
        for i in range(len(subpiece)):
            for j in range(i + 1, len(subpiece)):
                if subpiece[i] > subpiece[j]:
                    subpiece[i], subpiece[j] = subpiece[j], subpiece[i]
        return subpiece

    def sorting(self):
        # Orchestrate the sorting procedure
        if not self.data:
            return self.data  # Return empty list if data is empty

        self.__make_atoms()  # Create atomic sublists
        while len(self.pieces) > 1:
            self.__combine()  # Combine and sort pieces

        return self.pieces[0]  # Return the final sorted list


class BinarySearch:
    def __init__(self, data):
        # Initialize with sorted data
        self.data = data

    def search(self, val):
        # Implement binary search logic
        if not self.data:
            return False  # Return False if data is empty

        low, high = 0, len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == val:
                return True  # Found the value
            elif self.data[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return False  # Value not found