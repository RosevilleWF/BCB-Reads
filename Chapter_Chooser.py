import random
import time
from typing import List, Dict

from menu import Menu

# I personally try to avoid having floating variables unless they are "Configuration Variables" that do not change during program operation
CHAPTERS_PER_ROUND = 9

# Puts all chapters into lists, by number of major roles
majors_2 = ["After You", "Another Direction", "Escape Route", "Ice Breaker", "PDA"]
majors_3 = ["A New Leaf", "Another Date", "Candied Bacon", "Helping Hands", "Leaving Home",
            "Local Area", "Mutual Assurance", "Pick Me Up", "To The Top", "Wonderland", "Seeing Stars", "Trapped"]
majors_4 = ["A Better You", "Adult Supervision", "Blind Date", "Catty Remarks", "Date Night,", "December",
            "Dial Tone", "Dinner Time", "Door to Door", "Elementary School Sweethearts", "Gone Fishing",
            "Just Beautiful", "Merry Snow Day", "Minicomics 11-20", "Onwards to Adventure", "Safe Boundaries",
            "Time Out"]
majors_5 = ["Another Shoulder", "Behind Closed Doors", "Blood Lust", "Boy Toy", "Call Waiting", "Carry Me", "Carry On",
            "Carry On", "Casting Call", "Clean Slate", "College Material", "Critical Hit", "Eternal Flame",
            "Farewell, Middle School", "Featured Attraction", "Fuel Economy", "Gaming Rivalry", "Good Enough",
            "Guest of Honor", "Left Behind", "Link Play", "Mother's Day", "New Beginnings", "New Year's Resolution",
            "Off to the Movies", "Piece of Cake", "Simple Pleasures", "Small Fry", "Starting Over",
            "The Burden of Parenthood", "Track Meet", "Wardrobe Malfunction"]

majors_6 = ["A Difficult Choice", "A Distance Apart", "Bonding", "Curtain Call", "Enter High School", "Everyday Life",
            "Flirting with Disaster", "Grave Concern", "Hot Pursuit", "Humble Pursuit", "Humble Approach",
            "It's All in the Mind", "Love My Way", "Minicomics 1-10", "Minicomics 21-30", "Model Girlfriend",
            "Pep Rally", "Popularity Contest", "Prom Preparation", "Puppy Love", "Rising Temperature", "Show and Tell",
            "Study Buddy", "Unfit for Education", "Unrequited"]

majors_7 = ["Burnt Bridges", "Fair Game", "Field Day", "High Expectations", "Intervention", "Magic Tricks",
            "Mischief Night", "Photo Day", "Troubled Waters", "Unfulfilled Fantasy"]

majors_8 = ["Arrival", "Back and Forth", "Feline Festivities", "Follow Me", "Golden Hour", "Search and Rescue",
            "Unspoken Rule", "Witch Hunt"]

majors_9 = ["Double Down", "Happy Hour", "Invitation", "Table for One", "Take Heart", "Total Recall"]

majors_10 = ["Breaking Up", "Feline Filibuster", "Method Acting", "Moments Apart", "Out of Frame", "Under Pressure"]

majors_11 = ["Ten Seconds to Midnight"]

majors_12 = ["At Loose Ends", "Moving On", "Volume 1 Birthdays"]

majors_13 = ["A Different Side", "Love Again", "Pillow talk"]

# Dicts are my favorite thing ever, in other languages I would be using a map/hashmap for this purpose
# Organizing each chapter by number of parts.
chapters_by_parts_dict: Dict[int, List[str]] = {
    2: majors_2,
    3: majors_3,
    4: majors_4,
    5: majors_5,
    6: majors_6,
    7: majors_7,
    8: majors_8,
    9: majors_9,
    10: majors_10,
    11: majors_11,
    12: majors_12,
    13: majors_13,
}


def get_list_of_chapters(
        num_of_participants: int,
        list_size: int,
        banned_chapters: List[str] = None,
) -> List[str]:
    """
    Make a list of all the valid chapters
    :param num_of_participants: Number of people playing
    :param banned_chapters: Chapters we want to exclude
    :return: Sorted list of eligable chapters
    """

    print("Getting list of chapters...")

    # If we have not defined a max number of participants, let's just do two roles per player
    max_roles = num_of_participants * 2

    # Get all the chapters valid to our query
    list_of_chapters: List[str] = []
    pool_to_select_from: List[str] = []

    # Starting from lower parts, moving up to more parts...
    for participant_number, chapters in chapters_by_parts_dict.items():

        # If not enough roles, skip this MF
        if participant_number < num_of_participants:
            continue

        # Little debug message, uncomment if you want :)
        # if participant_number > num_of_participants:
        #     print(f"Currently have [{len(list_of_chapters)}] chapters, but we ran out of chapters from pool of chapters with {participant_number - 1} parts, Adding chapters from pool of chapters with {participant_number} parts")

        # Fill the selection pool
        pool_to_select_from = chapters.copy()

        # Keep randomly picking from this pool until we have enough chapters or the pool is empty...
        # When this while loop ends, we will move on to next stage of the above for loop
        while len(pool_to_select_from) > 0:

            # Select a random chapter...
            choice_index = random.randint(0, len(pool_to_select_from) - 1)

            # Remove the choice from the list, then we'll examine it 👁️🔎
            chapter: str = pool_to_select_from.pop(choice_index)

            # If there are banned chapters, and this chapter is in it, then move on to next loop
            if banned_chapters and chapter in banned_chapters:
                continue

            # This baby is good to stick in the oven
            list_of_chapters.append(chapter)
            if len(list_of_chapters) >= list_size:
                # When we use a return, we end all the loops we are in for this function
                list_of_chapters.sort()
                return list_of_chapters

    # Return da list (sorted)
    # This would onl y occur if the list_size input was shorter than the total available pool of chapters available to select from
    # print(f"Ran out of chapters lol, you have {len(list_of_chapters)} chapters")
    list_of_chapters.sort()
    return list_of_chapters


