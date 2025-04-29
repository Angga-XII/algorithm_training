import heapq

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sx, sy, dx, dy = map(int, input().split())

        # Wormholes: List of (entry_x, entry_y, exit_x, exit_y, cost)
        wormholes = []
        for _ in range(n):
            wormholes.append(tuple(map(int, input().split())))

        # Build nodes list: source, destination, and all wormhole endpoints
        nodes = [(sx, sy), (dx, dy)]
        for w in wormholes:
            ex, ey, ex2, ey2, cost = w
            nodes.append((ex, ey))
            nodes.append((ex2, ey2))

        # Total nodes: 2 + 2*N
        node_count = len(nodes)

        # Build adjacency list: graph[i] = list of (neighbor_index, cost)
        graph = [[] for _ in range(node_count)]

        # Add normal movement (Manhattan distance) edges between all pairs
        for i in range(node_count):
            for j in range(node_count):
                if i != j:
                    cost = manhattan_distance(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])
                    graph[i].append((j, cost))

        # Add wormhole edges (shortcut cost)
        for idx, w in enumerate(wormholes):
            ex, ey, ex2, ey2, cost = w
            # Wormhole ends are at nodes 2 + idx*2 and 2 + idx*2 + 1
            node1 = 2 + idx * 2
            node2 = node1 + 1
            # Add bi-directional wormhole with fixed cost
            graph[node1].append((node2, cost))
            graph[node2].append((node1, cost))

        # Now run Dijkstra's algorithm from source node (index 0)
        dist = [float('inf')] * node_count
        dist[0] = 0
        heap = [(0, 0)]  # (cost_so_far, node_index)

        while heap:
            cost_so_far, u = heapq.heappop(heap)

            if cost_so_far > dist[u]:
                continue  # already found a better path

            for v, edge_cost in graph[u]:
                if dist[v] > dist[u] + edge_cost:
                    dist[v] = dist[u] + edge_cost
                    heapq.heappush(heap, (dist[v], v))

        # Output minimum cost to reach destination (index 1)
        print(dist[1])

import time
if __name__ == "__main__":
    t0 = time.time()
    solve()
    t1 = time.time()
    print("process time: " + str(t1 - t0))