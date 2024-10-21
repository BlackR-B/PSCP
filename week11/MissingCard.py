"""MissingCard No Set"""
def main():
    """Main MissingCard No Set"""
    suits = ['S', 'H', 'D', 'C']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    full_deck = set(rank + suit for rank in ranks for suit in suits)
    remaining_cards = set(input().strip() for _ in range(51))
    missing_card = full_deck - remaining_cards
    print(missing_card.pop())
main()
