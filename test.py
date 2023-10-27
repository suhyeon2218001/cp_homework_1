# 안전공학 계산기 프로그램

# 안전율 계산 함수
def print_safety_factor(ultimate_strength, allowable_stress):
    result = ultimate_strength / allowable_stress
    return result

# 허용 응력 계산 함수
def print_allowable_stress(ultimate_strength, safety_factor):
    result = ultimate_strength / safety_factor
    return result

# 허용 하중 계산 함수
def print_allowable_load(allowable_stress, cross_section):
    result = allowable_stress * cross_section
    return result

# 사용자 입력 함수
def get_user_input():
    ultimate_strength = float(input("재료의 극한 강도를 입력하세요 : "))
    allowable_stress = float(input("허용 응력을 입력하세요 : "))
    cross_section = float(input("단면적을 입력하세요 : "))
    return ultimate_strength, allowable_stress, cross_section

# 메인 함수
def main():
    ultimate_strength, allowable_stress, cross_section = get_user_input()

    while True:
        print("안전공학 계산기")
        print("1. 안전율 계산")
        print("2. 허용 응력 계산")
        print("3. 허용 하중 계산")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            safety_factor = print_safety_factor(ultimate_strength, allowable_stress)
            print("안전율은 {:.2f} 입니다.".format(safety_factor))

        elif choice == "2":
            safety_factor = print_safety_factor(ultimate_strength, allowable_stress)
            allowable_stress = print_allowable_stress(ultimate_strength, safety_factor)
            print("허용 응력은 {:.2f} MPa 입니다.".format(allowable_stress))

        elif choice == "3":
            safety_factor = print_safety_factor(ultimate_strength, allowable_stress)
            allowable_stress = print_allowable_stress(ultimate_strength, safety_factor)
            allowable_load = print_allowable_load(allowable_stress, cross_section)
            print("허용 하중은 {:.2f} N 입니다.".format(allowable_load))

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 프로그램 실행
if __name__ == "__main__":
    main()
