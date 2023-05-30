# MusicRecPlus
MusicRecPlus: A Python-based recommendation system for music artists. Users can enter/delete preferences. System provides artist suggestions based on user and collective preferences.


# Music Recommendation System

This project is a simple command-line application for music recommendations based on user preferences. It lets users enter their favorite artists, then makes recommendations based on other users with similar tastes. It also includes features like showing the most popular artists and the user who has liked the most artists.

## How It Works

The program begins by loading an existing database of users and their artist preferences from a file. New users can enter their favorite artists, and these preferences are stored for future sessions. Users can get recommendations for artists they may like, based on what other users with similar tastes have liked.

The system provides the following options:

- Enter preferences
- Get recommendations
- Show the most popular artists
- Display the popularity of the most popular artist
- Show the user who has liked the most artists
- Save and quit

## Functions

The program consists of several functions, including:

- `loadDB(filename)`: Loads the user database from the provided file.
- `enterPreferences(username)`: Allows users to enter their preferred artists.
- `numMatches(L1, L2)`: Returns the number of matches between two lists.
- `filterDuplicates(L1, L2)`: Returns the items in L1 that are not in L2.
- `getRecommendations(username)`: Provides music recommendations for the user.
- `getAllArtists()`: Returns all artists that people follow.
- `removeArtistDuplicates(all_artists)`: Removes duplicate artists from the list.
- `assignLikesToArtists(all_artists, all_artists_no_duplicates)`: Assigns the total likes per artist.
- `mostPopularArtist()`: Returns the top three most popular artists.
- `howPopularIsTheMostPopular()`: Returns the number of likes the most popular artist has.
- `getUserWithMostLikes()`: Returns the user with the most artist preferences.
- `saveAndQuit()`: Saves the current user database to a file.
- `mainMenu(username)`: Provides the main menu for the user to choose an option.
- `startProgram()`: Starts the program, loads the user database, and prompts the user to sign in.

## Setup & Execution

You can clone this repository to your local machine and run the Python script from the command line. You need to have Python installed on your computer to run this program.

Please follow the steps below to run the application:

1. Clone the repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Run the Python script using the command `python <filename>.py`.

## User Guide

When you run the program, you'll be prompted to enter your name. If you want your preferences to remain private, append a "$" symbol after your name.

The main menu will then appear with various options:

- `e`: Enter your favorite artists.
- `r`: Get music recommendations based on your preferences and the preferences of other users.
- `p`: See the most popular artists among all users.
- `h`: See how many likes the most popular artist has.
- `m`: See which user has liked the most artists.
- `q`: Save your preferences and quit the program.

Choose an option by entering the corresponding letter.

Remember, your preferences will be saved for future sessions!

## Dependencies

This Python application requires no special libraries or packages and should run with Python 3.x.

## Contribution

Feel free to fork this project and make your own changes. Any contributions you make are greatly appreciated.
