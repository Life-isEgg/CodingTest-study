# 조합으로 팀 조합 만든 후 능력치 비교
from itertools import combinations
from _collections import deque
import sys

#input
n = int(input()) #총인원
power = [list(map(int, input().split())) for _ in range(n)] #각각의 능력치
members = [i for i in range(n)] #각 선수들에게 0부터 n-1번까지 번호부여
team = deque(combinations(members,n//2)) #팀 조합 ex)0,1,2,3 -> (0,1),(0,2),(0,3),(1,2),(1,3),(2,3)


#능력치 합 구하는 함수
def power_hap(team_list, power_list):
    n = len(team_list)
    hap = 0
    for i in range(n-1):
        for j in range(i+1, n):
            hap = hap + power_list[team_list[i]][team_list[j]] + power_list[team_list[j]][team_list[i]]
    return hap


minp = sys.maxsize #정수최댓값으로 최소값 설정

start_team = []
link_team = []

for _ in range(len(team)//2):  #조합의 경우의 수를 반으로 나눴을 떄 서로 반대로 짝꿍
    start_team.append(team.pop())
    link_team.append(team.popleft())

for i in range(len(start_team)):
    ans = abs(power_hap(start_team[i],power) - power_hap(link_team[i],power))
    if ans < minp:
        minp = ans

print(minp)


