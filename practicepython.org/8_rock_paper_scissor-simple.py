__author__ = "Geoffrey Bachelot"


def rock_paper_scissors():
    players = [
        {
            'name': "player1",
            'score': 0,
            'pick': None
        },
        {
            'name': "player2",
            'score': 0,
            'pick': None
        }
    ]

    comps = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    picks = {}

    while True:
        for player in players:
            while player['pick'] not in comps.keys() or None:
                player['pick'] = input(
                    f"Hello {player['name']}, "
                    f"please pick a weapon between {list(comps.keys())}: "
                )

        if players[0]['pick'] == players[1]['pick']:
            print('draw')
        elif comps[players[0]['pick']] == players[1]['pick']:
            players[0]['score'] += 1
            print(f"{players[0]['name']} win")
        else:
            players[1]['score'] += 1
            print(f"{players[1]['name']} win")

        if input('Do you want to continue playing ?').lower() == 'no' or 'n':
            break
        else:
            for player in players:
                player['pick'] = None
            continue


if __name__ == "__main__":
    rock_paper_scissors()