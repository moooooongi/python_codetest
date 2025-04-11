import heapq
import sys
input = sys.stdin.readline
INF = float("inf")
def dijkstra(s,n, graph):
    distance = [INF for _ in range(n+1)]
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
    while q :
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n+1)]

    distance = [INF for _ in range(n+1)]
    for i in fares :
        graph[i[0]] += [[i[1],i[2]]]
        graph[i[1]] += [[i[0],i[2]]]
    go_with = dijkstra(s,n, graph)
    for i in range(1,n+1):
        distance = [INF for _ in range(n+1)]
        go_solo = dijkstra(i,n,graph)
        if answer > go_with[i] + go_solo[a]+go_solo[b] :
            answer = go_with[i] + go_solo[a]+go_solo[b]
    return answer