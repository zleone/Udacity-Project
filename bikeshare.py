import time
import calendar
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
    print('Hello! Let\'s explore US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\nPlease input one of the following cities you would like to learn about: chicago, new york city, or washington.\n").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("No information is available for any cities other than: chicago, new york city, or washington. Please select one of these three cities.")
            continue
        else:
            break


    # get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nInput the month you would like to explore: january, february, march, april, may, june, or input 'all' if you would like to access each month's data at once.\n").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Unfortunately, there is no information available for any other month than those listed above. Please select from one of the given options.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nInput the day you would like specifically look into: monday, tuesday, wednesday, thursday, friday, saturday, sunday, or input 'all' if you would like to access each day's data at once.\n").lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("That input is invalid, please select from one of the options given above.")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_popular_month = df['month'].mode()[0]
    print('The most popular month to travel is {}.'.format(calendar.month_name[most_popular_month]))


    # TO DO: display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day of the week is {}.'.format(most_popular_day))

    # TO DO: display the most common start hour
    most_popular_hour = df['hour'].mode()[0]
    print('\nThe most popular start hour is {}.'.format(most_popular_hour))


    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is {}.'.format(most_popular_start_station))

    # TO DO: display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]
    print('\nThe most popular end station is {}.'.format(most_popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_popular_trip = df[['Start Station', 'End Station']].mode().loc[0]
    print('\nThe most popular trip starts at {}, and ends at {}.'.format(most_popular_trip[0],most_popular_trip[1]))


    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_in_seconds = df['Trip Duration'].sum()
    total_travel_time_in_minutes = int((total_travel_time_in_seconds/60))
    print('The total travel time is {} minutes.\n'.format(total_travel_time_in_minutes))

    # TO DO: display mean travel time
    total_mean_travel_time_in_seconds = df['Trip Duration'].mean()
    total_mean_travel_time_in_minutes = int((total_mean_travel_time_in_seconds/60))
    print('The total mean travel time is {} minutes.'.format(total_mean_travel_time_in_minutes))

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('\nUser Data:\n')
    print('The various user types consist of:\n\n{}'.format(user_type_count))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_of_user_count = df['Gender'].value_counts()
        print('\n\nGender Data:')
        print('\nThe gender counts of the users are:\n\n{}'.format(gender_of_user_count))
    else:
        print('\n\nGender Data:')
        print('\nSorry, there is no gender information availble for this particular request at this time. Try another!')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('\n\nBirth Year Data:')
        print('\n{} is the earliest birth year.'.format(earliest_birth_year))
        print('{} is the most recent birth year.'.format(most_recent_birth_year))
        print('{} is the most common birth year.'.format(most_common_birth_year))
    else:
        print('\n\nBirth Year Data:\n')
        print('Unfortunately, there is no birth year data available for this request. Please try another!')

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    display_data = input('\nDo you want to see the raw data? Enter yes or no.\n').lower()
    if display_data == ('yes'):
        index = 0
        while True:
            print(df.iloc[index:index + 5])
            index += 5

            display_more_data = input('\nDo you want to see 5 more lines of raw data? Enter yes or no.\n').lower()
            if display_more_data != ('yes'):
                print('\nThank you for exploring the data!')
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
