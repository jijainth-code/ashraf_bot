from random import randint, choice

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Silent treatment, huh? Playing hard to get, I see! 😏'
    elif 'hello' in lowered:
        return 'Well, hey there, handsome! 😉'
    elif 'how are you' in lowered:
        return 'Better now that you’re here, darling! 😘'
    elif 'bye' in lowered:
        return 'Oh no, leaving so soon? Come back soon, sugar! 💔'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)} – but you know, you’re already a winner to me! 🌈✨'
    else:
        return choice([
            'Ooh, mysterious! Tell me more, handsome! 😏',
            'Hmm, you’re talking, but all I hear is “kiss me”! 😘',
            'Oh honey, I didn’t quite get that, but you sure have my attention! 💖'
        ])
