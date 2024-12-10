class Queue:
    def __init__(self, data):
        # Initialize the queue with the provided data
        self.data = data

    def dequeue(self):
        # Allow the first person in the queue to enter
        if self.data:
            return self.data.pop(0)  # Removes and returns the first element
        return None  # Return None if queue is empty

    def enqueue(self, person):
        # Add person(s) to the end of the queue
        if isinstance(person, (int, float)):
            self.data.append(person)
        elif isinstance(person, (list, tuple)):
            self.data.extend(person)

    def is_member(self, person):
        # Check if a person is in the queue
        return person in self.data

class PriorityQueue(Queue):
    def __init__(self, data, priority):
        # Initialize with both data and priority
        super().__init__(data)
        self.data = list(zip(data, priority))  # Combine data and priority into tuples

    def sorted_queue(self):
        # Sort the queue by priority (highest first)
        self.data = sorted(self.data, key=lambda x: x[1], reverse=True)

    def enqueue(self, person, priority):
        # Add a new person with a priority to the queue
        self.data.append((person, priority))
        self.sorted_queue()  # Sort the queue after adding

    def dequeue(self):
        # Allow the person with the highest priority to enter
        if self.data:
            self.sorted_queue()  # Ensure the queue is sorted before dequeuing
            return self.data.pop(0)[0]  # Return the person (first element of tuple)
        return None  # Return None if queue is empty

    def is_member(self, person):
        # Check if a person is in the queue
        return any(person == item[0] for item in self.data)

class ImprovedPriorityQueue(PriorityQueue):
    def enqueue(self, person, priority):
        # Add a new person with a priority to the queue
        if isinstance(person, (list, tuple)) and isinstance(priority, (list, tuple)) and len(person) == len(priority):
            for p, pr in zip(person, priority):
                self.data.append((p, pr))
        elif isinstance(person, (int, float)) and isinstance(priority, (int, float)):
            self.data.append((person, priority))
        else:
            raise ValueError("Person and priority must be of matching and correct types")

    def dequeue(self):
        # Find and remove the person with the highest priority
        if self.data:
            max_priority_index = 0
            for i in range(1, len(self.data)):
                if self.data[i][1] > self.data[max_priority_index][1]:
                    max_priority_index = i
            person_with_highest_priority = self.data.pop(max_priority_index)
            return person_with_highest_priority[0]
        return None  # Return None if queue is empty

# Basic Queue Operations
queue = Queue([1, 2, 3])
print(queue.dequeue())  # Output: 1
queue.enqueue([4, 5])
print(queue.is_member(4))  # Output: True

# Priority Queue Operations
priority_queue = PriorityQueue([1, 2, 3], [10, 5, 8])
priority_queue.enqueue(4, 12)
print(priority_queue.dequeue())  # Output: 4
print(priority_queue.is_member(3))  # Output: True

# Improved Priority Queue Operations
improved_queue = ImprovedPriorityQueue([1.5, 10, 12, 2, 3], [22, 29, 31, 88, 66])
improved_queue.enqueue(0, 0)
print(improved_queue.dequeue()) 
print(improved_queue.is_member(3)) 
print(improved_queue.data)
