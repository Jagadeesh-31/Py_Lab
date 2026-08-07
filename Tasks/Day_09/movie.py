from datetime import date, datetime, timedelta


def movie_booking():
    telugu_action = ["Pushpa 2", "OG", "Salaar"]
    telugu_comedy = ["MAD", "Jathi Ratnalu", "F2"]
    telugu_horror = ["Virupaksha", "Masooda", "Kanchana"]
    telugu_romance = ["Hi Nanna", "Sita Ramam", "Geetha Govindam"]

    hindi_action = ["War", "Pathaan", "Jawan"]
    hindi_comedy = ["3 Idiots", "Bhool Bhulaiyaa 2", "Golmaal"]
    hindi_horror = ["Stree", "Shaitaan", "Bhoot"]
    hindi_romance = ["Aashiqui 2", "Yeh Jawaani Hai Deewani", "Rockstar"]

    english_action = ["Avengers", "John Wick", "Mission Impossible"]
    english_comedy = ["The Mask", "Home Alone", "Free Guy"]
    english_horror = ["The Nun", "Conjuring", "Insidious"]
    english_romance = ["Titanic", "The Notebook", "Me Before You"]

    timings = {
        1: "10:00 AM",
        2: "1:30 PM",
        3: "4:30 PM",
        4: "7:30 PM",
        5: "10:00 PM"
    }

    print("=" * 40)
    print("      Welcome to MovieMate AI")
    print("=" * 40)

    name = input("Enter your name: ")

    languages = {1: "Telugu", 2: "Hindi", 3: "English"}
    print("\nChoose Language")
    for key, value in languages.items():
        print(key, ".", value)
    lang = int(input("Enter choice: "))

    genres = {1: "Action", 2: "Comedy", 3: "Horror", 4: "Romance"}
    print("\nChoose Genre")
    for key, value in genres.items():
        print(key, ".", value)
    genre = int(input("Enter choice: "))

    if lang == 1:
        if genre == 1:
            movies = telugu_action
        elif genre == 2:
            movies = telugu_comedy
        elif genre == 3:
            movies = telugu_horror
        elif genre == 4:
            movies = telugu_romance
        else:
            print("Invalid Genre")
            return
    elif lang == 2:
        if genre == 1:
            movies = hindi_action
        elif genre == 2:
            movies = hindi_comedy
        elif genre == 3:
            movies = hindi_horror
        elif genre == 4:
            movies = hindi_romance
        else:
            print("Invalid Genre")
            return
    elif lang == 3:
        if genre == 1:
            movies = english_action
        elif genre == 2:
            movies = english_comedy
        elif genre == 3:
            movies = english_horror
        elif genre == 4:
            movies = english_romance
        else:
            print("Invalid Genre")
            return
    else:
        print("Invalid Language")
        return

    print("\nAvailable Movies")
    for i in range(len(movies)):
        print(i + 1, ".", movies[i])

    movie = input("\nEnter movie name: ")
    if movie not in movies:
        print("\nSorry, this movie is not available for online booking.")
        print("Please visit the theater directly to buy a ticket.")
        return

    # ---- NEW: choose show day ----
    show_days = {
        1: "Today",
        2: "Tomorrow",
        3: "Day After Tomorrow",
        4: "Within a Week (choose your day)"
    }
    print("\nChoose Show Day")
    for key, value in show_days.items():
        print(key, ".", value)
    show_day = int(input("Enter choice: "))

    booking_datetime = datetime.now()  # exact date and time the booking is made

    if show_day == 1:
        show_date = date.today()
    elif show_day == 2:
        show_date = date.today() + timedelta(days=1)
    elif show_day == 3:
        show_date = date.today() + timedelta(days=2)
    elif show_day == 4:
        days = int(input("Enter number of days from today (0-7): "))
        if 0 <= days <= 7:
            show_date = date.today() + timedelta(days=days)
        else:
            print("Booking allowed only within the next 7 days.")
            return
    else:
        print("Invalid Show Day")
        return
    # -------------------------------

    # ---- NEW: choose show timing ----
    print("\nAvailable Show Timings")
    for key, value in timings.items():
        print(key, ".", value)

    time_choice = int(input("Enter timing choice: "))
    if time_choice not in timings:
        print("Invalid Timing")
        return

    show_time = timings[time_choice]
    # -------------------------------

    print("\nBooking Confirmed!")
    print("-" * 35)
    print("Customer     :", name)
    print("Movie        :", movie)
    print("Show Time    :", show_time)
    print("Booking Date :", booking_datetime.strftime("%d-%b-%Y %I:%M %p"))
    print("Show Date    :", show_date.strftime("%d-%b-%Y"), "|", show_time)
    print("-" * 35)
    print("Enjoy your movie!")


movie_booking()
