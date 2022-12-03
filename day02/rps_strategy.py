# map rps string to score
scores_key = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

outcomes_key = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

valid_choices = list(scores_key.keys())

# map code to rps string
opponent_key = {"A": "rock", "B": "paper", "C": "scissors"}
my_key = {"X": "rock", "Y": "paper", "Z": "scissors"}


def calc_total_score():
    def determine_score(opp_choice: str, my_choice: str):
        my_idx = valid_choices.index(my_choice)

        # win
        if valid_choices[my_idx - 1] == opp_choice:
            print(f"{my_choice} beats {opp_choice}!")
            outcome_score = 6
        # draw
        elif valid_choices[my_idx] == opp_choice:
            print(f"{my_choice} draws {opp_choice}!")
            outcome_score = 3
        # lose
        else:
            print(f"{my_choice} loses to {opp_choice}!")
            outcome_score = 0

        return outcome_score + scores_key[my_choice]

    with open("day02/input.txt") as f:
        total_score = 0
        for line in f.readlines():
            # opp {A, B, C}, my {X, Y, Z}
            opp_encoded, my_encoded = line.strip().split(" ")

            # 'rock', 'paper', or 'scissors'
            opp_choice = opponent_key.get(opp_encoded, None)
            my_choice = my_key.get(my_encoded, None)

            my_score = determine_score(opp_choice=opp_choice, my_choice=my_choice)
            total_score += my_score

    return total_score


def calc_total_score_but_different():
    def determine_score(opp_choice: str, my_choice: str):
        my_idx = valid_choices.index(my_choice)

        # win
        if valid_choices[my_idx - 1] == opp_choice:
            # print(f"{my_choice} beats {opp_choice}!")
            outcome_score = 6
        # draw
        elif valid_choices[my_idx] == opp_choice:
            # print(f"{my_choice} draws {opp_choice}!")
            outcome_score = 3
        # lose
        else:
            # print(f"{my_choice} loses to {opp_choice}!")
            outcome_score = 0

        return outcome_score + scores_key[my_choice]

    def determine_choice(outcome: str, opp_choice: str):

        opp_idx = valid_choices.index(opp_choice)

        # lose
        if outcome == "lose":
            # print(f"{outcome} {opp_choice} with {valid_choices[opp_idx - 1]}")
            return valid_choices[opp_idx - 1]
        # draw
        elif outcome == "draw":
            # print(f"{outcome} {opp_choice} with {valid_choices[opp_idx]}")
            return valid_choices[opp_idx]
        # win
        else:
            if opp_idx == 2:
                # print(f"{outcome} {opp_choice} with {valid_choices[0]}")
                return valid_choices[0]
            else:
                # print(f"{outcome} {opp_choice} with {valid_choices[opp_idx + 1]}")
                return valid_choices[opp_idx + 1]

    with open("day02/input.txt") as f:
        total_score = 0
        for line in f.readlines():
            # read encoded values
            opp_encoded, outcome_encoded = line.strip().split(" ")

            # decode as outcome and opponent choice
            outcome = outcomes_key.get(outcome_encoded, None)
            opp_choice = opponent_key.get(opp_encoded, None)

            # select proper choice given outcome
            my_choice = determine_choice(outcome=outcome, opp_choice=opp_choice)

            # calculate score for round
            my_score = determine_score(opp_choice=opp_choice, my_choice=my_choice)
            total_score += my_score

    return total_score


if __name__ == "__main__":
    # print(calc_total_score())
    print(calc_total_score_but_different())
