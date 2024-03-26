def calculate_score(participant):
    
    score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
    return score

def create_scoreboard(participants):
    
    for participant in participants:
        participant['score'] = calculate_score(participant)
    
    
    sorted_participants = sorted(participants, key=lambda x: (-x['score'], x['name']))
    
    
    scoreboard = [{'name': participant['name'], 'score': participant['score']} for participant in sorted_participants]
    
    return scoreboard