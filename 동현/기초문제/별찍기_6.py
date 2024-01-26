# 입력값 5
# N = 5
# 중첩반복문을 통해 별 출력
# range(N,0,-1) - N부터 0까지 역순으로 출력
# # -> 역순 : 출력값이 위로 갈수록 숫자가 커지기 떄문
# for i in range(N,0,-1):
#     # 출력값 - 홀수 단위
#     n = 2 * i - 1
#     # 줄바꿈
#     print('')
#     # 별 표시를 위한 반복문
#     # range를 통해 n갯수만큼 출력
#     for j  in range(n):
#         print('*', end='')

# 출력을 완료되었으나, 가운데 기준으로 대칭하는 방법???
# range(N,0,-1) - N부터 1까지 역순으로 값 출력
N = int(input())
for i in range(N,0,-1):
    # 공백은 N부터 i만큼 감소하며 출력,
    # * 모양은 홀수 갯수로 출력
    print(' '*(N-i) + '*'*(2*i-1))