def display_list_w_numbers(list: List[str]) -> None:
    """
    Display a list of chapters with an index number
    The idea i have here, is you could just type a number to select a chapter.
    """
    if list is None or len(list) == 0:
        print("--No chapters to display--")
        return

    for index, chapter in enumerate(list):
        print(f"{index}: {chapter}")


def select_chapter(chapter_index: int, chapter_list: List[str], ban_list: List[str]):
    chapter: str | None = None
    try:
        chapter = chapter_list.pop(chapter_index)
        ban_list.append(chapter)
        print(f"Ban list so far", ban_list)
    except Exception as err:
        print(f"You fucked up! Tried to select from a chapter list with an invalid index! {err}")
        raise err


def select_chapter_menu(chapter_list: List[str], ban_list: List[str] = []):
    """
    Select a chapter from a list of chapters. We return a ban list whether the user inputs one or not
    :param chapter_list: List of chapters to select from
    :param ban_list: Chapters that have been selected or pre-chosen to not show up
    :return:
    """
    menu_children: List[Menu] = []

    # Set up all the menu selection options
    for index, chapter in enumerate(chapter_list):
        menu_children.append(Menu(f"{chapter}", None, lambda idx=index: select_chapter(idx, chapter_list, ban_list)))

    # Create select chapter menu
    menu = Menu("Select Chapter", "Select a chapter to read", None, menu_children)

    # Run the menu
    menu.menu_loop()


def ban_chapter_menu(chapter_list: List[str], ban_list: List[str] = []) -> None:
    user_input: str = ''
    while user_input != 'DONE':
        user_input = input("Type any chapter you would like to ban. Type \'DONE\' when you are finished")

        # Copying this code from the Menu class
        # TBH I should be using a menu here, but I hate the way I wrote menus RN so they can fug off
        select_index: int = -1

        # If this is a number see if it's an index number for our menu
        if user_input.isdigit():
            if len(chapter_list) > int(user_input) >= 0:
                select_index = int(user_input)
        else:
            selected_children: List[str] = []
            for chapter in chapter_list:
                if user_input in chapter:
                    selected_children.append(chapter)

            # If more than one option matches, GTFO
            if len(selected_children) > 1:
                print("More than one option matches your input")
                for chapter in enumerate(selected_children):
                    print(f"{chapter}")
                continue

            # This matches with an option, select it!
            if len(selected_children) == 1:
                select_index = 0

        if select_index is not None:
            selected_chapter: str = chapter_list[select_index]
            print(f"You selected \'{selected_chapter}\'")
            ban_list.append(selected_chapter)


def main_loop() -> None:
    print("Hello Rosie!")

    # Define lists
    ban_list = []

    # Because I like some delay (As a treat)💅🏻
    time.sleep(1)

    # Allows input for number of readers, which determines the lists from which chapters are pulled
    # Is this a valid number?
    part_count: str
    try:
        part_count = input("Please enter number of readers: ")
    except Exception as e:
        print(f"Ran into a problem parsing out part count {e}")
        return
    part_count_int = int(part_count)

    all_possible_chapters = get_list_of_chapters(
        num_of_participants=part_count_int,
        list_size=999,
        banned_chapters=ban_list
    )
    # Display all of our options to make banning easier
    display_list_w_numbers(all_possible_chapters)

    # Handle banning chapters...
    ban_chapter_menu(
        chapter_list=all_possible_chapters,
        ban_list=ban_list
    )

    read_count = 0
    while read_count < 4:  # Stops program after 4 reads have been completed
        selection_list: List[str] = get_list_of_chapters(part_count_int, CHAPTERS_PER_ROUND, ban_list)
        select_chapter_menu(selection_list, ban_list)
        read_count += 1
        print("\n---\n")
        print(f"Reads selected so far: {read_count}")
    print("done")


if __name__ == "__main__":
    main_loop()
