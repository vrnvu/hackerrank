# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def slowClimbingLeaderboard(ranked, player):
    player_rankings = []
    current_best_score = float('inf')
    current_best_ranking = 0
    normalized_rankings = []
    for r in ranked:
        if r < current_best_score:
            current_best_score = r
            current_best_ranking += 1
            normalized_rankings.append(current_best_ranking)
        else:
            normalized_rankings.append(current_best_ranking)

    for p in player:
        for i, v in enumerate(ranked[::-1]):
            if p == v:
                player_rankings.append(normalized_rankings[len(ranked) - i - 1])
                break
            elif p < v:
                player_rankings.append(normalized_rankings[len(ranked) - i - 1] + 1)
                break
            elif p > v and i == len(ranked) - 1:
                player_rankings.append(1)
                break
            else:
                continue
    return player_rankings

def climbingLeaderboard(ranked, player):
    player_rankings = []
    current_best_score = float('inf')
    current_best_ranking = 0
    normalized_rankings = []
    for r in ranked:
        if r < current_best_score:
            current_best_score = r
            current_best_ranking += 1
            normalized_rankings.append(current_best_ranking)
        else:
            normalized_rankings.append(current_best_ranking)

    reversed_ranked = ranked[::-1]
    last_i = 0
    for p in player:
        for i, v in enumerate(reversed_ranked[last_i:]):
            i += last_i
            if p == v:
                player_rankings.append(normalized_rankings[len(ranked) - i - 1])
                last_i = i
                break
            elif p < v:
                player_rankings.append(normalized_rankings[len(ranked) - i - 1] + 1)
                last_i = i
                break
            elif p > v and i == len(ranked) - 1:
                player_rankings.append(1)
                last_i = i
                break
            else:
                continue
    return player_rankings



r = slowClimbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
print(r)
r = slowClimbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
print(r)
r = climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
print(r)
r = climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
print(r)
