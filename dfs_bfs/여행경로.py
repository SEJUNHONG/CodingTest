from collections import deque

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] #[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

def solution(tickets):
    answer = []
    queue = deque()
    queue.append(("ICN", ["ICN"], []))

    while queue:
        airport, path, used = queue.popleft()
        if len(used) == len(tickets):
            answer.append(path)
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                queue.append((ticket[1], path+[ticket[1]], used+[idx]))

    answer.sort()
    return answer[0]

print(solution(tickets))