# doesn't have to be its own file, but this should contain the algorithms for actually computing the simulation

def sort_athlete_list(athlete_list):
    for i in range(1, len(athlete_list)):
        score = athlete_list[i].score
        low = 0
        high = i
        while high - low > 1:
            index = (low + high) // 2

            if athlete_list[index].score < score:
                low = index
            elif athlete_list[index].score > score:
                high = index
            else:
                break

        athlete_list.insert(high, athlete_list.pop(i))
    return athlete_list

def simulate_xc(athlete_list, random=False):
    team_dictionary = {}
    if random:  # one of these two will generate a list of athletes with their predicted race placement
        pass
    else:
        athlete_list = sort_athlete_list(athlete_list)
    team_list = []
    for i in range(len(athlete_list)):  # this is how I simulated XC scoring, there's probably a better way
        current = athlete_list[i]
        if current.team not in team_dictionary:
            team_dictionary[current.team] = len(team_list)
            team_list.append([0, 0, current.team])
        if team_list[team_dictionary[current.team]][1] < 5:
            team_list[team_dictionary[current.team]][1] += 1
            team_list[team_dictionary[current.team]][0] += (i + 1)
    team_list.sort()
    print(team_list)
    return team_list
