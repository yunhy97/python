scores = [90, 100, 87, 89, 82]

# 아래는 sum( )이라는 내장함수를 사용한다.
average = sum(scores) / len(scores)

if  average >= 80:
    print("평균 성적 {}으로 합격입니다.".format(average))
else:
    print("평균 성적 {}으로 불합격입니다.".format(average))