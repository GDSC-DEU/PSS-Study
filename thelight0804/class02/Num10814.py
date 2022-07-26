"""
Date:
    22.07.24
Title:
    BAEKJOON 10814번
Project:
    나이순 정렬
Level:
    Silver 5
Name:
    thelight0804
"""

import sys

testNum = int(sys.stdin.readline())
# member = ["21 Junkyu", "21 Dohyun", "20 Sunyoung"]
member = [] #온라인 저지에 가입한 사람들
for i in range(testNum):
  member.append(sys.stdin.readline().rstrip())

#나이 정렬
member.sort(key = lambda member: int(member.split()[0]))

for i in range(len(member)):
  print(member[i])