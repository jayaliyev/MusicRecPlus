import os
USER_DB = {}

def loadDB(filename):
    '''
        Loads the musicrecplus.txt file into a dictionary
    '''
    if filename not in os.listdir():
        with open(filename, "w") as file_out:
            file_out.write("")
            return {}

    file = open(filename, "r")
    user_dict = {}
    for line in file:
        if not line.strip():
            continue

        [username, artists] = line.strip().split(":")
        artist_list = artists.split(",")
        artist_list.sort()
        user_dict[username] = artist_list

    file.close()
    return user_dict

def delete_Preferences(username):
    preference_list = USER_DB[username]
    for i in range(len(preference_list)):
        artist_name = preference_list[i]
        print(i + 1, artist_name)

    user_input = input("Select the corresponding number for your preference to be deleted: \n")
    if not user_input.isdigit() or int(user_input) <= 0 or int(user_input) - 1 >= len(preference_list):
        print("Error: Invalid input.")
        return

    artist_index = int(user_input) - 1

    preference_list.pop(artist_index)
    USER_DB[username] = preference_list


def enterPreferences(username):
    '''
        Entering user preferences function
    '''
    preferences = []

    if username not in USER_DB:
        USER_DB[username] = []

    while True:
        new = input("Enter an artist that you like ( Enter to finish ):")
        if new != "":
            artist = new.title()
            if artist not in USER_DB[username]:
                preferences.append(artist)
        else:
            break

    if username in USER_DB:
        current_preferences = USER_DB[username]
        new_preferences = current_preferences + preferences
        USER_DB[username] = sorted(new_preferences)
    else:
        USER_DB[username] = preferences

    return

def numMatches(L1, L2):
    '''
        Returns number of matches between two lists
    '''
    total = 0
    for i in L1:
        for j in L2:
            if i == j:
                total += 1
    return total

def filterDuplicates(L1, L2):
    '''
        Returns the items in L1 that are not in L2
    '''
    new_lst = []
    for i in L1:
        if i not in L2:
            new_lst.append(i)
    return new_lst

def getRecommendations(username):
    '''
        Getting recommendations for user based on their preferences
    '''
    if len(USER_DB) == 1:
        print("There isn't enough user preferences in the database.")
        return True

    top_user = ""
    top_matches = 0

    for user in USER_DB:
        if user != username and user[-1] != "$":
            num_matches = numMatches(USER_DB[user], USER_DB[username])
            if num_matches > top_matches:
                top_matches = num_matches
                top_user = user

    if top_user == "":
        print("No recommendations available at this time.")
    else:
        recommendations = filterDuplicates(USER_DB[top_user], USER_DB[username])
        for rec in recommendations:
            print(rec)

    return False

def getAllArtists():
    '''
        Returns all artists that people follow
    '''
    all_artists = []
    for key in USER_DB:
        if key[-1] == "$":
            continue
        else:
            user_artists = USER_DB[key]
            for artist in user_artists:
                all_artists.append(artist)
    return all_artists

def removeArtistDuplicates(all_artists):
    '''
        Removes duplicates from all arists
    '''
    all_artists_no_duplicates = []
    for artist in all_artists:
        if artist in all_artists_no_duplicates:
            continue
        else:
            all_artists_no_duplicates.append(artist)
    return  all_artists_no_duplicates

def assignLikesToArtists(all_artists, all_artists_no_duplicates):
    '''
        Assigns total likes per artist
    '''
    artist_count = {}
    for artist in all_artists_no_duplicates:
        artist_count[artist] = all_artists.count(artist)
    return artist_count



def mostPopularArtist():
    '''
     	getting top 3 most popular artists
    '''

    # ----- Putting all public user's artists into one list -----#
    all_artists = getAllArtists()

    #----- Checks if there are any artists found -----#
    if all_artists == []:
        print("Sorry, no artists found.")
        return

    #----- Creates a list of artist with no duplicates -----#
    all_artists_no_duplicates = removeArtistDuplicates(all_artists)

    #----- Prints all artists if there are less than 3 artists in the DB -----#
    if len(all_artists_no_duplicates) < 3:
        for artist in all_artists_no_duplicates:
            print(artist)
        return

    #----- Creates a dictionary with artists as keys and values as how many times they appear -----#
    artist_count = assignLikesToArtists(all_artists, all_artists_no_duplicates)

    #----- Sorted keys based on values from greatest to lowest -----#
    artists_sorted = sorted(artist_count, key = artist_count.get, reverse=True)

    #----- Getting the top 3 artists -----#
    top_3_artists = [artists_sorted[0]]
    max_likes = artist_count[artists_sorted[0]]
    for artist in artists_sorted:
        if len(top_3_artists) >= 3:
            break
        likes = artist_count[artist]
        if likes < max_likes:
            top_3_artists.append(artist)
            max_likes = likes

    for artist in top_3_artists:
        print(artist)

    return


def howPopularIsTheMostPopular():
    '''
        Returns how many likes does not most popular artist has
    '''

    # ----- Putting all public user's artists into one list -----#
    all_artists = getAllArtists()

    # ----- Checks if there are any artists found -----#
    if all_artists == []:
        print("Sorry, no artists found.")
        return

    # ----- Creates a list of artist with no duplicates -----#
    all_artists_no_duplicates = removeArtistDuplicates(all_artists)

    # ----- Creates a dictionary with artists as keys and values as how many times they appear -----#
    artist_count = assignLikesToArtists(all_artists, all_artists_no_duplicates)

    # ----- Sorted keys based on values from greatest to lowest -----#
    artists_sorted = sorted(artist_count, key=artist_count.get, reverse=True)

    print(artist_count[artists_sorted[0]])

def getUserWithMostLikes():
    """
        Returns user with the most artist preferences
    """

    sort_orders = sorted(USER_DB.items(), key=lambda x: len(x[1]), reverse=True)

    without_private = list(filter(lambda x: "$" not in x[0], sort_orders))

    if without_private == []:
        print("Sorry , no user found.")
    else:
        print(without_private[0][0])


def saveAndQuit():
    """
        Saves the current user db to a file
    """

    with open("musicrecplus.txt", "w+") as f:
        for k, music_names in USER_DB.items():
            arr_music_names = ",".join(music_names)
            f.write(f"{k}:{arr_music_names}" + "\n")


def show_Preferences(username):
    for i in USER_DB[username]:
        print(i)

def mainMenu(username):
    '''
        Main Menu - on loop until quit
    '''
    while True:
        response = input("Enter a letter to choose an option: \n e - Enter preferences \n r - Get recommendations \n s - Show current user's preferences \n "
                         "p - Show most popular artists \n h - How popular is the most popular \n m - Which user has the most likes \n d - Delete Preferences \n q - Save and quit \n")
        is_cold_start = False
        if response == "e":
            enterPreferences(username)
        elif response == "r":
            is_cold_start = getRecommendations(username)
        elif response == "s":
            show_Preferences(username)
        elif response == "p":
            mostPopularArtist()
        elif response == "h":
            howPopularIsTheMostPopular()
        elif response == "m":
            getUserWithMostLikes()
        elif response == "d":
            delete_Preferences(username)
        elif response == "q":
            saveAndQuit()
            break
        else:
            continue

        if is_cold_start:
            continue

def startProgram():
    '''
        Program start - loads in User DB from file and signs in user
    '''
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private) ")
    if username in USER_DB:
        mainMenu(username)
    else:
        enterPreferences(username)
        mainMenu(username)


USER_DB = loadDB("musicrecplus.txt")
startProgram()
