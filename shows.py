SHOWS = [
    ' Avatar: The last Airbender',
    'The Legend  of Korra',
    'The Mandlorian',
    'the boys',
    ' The Walking Dad',
    'Strang Things',
    'Game of Thrones',
    'Breaki ng Bad',
    ' the office',
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))

main()