class Dijkstra:
    def __init__(self, graph, start_node, end_node):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node
        
        # Grab the list of all nodes from the graph dictionary keys
        self.nodes = list(self.graph.keys())
        
        # Additional attributes initialized later
        self.node_val = None
        self.base_val = None
        self.visited = None
        self.route = None

    def __initialize(self):
        n = len(self.nodes)
        self.node_val = [float('inf')] * n
        start_index = self.nodes.index(self.start_node)
        self.node_val[start_index] = 0
        
        # The base_val holds the current node's "value" at each step
        self.base_val = 0
        
        # Visited array indicates which nodes have been permanently chosen
        self.visited = [False] * n
        self.visited[start_index] = True
        
        # Route dictionary will store {child_node: parent_node}
        self.route = {}

    def __get_neighbours(self, node):
        return self.graph[node]

    def __visited_node(self, node):
        index = self.nodes.index(node)
        self.visited[index] = True

    def __check_visited(self, node):
        index = self.nodes.index(node)
        return self.visited[index]

    def __is_neighbour(self, node_1, node_2):
        return node_2 in self.graph[node_1]

    def __update_node_val(self, current_node):
        current_index = self.nodes.index(current_node)
        current_val = self.node_val[current_index]  # or self.base_val
        
        neighbours = self.__get_neighbours(current_node)
        for neigh, weight in neighbours.items():
            # Only proceed if unvisited
            if not self.__check_visited(neigh):
                neigh_index = self.nodes.index(neigh)
                # If we find a shorter path to this neighbor
                if self.node_val[neigh_index] > current_val + weight:
                    self.node_val[neigh_index] = current_val + weight
                    self.route[neigh] = current_node

    def __get_min_val(self):
        min_value = float('inf')
        for i, node in enumerate(self.nodes):
            if not self.visited[i] and self.node_val[i] < min_value:
                min_value = self.node_val[i]
        return min_value

    def __next_node(self, current_node):
        # 1. Update neighbors
        self.__update_node_val(current_node)
        
        # 2. base_val updated from the unvisited nodes
        next_val = self.__get_min_val()
        self.base_val = next_val
        
        # 3. Find which node has this next_val and is unvisited
        for i, node in enumerate(self.nodes):
            if not self.visited[i] and self.node_val[i] == next_val:
                return node
        
        # If none found (disconnected components scenario), return None
        return None

    def find_path(self):
        # Step 0: Initialize
        self.__initialize()
        
        # Start from the start_node
        current_node = self.start_node
        
        # We'll keep traversing until we visit the end_node or run out of options
        while True:
            # If we've reached the end_node, no need to continue
            if current_node == self.end_node:
                break
            
            # Pick the next node to move to
            next_node = self.__next_node(current_node)
            if next_node is None:
                # No more reachable unvisited nodes (disconnected or no path)
                break
            
            # Mark that node visited
            self.__visited_node(next_node)
            current_node = next_node
        
        # Once done, reconstruct the path using self.route
        path = [self.end_node]
        
        # Work backward from end_node, stopping when we reach start_node or can't go further
        while True:
            node = path[-1]
            if node == self.start_node:
                break
            if node not in self.route:
                # No path found if we never set a predecessor for this node
                break
            path.append(self.route[node])
        
        # The path list is from end to start, so reverse it
        path.reverse()
        
        return path