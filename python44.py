is_magician = True
is_expert = False

if is_expert and is_magician:
    print("You are a master magician!")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print("You need magic powers")