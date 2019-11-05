import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("please enter city name of these(chicago, new york city, washington)").lower()
        if city in CITY_DATA:
            break 
        else:
            print("sorry,the value you enterd is incorrect")


    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input ("please enter the month you wanted to filter with from these(all,january, february, march, april, may, june)").lower()
        if month in months:
            break 
        elif month=="all":
            break
        else:
            print("sorry,the value you enterd is incorrect")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    while True:
        day = input ("please enter the day you wanted to filter with from these(all,monday,tuesday,wednesday,thursday,friday,saturday,sunday)").lower()
        if day in days:
            break 
        elif day=="all":
            break
        else:
            print("sorry,the value you enterd is incorrect")

    print('-'*40)
    return city, month, day
# This will display 5 rows
def display(df):
    index = 0
    while True :
        if index +5 >= len(df):
            print("end of rows") 
            break           
        print(df.iloc[index:index+5])
        index+=5
        answer = " "
        while True:
            answer=input ("Do you want to display another 5 rows?(yes/no)").lower()
            if answer == "yes" or  answer == "no" :
                break
            else :
                print("sorry wrong answer, try again")   
        if answer == "no" : 
            break
        else :
            continue
# This is refactoring branch      
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = [i+1 for i in range(len(months)) if months[i] == month] 

        # filter by month to create the new dataframe
        df = df[df["month"]==month[0]]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df["day_of_week"]==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df["month"].value_counts().idxmax()
    print("the most common month is "+ str(most_common_month) )


    # display the most common day of week
    most_common_dayofweek = df["day_of_week"].value_counts().idxmax()
    print("the most common day of week is "+str( most_common_dayofweek))


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax() 
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df["Start Station"].value_counts().idxmax()
    print("the most common start station is "+str( most_common_start))


    # display most commonly used End Station
    most_common_end = df["End Station"].value_counts().idxmax()
    print("the most common end station is "+ str(most_common_end))


    # display most frequent combination of start station and end station trip
    combination =df["Start Station"]+" & "+df["End Station"]
    most_common_combination = combination.value_counts().idxmax()
    print("the most frequent combination of start station and end station trip are "+ str(most_common_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("the total travel time = "+str(total_travel_time))


    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("the average travel time = "+str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("count of user types are :")
    print(user_types)
    
    if set(['Gender','Birth Year']).issubset(df.columns):
        # Display counts of gender
        gender = df["Gender"].value_counts()
        print("count of Gender are :")
        print(gender)
        # Display earliest, most recent, and most common year of birth
        earliest = df["Birth Year"].min()
        recent = df["Birth Year"].max()
        most_common_year = df["Birth Year"].value_counts().idxmax()
        print("The earliest year of birth is "+ str(earliest))
        print("The most recent year of birth is "+ str(recent))
        print("The most common year of birth is "+ str(most_common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
