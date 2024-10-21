"""Blackjack"""
def blackjack(number):
    """main Blackjack"""
    score = 0
    ace = 0
    for _ in range(number):
        card = input()
        if card in ("J", "Q", "K"):
            score += 10
        elif card == "A":
            score += 11
            ace += 1
        else:
            score += int(card)
    while score > 21 and ace:
        score -= 10
        ace -= 1
    print(score)
blackjack(int(input()))
