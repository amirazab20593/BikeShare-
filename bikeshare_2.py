import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wedensday', 'thursday', 'friday', ' saturday']

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
        city = input('Would you like to see data for Chicago, New York City, or Washington ?\n').lower()
        if city in cities:
            break

    filtering = input('Would you like to filter data by month, day, both, or not at all ? Type \"none for no time filter .\n')
    if filtering == 'month':
        month = input('Which month? January, February, March, April, May, or June? \n')
        day = 'all'

    elif filtering == 'day':
        day = input('Which day? Saturday, Sunday, Monday, Tuesday, Wedensday, Thursday, Friday? \n')
        month ='all'
    elif filtering == 'both':
        month = input('Which month? January, February, March, April, May, or June? \n').lower()
        day = input('Which day? Saturday, Sunday, Monday, Tuesday, Wedensday, Thursday, Friday? \n').lower()
    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts()
    max_ind = most_common_month.index.max()
    max_val = most_common_month.values.max()
    print('Most common Month is : {},  Count : {} '.format(max_ind,max_val))

    # display the most common day of week
    most_common_day = df['day'].value_counts()
    max_ind_day = most_common_day.index.max()
    max_val_day = most_common_day.values.max()
    print('Most common Month is : {},  Count : {} '.format(max_ind_day,max_val_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].value_counts()
    max_ind_hour = df['hour'].mode()[0]
    max_val_hour = most_common_hour.values.max()
    print('Most common Start Hour is : {},  Count : {} '.format(max_ind_hour,max_val_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].value_counts()
    max_ind_station = most_start_station.idxmax()
    max_val_station = most_start_station.values.max()
    print('Most used Start station : {} , Count : {}'.format(max_ind_station,max_val_station))


    # display most commonly used end station
    most_end_station = df['End Station'].value_counts()
    max_ind_endstation = most_end_station.idxmax()
    max_val_endstation = most_end_station.values.max()
    print('Most used End station : {} , Count : {}'.format(max_ind_endstation,max_val_endstation))



    # display most frequent combination of start station and end station trip
    most_frequent_comb = df[['Start Station','End Station']].mode().loc[0]
    print('Most frequent combination of start station and end station trip : ',most_frequent_comb[0], most_frequent_comb[1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is : {}'.format(total_travel_time))


    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time is : {}'.format(avg_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    for i , user in enumerate(user_type):
        print('{} : {}'.format(user_type.index[i],user))


    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        for num , genders in enumerate(gender):
            print('{} : {}'.format(gender.index[num],genders))
    else:
        print('Gender stats can not be calculated because gender does not appear in the DataFrame')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        year_of_birth = df['Birth Year']
        earliest_year_of_birth = year_of_birth.min()
        print('Earliest year of birth : ',earliest_year_of_birth)

        mostrecent_year_of_birth = year_of_birth.max()
        print('Most recent year of birth : ',mostrecent_year_of_birth)

        most_common_year = year_of_birth.value_counts().idxmax()
        print('Most Common year of birth : ', most_common_year)
    else:
        print('Birth Year stats can not be calculated because birth year does not appear in the DataFrame')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?').lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue? ").lower()
        if view_display == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
