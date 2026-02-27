emoticon = 'v.v'

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ':)'
    say('I am here!')

def say(phrase):
    print(phrase + ' ' + emoticon)

main()