# Universify
Welcome to Universify! A program made by Luis Jaco.

Universify is a program for viewing and adding top genre data for specific schools using the Spotify API.

This is my first full project, feedback is heavily appreciated!

# Features
- View different school genre data (top genres).
- View in-depth data for genres which can display a genres popularity for specific grades of students (for example: freshman, seniors).
- Add your top three genres to a schools data (using your Spotify account).

# Notes
* Due to the way the Spotify API works, a small project like this cannot be used without manual entry into a system which allows other Spotify users to use this program. If you are interested in using the 'adding data' portion of this program for yourself you can contact me at luisjacoo04@gmail.com
* If you would like to see an example of the 'viewing data' portion of this program you can look for the school: NEW YORK INSTITUTE OF TECHNOLOGY (state: ny, zip: 11568, id: 1966) (my school and data!).
* Where I got the list of schools: https://www.kaggle.com/datasets/yashgpt/us-college-data (thank you kaggle.) the data was heavily edited and then reformated into json by me.

# Technical Stuff!
As this is my first ever project, I feel like I should list what skills/knowledge I put to use in this project.
* Each schools genre data is stored within a single JSON file, which is both edited and read by the program.
* The Spotify API is used heavily in this program, which handles both signing in the user and gathering top song data (in the form of JSON).
* Genre score data within a school is stored in a max heap of objects which contain stats for the genre (sorted by the genre-score). The heap is upkept after every change to the genre score data.
