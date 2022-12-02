OppRock = "A"
OppPapr = "B"
OppScsr = "C"
SelfRock = "X"
SelfPapr = "Y"
SelfScsr = "Z"
PointRock = 1
PointPapr = 2
PointScsr = 3
PointLose = 0
PointTie = 3
PointWin = 6
OutcomeLose = "X"
OutcomeTie = "Y"
OutcomeWin = "Z"

SCORE_LOOKUP_1 = {
    f"{OppRock} {SelfRock}": PointRock + PointTie,
    f"{OppRock} {SelfPapr}": PointPapr + PointWin,
    f"{OppRock} {SelfScsr}": PointScsr + PointLose,
    f"{OppPapr} {SelfRock}": PointRock + PointLose,
    f"{OppPapr} {SelfPapr}": PointPapr + PointTie,
    f"{OppPapr} {SelfScsr}": PointScsr + PointWin,
    f"{OppScsr} {SelfRock}": PointRock + PointWin,
    f"{OppScsr} {SelfPapr}": PointPapr + PointLose,
    f"{OppScsr} {SelfScsr}": PointScsr + PointTie,
}

SCORE_LOOKUP_2 = {
    f"{OppRock} {OutcomeLose}": PointScsr + PointLose,
    f"{OppRock} {OutcomeTie}": PointRock + PointTie,
    f"{OppRock} {OutcomeWin}": PointPapr + PointWin,
    f"{OppPapr} {OutcomeLose}": PointRock + PointLose,
    f"{OppPapr} {OutcomeTie}": PointPapr + PointTie,
    f"{OppPapr} {OutcomeWin}": PointScsr + PointWin,
    f"{OppScsr} {OutcomeLose}": PointPapr + PointLose,
    f"{OppScsr} {OutcomeTie}": PointScsr + PointTie,
    f"{OppScsr} {OutcomeWin}": PointRock + PointWin,
}


def part_1(input: str) -> int:
    return sum([SCORE_LOOKUP_1[line] for line in input.strip().splitlines()])


def part_2(input: str) -> int:
    return sum([SCORE_LOOKUP_2[line] for line in input.strip().splitlines()])
