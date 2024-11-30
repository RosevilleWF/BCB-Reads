import time
import random

#Puts all chapters into lists, by number of major roles
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

#Define lists
ban_list = []
select_list = []
sorted_select = []
count = 0
chosen_chapter = None
element = None

print("Hello Rosie!")
#Because I like some delay (As a treat)
time.sleep(1)

#Allows input of chapters to be removed from each chapter list, using "DONE" as the input to continue
while element != "DONE":
    element = input("Enter banned chapter: ")
    if element in majors_2:
        majors_2.remove(element)
    elif element in majors_3:
        majors_3.remove(element)
    elif element in majors_4:
        majors_4.remove(element)
    elif element in majors_5:
        majors_5.remove(element)
    elif element in majors_6:
        majors_6.remove(element)
    elif element in majors_7:
        majors_7.remove(element)
    elif element in majors_8:
        majors_8.remove(element)
    elif element in majors_9:
        majors_9.remove(element)
    elif element in majors_10:
        majors_10.remove(element)
    elif element in majors_11:
        majors_11.remove(element)
    elif element in majors_12:
        majors_12.remove(element)
    elif element in majors_13:
        majors_13.remove(element)

#Allows input for number of readers, which determines the lists from which chapters are pulled
part_count = input("Please enter number of readers: ")

def list_making ():
    if part_count == "2":
        while len(select_list) <9: #Sets number of items to be selected
            #Selects chapters from major_3 only if all of items in major_2 have been removed
            if len(majors_2) ==0:
                #Chooses chapter, adds to new list, then removes from chapter pool
                chosen_chapter = random.choice(majors_3)
                select_list.append(chosen_chapter)
                majors_3.remove(chosen_chapter)
            else:
                chosen_chapter = random.choice(majors_2)
                select_list.append(chosen_chapter)
                majors_2.remove(chosen_chapter)

    if part_count == "3":
        while len(select_list) < 9:
            count = len(select_list)
            if count <=6:
                chosen_chapter = random.choice(majors_3)
                select_list.append(chosen_chapter)
                majors_3.remove(chosen_chapter)
                count = count+1
            elif count == 6 or count <= 7:
                chosen_chapter = random.choice(majors_4)
                select_list.append(chosen_chapter)
                majors_4.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_5)
                select_list.append(chosen_chapter)
                majors_5.remove(chosen_chapter)

    if part_count == "4":
        while len(select_list) < 9:
            count = len(select_list)
            if count <=6:
                chosen_chapter = random.choice(majors_4)
                select_list.append(chosen_chapter)
                majors_4.remove(chosen_chapter)
                count = count+1
            elif count == 6 or count <= 7:
                chosen_chapter = random.choice(majors_5)
                select_list.append(chosen_chapter)
                majors_5.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_6)
                select_list.append(chosen_chapter)
                majors_6.remove(chosen_chapter)

    if part_count == "5":
        while len(select_list) < 9:
            count = len(select_list)
            if count <=6:
                chosen_chapter = random.choice(majors_5)
                select_list.append(chosen_chapter)
                majors_5.remove(chosen_chapter)
                count = count+1
            elif count == 6 or count <= 7:
                chosen_chapter = random.choice(majors_6)
                select_list.append(chosen_chapter)
                majors_6.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_7)
                select_list.append(chosen_chapter)
                majors_7.remove(chosen_chapter)

    if part_count == "6":
        while len(select_list) < 9:
            count = len(select_list)
            if count <=6:
                chosen_chapter = random.choice(majors_6)
                select_list.append(chosen_chapter)
                majors_6.remove(chosen_chapter)
                count = count+1
            elif count == 6 or count <= 7:
                chosen_chapter = random.choice(majors_7)
                select_list.append(chosen_chapter)
                majors_7.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_8)
                select_list.append(chosen_chapter)
                majors_8.remove(chosen_chapter)

    if part_count == "7":
        while len(select_list) < 9:
            count = len(select_list)
            if count <=6:
                chosen_chapter = random.choice(majors_7)
                select_list.append(chosen_chapter)
                majors_7.remove(chosen_chapter)
                count = count+1
            elif count == 6 or count <= 7:
                chosen_chapter = random.choice(majors_8)
                select_list.append(chosen_chapter)
                majors_8.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_9)
                select_list.append(chosen_chapter)
                majors_9.remove(chosen_chapter)

    if part_count == "8":
        while len(select_list) < 9:
            count = len(select_list)
            if count <=6:
                chosen_chapter = random.choice(majors_8)
                select_list.append(chosen_chapter)
                majors_8.remove(chosen_chapter)
                count = count+1
            elif count == 6 or count <= 7:
                chosen_chapter = random.choice(majors_9)
                select_list.append(chosen_chapter)
                majors_9.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_10)
                select_list.append(chosen_chapter)
                majors_10.remove(chosen_chapter)

    if part_count == "9":
        while len(select_list) < 8:
            count = len(select_list)
            if count <=5:
                chosen_chapter = random.choice(majors_9)
                select_list.append(chosen_chapter)
                majors_9.remove(chosen_chapter)
                count = count+1
            elif count == 5 or count <= 6:
                chosen_chapter = random.choice(majors_10)
                select_list.append(chosen_chapter)
                majors_10.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_11)
                select_list.append(chosen_chapter)
                majors_11.remove(chosen_chapter)

    if part_count == "10":
        while len(select_list) < 8:
            count = len(select_list)
            if count <=5:
                chosen_chapter = random.choice(majors_10)
                select_list.append(chosen_chapter)
                majors_10.remove(chosen_chapter)
                count = count+1
            elif count == 5 or count <= 6:
                chosen_chapter = random.choice(majors_11)
                select_list.append(chosen_chapter)
                majors_11.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_12)
                select_list.append(chosen_chapter)
                majors_12.remove(chosen_chapter)

    if part_count == "11":
        while len(select_list) < 6:
            count = len(select_list)
            if count <=1:
                chosen_chapter = random.choice(majors_11)
                select_list.append(chosen_chapter)
                majors_11.remove(chosen_chapter)
                count = count+1
            elif count == 2 or count <= 5:
                chosen_chapter = random.choice(majors_12)
                select_list.append(chosen_chapter)
                majors_12.remove(chosen_chapter)
                count = count + 1
            else:
                chosen_chapter = random.choice(majors_13)
                select_list.append(chosen_chapter)
                majors_13.remove(chosen_chapter)

    if part_count == "12":
        while len(select_list) < 7:
            count = len(select_list)
            if count <=3:
                chosen_chapter = random.choice(majors_12)
                select_list.append(chosen_chapter)
                majors_12.remove(chosen_chapter)
                count = count + 1

            else:
                chosen_chapter = random.choice(majors_7)
                select_list.append(chosen_chapter)
                majors_7.remove(chosen_chapter)
                count = count + 1

    if part_count == "13":
        while len(select_list) < 3:
            count = len(select_list)
            if count <=3:
                chosen_chapter = random.choice(majors_12)
                select_list.append(chosen_chapter)
                majors_12.remove(chosen_chapter)
                count = count + 1

list_making() #Runs function to make slection list
select_list.sort() #Sorts selection list alpabetically
print(select_list)
read_count = 1 #Starts read count at 1
while read_count <=4: #Stops program after 4 reads have been completed
    read_chapter = input("Enter Read Chapter: ") #Allows entry of read chapter
    select_list.remove(read_chapter)  #Removes chapter from the current selection list
    list_making() #Reruns function to add new chapter
    select_list.sort() #Resorts list by alpabetically
    print(select_list)
    read_count = read_count+1 #Adds one to read count
