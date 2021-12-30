def correctness(bobs_decisions, expert_decisions): 
    score = 0

    for i in range(len(bobs_decisions)):
        if bobs_decisions[i] == expert_decisions[i]:
            score += 1
        elif bobs_decisions[i] == '?' or expert_decisions[i] == '?':
            score += 0.5

    return score
