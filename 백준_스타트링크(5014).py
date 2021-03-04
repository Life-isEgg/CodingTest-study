#F건물층수, S현재위치, G가야할 곳, U위, D아래
#출력 : 최소 누른 버튼의 횟수, G층에 갈 수 없다면, "use the stairs"
#bfs? 방문했던 층 표시


##백준에서 런타임에러남

from collections import  deque

def bfs():
    q = deque([(S,0)])

    while q:
        now, cnt = q.popleft() #현재 층과 버튼 누른 횟수
        if now == G:
            return cnt

        if now+U <= F and not visit[now+U]:
            visit[now+U] = 1
            q.append((now+U,cnt+1))
        if now-D >= 1 and not visit[now-D]:
            visit[now-D] = 1
            q.append((now-D,cnt+1))

        return "use the stairs"


F, S, G, U, D = map(int,input().split())
visit = [0 for _ in range(F+1)]
visit[S] = 1

print(bfs())


