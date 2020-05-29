"""사용자가 일한 시간(hours)과 시급(rate per hour)을 프름프트에서 입력하면,
임금 총액을 계산해 주는 프로그램을 만들어 보세요. 35시간을 일 하고, 시간당 2.75 만큼을 벌었다고 가정하겠습니다.
(그러면, 임금 총액은 96.25가 됩니다).
여러분은 input 함수를 써서 문자열(string)타입을 읽어오게 되지만,
float()을 통해 변환을 해주어야 합니다.
"""

hour = float(input("Enter your hours: "))
p_hour=float(input("Enter your rate per hour: "))

total = hour * p_hour
print("total: ",total)

# total = float(hour) * float(p_hour) => OK

