import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# lists are used in diffent functions to print city, month or day in the terminal
city_list = ["chicago", "new york city", "washington"]
month_list = ["january", "february", "march", "april", "may", "june", "all"]
day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

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
        city = input('Please enter the city you want to explore (chicago, new york city, washington): ').lower()
        if city in city_list:
            break
        else:
            print('Please enter a correct option')
       
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter the month you want to explore (all, january, february, ... , june): ').lower()
        if month in month_list:
            break
        else:
            print('Please enter a correct option')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter the day of week you want to explore (all, monday, tuesday, ... , sunday): ').lower()
        if day in day_list:
            break
        else:
            print('Please enter a correct option')

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
    #read data from correct .csv file
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #add columns for month, day_of_week, hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_count = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month_count]
        
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print("Below you can find the statistics for your selection:\n-City:\t{}\n-Month:\t{}\n-Day:\t{}".format(city.title(), month.title(), day.title())) 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    
    #display the most common month
    most_common_month = month_list[df['month'].mode()[0]-1]
    print("The most common month:\t",most_common_month.title())
    
    #display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day:\t",most_common_day)
    
    #display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour:\t",most_common_hour)
    
    # print calculation time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station:\t\t\t", most_common_start_station)
    
    #display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station:\t\t\t\t", most_common_end_station)
    
    #display most frequent combination of start station and end station trip
    most_common_start_end_station = ("Start: " + df['Start Station'] + ", End: " + df['End Station']).mode()[0]
    print("The most frequent combination of start and end station:\t", most_common_start_end_station)
    

    # print calculation time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_days = total_travel_time//(60*60*24)
    remaining_sec = total_travel_time%(60*60*24)
    total_travel_time_hours = remaining_sec//(60*60)
    remaining_sec = remaining_sec%(60*60)
    total_travel_time_minutes = remaining_sec//60
    total_travel_time_seconds = remaining_sec%60
    
    print("The total travel time: \tdays: {} hours: {} minutes: {} seconds: {}".format(total_travel_time_days, total_travel_time_hours, total_travel_time_minutes, total_travel_time_seconds))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_days = mean_travel_time//(60*60*24)
    remaining_sec = mean_travel_time%(60*60*24)
    mean_travel_time_hours = remaining_sec//(60*60)
    remaining_sec = remaining_sec%(60*60)
    mean_travel_time_minutes = remaining_sec//60
    mean_travel_time_seconds = remaining_sec%60
    print("The mean travel time: \tdays: {} hours: {} minutes: {} seconds: {}".format(int(mean_travel_time_days), int(mean_travel_time_hours), int(mean_travel_time_minutes), int(mean_travel_time_seconds)))
    
    # print calculation time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print("User Types in the data set:\n")
    if 'User Type' in df:
        user_types = df['User Type'].value_counts()
        for index in user_types.index:
            if user_types[index] == 1:
                print("The type {} is {}-time in the data set:".format(index, user_types[index]))
            else:
                print("The type {} is {}-times in the data set:".format(index, user_types[index]))
    else:
        print("The are no data about the user type in the data set")
    print("\n")
    
    
    #Display counts of gender
    print("Genders in the data set:\n")
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()
        for index in gender_types.index:
            print("There are {} {} customers in the data set:".format(index, gender_types[index]))
        
    else:
        print("There are no gender data in the data set")
    print("\n")
        
    #Display earliest, most recent, and most common year of birth
    print("Birth years of customers in the data set:\n")
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()) 
        print("The earliest birth year is: {}, the most recent birth year is: {}, the most common birth year is: {}".format(earliest_year, recent_year, common_year))
    else:
        print("There are no birth dates in the data set")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # print raw data
        indexlen = len(df.index)
        rawdata = input('\nWould you like to see raw data for your selected filters? Enter yes or no.\n')
        count=0;
        if rawdata.lower() == 'yes':
            # if there are enough rows in the data set, display the first 5 rows, otherwise only 1 row
            if indexlen >= 5:
                print(df.iloc[0:4])
            else:
                print('less than 5 rows in your data set, i will only print the first row.\n')
                print(df.iloc[0])
              
            count +=5
            print(count)
            print(indexlen)
            print((count+5) <= indexlen)
            # as long as there are 5 more rows in the data set, offer the user to display the next 5 rows
            while (count+5) <= indexlen:
                rawdata = input('\nWould you like to see more raw data for your selected filters? Enter yes or no.\n')
                if (rawdata.lower() == 'yes'):
                    print(df.iloc[count:count+5])
                    count += 5    
                else:
                    break
                
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
