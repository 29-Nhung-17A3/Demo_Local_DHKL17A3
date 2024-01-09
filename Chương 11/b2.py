def find_worst_captain(teams):
    if not teams:
        return None
    worst_team = teams[-1]
    worst_captain = worst_team[1] 
    return worst_captain
def main():
    teams = [['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce'], ['David', 'Jack', 'Bill', 'Tom', 'Mike', 'Daniel'], ['Alexander', 'Adam', 'Payam', 'Kevin', 'Sigal', 'Mike']]
    while True:
        team_name = input("Nhập tên đội (nhập 'done' để kết thúc): ")
        if team_name.lower() == 'done':
            break
        coach = input("Nhập tên huấn luyện viên: ")
        captain = input("Nhập tên đội trưởng: ")
        players = input("Nhập tên các vận động viên (cách nhau bằng dấu phẩy): ").split(',')
        team = [team_name, captain, coach] + players
        teams.append(team)
    worst_captain = find_worst_captain(teams)
    if worst_captain:
        print(f"Đội trưởng của đội tệ nhất là: {worst_captain}")
    else:
        print("Không có đội nào trong danh sách.")

if __name__ == "__main__":
    main()
