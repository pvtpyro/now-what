from story import story

def display_scene(text, options):
    print("\n" + text)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option['text']}")

def get_user_choice(num_options):
    while True:
        try:
            choice = int(input("Choose an option: ")) - 1
            if 0 <= choice < num_options:
                return choice
            else:
                print(f"Please choose a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    current_scene = "start"

    while True:
        scene = story[current_scene]
        display_scene(scene['text'], scene['choices'])

        # ending
        if not scene['choices']:
            print("~Fin")
            break

        # get users choice
        choice = get_user_choice(len(scene['choices']))

        # move to next scene based on above choice
        current_scene = scene['choices'][choice]['next']

main()