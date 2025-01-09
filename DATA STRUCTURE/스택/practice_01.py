# 1 스택에 A B C D를 순서대로 입력해서 B > C > D > A 와 같은 출력을 얻으려면 push()와 pop()의 호출 순서가 어떻게 되어야 하는지
## push(A) > push(B) > pop() > push(C) > pop() > push(D) > pop() > pop()

# 2 스택 클래스에 스택을 공백 상태로 초기화하는 clear() 연산을 추가하기
## def clear(self):
##      self.top = -1

# 3 스택 클래스에 모든 요소를 가장 먼저 들어온 요소부터 순서대로 화면에 출력하는 display() 연산 추가하기
## def display(self):
##      for i in range(0, self.top+1):
##          print(self.array[i], end=' ')
##      print()

# 4 checkBrackets()로 다음 문자열의 괄호 사용을 검사하려고 함
#   알고리즘을 추적하여 각 단계에서 스택의 내용이 변경되는 것을 그려서 설명
# (a) for (i=1; i<10; i++) a[i] = a[(i+1)];
# (b) a { b [ (c+d) -e] *f}

# 연산 결과 스택에 남아 있는 내용을 순서대로 적기
# values = Stack()
# for i in range(20):
#   if i % 3 == 0:
#       values.push(i)
#   elif i % 4 == 0:
#       values.pop()
## 18, 12, 9, 0

# 6 문자열을 뒤집어 출력하는 프로그램을 순환 호출을 이용해 구현하기
#   순환 호출은 시스템 스택을 이용하므로 추가적인 스택을 사용할 필요는 없지만 순환 호출 함수를 하나 만들어야 함
#   다음 코드를 완성해 텍스트인 '자료구조'가 뒵집혀서 '조구료자'로 출력되도록 하기
# def printReverse(msg, len):
#   ... # 구현할 부분
#   instr = "자료구조"
#   printReverse(instr, len(instr))

## def printReverse(msg, len):
##      if len > 0:
##          print(msg[leen-1])
##          printReverse(msg, len-1)