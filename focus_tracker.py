import datetime
import random
import statistics
import json
import os

# -----------------------------
# 전역 변수 및 초기 설정
# -----------------------------
DATA_FILE = "focus_data.json"
sessions = []  # 집중 세션 저장 리스트

actions = [
    "물 한 컵 마시기",
    "5분 스트레칭하기",
    "눈 감고 1분 휴식하기",
    "간단한 산책하기",
    "심호흡 5회 하기"
]

# -----------------------------
# 유틸 함수
# -----------------------------
def pause():
    input("\n엔터를 누르면 메인 메뉴로 돌아갑니다.")

def get_today_str():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# -----------------------------
# 기능 구현
# -----------------------------
def record_session():
    while True:
        time_input = input("집중한 시간(분)을 입력하세요 (종료하려면 엔터): ")
        if time_input == "":
            break

        if not time_input.isdigit():
            print("숫자를 입력해주세요.")
            continue

        minutes = int(time_input)
        memo = input("메모를 입력하세요 (엔터로 생략): ")

        session = {
            "date": get_today_str(),
            "minutes": minutes,
            "memo": memo
        }

        sessions.append(session)
        print("세션이 저장되었습니다.")

    pause()

def today_statistics():
    today = get_today_str()
    today_sessions = [s["minutes"] for s in sessions if s["date"] == today]

    if not today_sessions:
        print("오늘 기록된 집중 세션이 없습니다.")
        pause()
        return

    print(f"\n오늘 날짜: {today}")
    print(f"세션 개수: {len(today_sessions)}")
    print(f"총 집중 시간: {sum(today_sessions)} 분")
    print(f"평균 집중 시간: {statistics.mean(today_sessions):.1f} 분")

    if len(today_sessions) >= 2:
        print(f"표준편차: {statistics.stdev(today_sessions):.1f}")
    else:
        print("표준편차: 계산 불가 (세션 1개)")

    pause()

def overall_statistics():
    if not sessions:
        print("기록된 집중 세션이 없습니다.")
        pause()
        return

    times = [s["minutes"] for s in sessions]

    print("\n전체 기록 통계")
    print(f"전체 세션 개수: {len(times)}")
    print(f"누적 집중 시간: {sum(times)} 분")
    print(f"평균 집중 시간: {statistics.mean(times):.1f} 분")

    if len(times) >= 2:
        print(f"표준편차: {statistics.stdev(times):.1f}")
    else:
        print("표준편차: 계산 불가 (세션 1개)")

    print(f"가장 긴 집중 시간: {max(times)} 분")
    print(f"가장 짧은 집중 시간: {min(times)} 분")

    pause()

def random_action():
    action = random.choice(actions)
    print(f"\n추천 행동: {action}")
    pause()

def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(sessions, f, ensure_ascii=False, indent=2)
        print("데이터가 성공적으로 저장되었습니다.")
    except Exception:
        print("파일 저장 중 오류가 발생했습니다.")
    pause()

def load_data():
    global sessions

    if not os.path.exists(DATA_FILE):
        print("저장된 데이터 파일이 없습니다.")
        pause()
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            sessions = json.load(f)
        print("데이터를 성공적으로 불러왔습니다.")
    except Exception:
        print("데이터 형식이 올바르지 않습니다.")
        sessions = []

    pause()

# -----------------------------
# 메인 메뉴
# -----------------------------
def main_menu():
    while True:
        print("\n====== 집중력 관리 프로그램 ======")
        print("1. 집중 세션 기록하기")
        print("2. 오늘 집중 통계 보기")
        print("3. 전체 기록 통계 보기")
        print("4. 랜덤 행동 추천 받기")
        print("5. 데이터 저장하기")
        print("6. 데이터 불러오기")
        print("7. 프로그램 종료")

        choice = input("메뉴 번호를 선택하세요: ")

        if choice == "1":
            record_session()
        elif choice == "2":
            today_statistics()
        elif choice == "3":
            overall_statistics()
        elif choice == "4":
            random_action()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "7":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력해주세요.")

# -----------------------------
# 프로그램 시작
# -----------------------------
if __name__ == "__main__":
    main_menu()
