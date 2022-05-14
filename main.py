import csv
import html_parser
import runner
import simulate_race


def create_runners():  # will create a runner for every runner contained within RelevantTeamTimes.csv
    athlete_list = []
    with open("RelevantTeamTimes.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        next(csv_reader)
        athlete_info = next(csv_reader)
        while True:  # not too familiar with csvs, I just need to skip 2 lines total according to RelevantTeamTimes.csv
            print(athlete_info)
            current = runner.athlete(athlete_info[0], athlete_info[2], athlete_info[-1],  int(athlete_info[-2][0]) * 60 + int(athlete_info[-2][2:]))
            next(csv_reader)
            next(csv_reader)
            line = next(csv_reader)
            while line != []:
                current.add_event(line[4], line[5], line[2] + line[3])  # make the month and day thing better later
                line = next(csv_reader)
            athlete_list.append(current)
            athlete_info = next(csv_reader)
            if athlete_info == ["end"]:
                break
        return athlete_list


html_parser.restart_csv()  # creates the csv file
team_list = ["1023", "1015"]
for team in team_list:
    html_parser.getTopSchool(team)
with open("RelevantTeamTimes.csv", "a") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["end"])

athlete_list = create_runners()  # creates the runners
for athlete in athlete_list:
    athlete.calculate_score()

print([x[-1] for x in simulate_race.simulate_xc(athlete_list)])  # prints the predicted results
