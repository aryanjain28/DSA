from heapq import heappop, heappush


def shortest_in_k(n, edges, src, dst, k):

    adjList = {i: [] for i in n}
    for s, d, wt in edges:
        adjList[s].append((d, wt))

    main, tmp = {}, {src: 0}
    for node in n:
        main[node] = float("inf")
    main[src] = 0

    for _ in range(k+1):

        q = [("A", 0)]
        while q:
            node, distance = q.pop(0)

            if distance < main[node]:
                tmp[node] = distance

            for neighbor, d2 in adjList[node]:
                q.append((neighbor, main[node] + d2))

        main = tmp

    print(main)


shortest_in_k(["A", "B", "C"], [("A", "B", 100),
                                ("A", "C", 500),
                                ("B", "C", 100),
                                ], "A", "C", 1)
