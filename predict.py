"""
predict.py
Road Damage Severity & Maintenance Recommendation
Member 4 - DriveGuard AI
"""


def calculate_road_damage_score(damage_count):

    if damage_count == 0:
        return 100

    elif damage_count <= 3:
        return 80

    elif damage_count <= 6:
        return 60

    elif damage_count <= 10:
        return 40

    else:
        return 20


def maintenance_recommendation(score):

    if score >= 80:
        return "Road condition is good."

    elif score >= 60:
        return "Minor road damage detected. Drive carefully."

    elif score >= 40:
        return "Moderate road damage. Vehicle inspection recommended."

    else:
        return "Severe road damage. Immediate maintenance is recommended."


if __name__ == "__main__":

    damage_count = 5

    score = calculate_road_damage_score(damage_count)

    print("Road Damage Score:", score)
    print("Recommendation:", maintenance_recommendation(score))
