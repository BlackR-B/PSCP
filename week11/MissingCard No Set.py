"""MissingCard"""
def main():
    """Main MissingCard"""
    suits = ['S', 'H', 'D', 'C']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    full_deck = [rank + suit for rank in ranks for suit in suits]
    remaining_cards = [input().strip() for _ in range(51)]
    missing_card = [card for card in full_deck if card not in remaining_cards]
    print(missing_card[0])
main()
