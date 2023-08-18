# -*- coding: utf-8 -*-

import time
import pandas as pd
import sys

from dateutil.relativedelta import relativedelta as rd

#******FUNCTIONS**************************************************

def err_handler(err_msg):
    
    """
    Error handler for if user types an invalid city, month, or dow.

    Args:
        (str) city - error message text from wherever the error occured to let user know what was wrong
    """
    
    print("ERROR \n")
    print(err_msg)
    sys.exit() #exit program after printing the error message

def get_filters():
    
    """
    Gets inputs from users so bike share data can be loaded and filteres as user wants.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) dow - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    month = "na"
    day_of_week = "na"
    
    # user input to select the city
    city = input("Would you like to see data for Chicago, New York, or Washington? --> ").lower()
    
    avail_cities = ['chicago', 'new york', 'washington', 'nyc', 'new york city']

    # Check to see if city input is one of the 3 cities
    if avail_cities.count(city) == 0:
        err_msg = "The city you selected is not valid, please restart the program and try again"
        err_handler(err_msg)
    
    # user input for if and how to sort the data
    sort_filter = input("Would you like to filter the data by month, day, or not at all? (Type 'none' for not at all) --> ").lower()
    
    avail_filters = ['month', 'mon', 'day', 'none', 'not at all']
    
    # Check to see if sort input is one of the available options
    if avail_filters.count(sort_filter) == 0:
        err_msg = "The filter criteria you entered did not match one of the options (month, day, none), please restart the program and try again"
        err_handler(err_msg)
    
    # Lists of available options user can input for months or days
    avail_months = ['january', 'jan', '1', 'february', 'feb', '2', 'march', 'mar', '3', 'april', 'apr', '4', 'may', '5', 'june', 'jun', '6']
    avail_days = ['mon', 'monday', 'mo', 'tue', 'tuesday', 'tu', 'tues', 'wednesday', 'wed', 'we', 'thu', 'thur', 'thursday', 'th', 'friday', 'fri', 'fr', 'sat', 'saturday', 'sa', 'sun', 'sunday', 'su']
    
    # Check to see if month or day input are options, if not then make filters 'all'
    if sort_filter == 'month' or sort_filter == 'mon':
        month = input("Which month - January, February, March, April, May, or June? --> ")
        month = month.lower().lstrip('0')
        if avail_months.count(month) == 0:
            err_msg = "The month you selected is not valid, please restart the program and try again"
            err_handler(err_msg)
    elif sort_filter == 'day':
        day_of_week = input("Which day - Mon, Tue, Wed, Thu, Fri, Sat, or Sun? --> ")
        day_of_week = day_of_week.lower()
        if avail_days.count(day_of_week) == 0:
            err_msg = "The day of the week you selected is not valid, please restart the program and try again"
            err_handler(err_msg)
    else:
        month = "all"
        day_of_week = "all"
    
    return city, month, day_of_week

def load_data(city, month, dow):

    """
    Gets inputs from users so bike share data can be loaded and filteres as user wants.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) dow - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """   

    start_time = time.time()
    
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',
              'new york': 'new_york_city.csv',
              'nyc': 'new_york_city.csv' }
    
    MONTH_OPTIONS = { 'january': 'january',
              'jan': 'january',
              '1': 'january',
              'february': 'february',
              'feb': 'february',
              '2': 'february',
              'march': 'march',
              'mar': 'march',
              '3': 'march',
              'april': 'april',
              'apr': 'april',
              '4': 'april',
              'may': 'may',
              '5': 'may',
              'june': 'june',
              'jun': 'june',
              '6': 'june'}
    
    DOW_OPTIONS = { 'monday': 'mon',
              'mon': 'mon',
              'mo': 'mon',
              'tuesday': 'tue',
              'tue': 'tue',
              'tu': 'tue',
              'tues': 'tue',
              'wednesday': 'wed',
              'wed': 'wed',
              'we': 'wed',
              'thursday': 'thu',
              'thu': 'thu',
              'th': 'thu',
              'thur': 'thu',
              'friday': 'fri',
              'fri': 'fri',
              'fr': 'fri',
              'saturday': 'sat',
              'sat': 'sat',
              'sa': 'sat',
              'sunday': 'sun',
              'sun': 'sun',
              'su': 'sun'}
   
    # get month in correct format from what user types if it's in one of the listed options above
    if month != 'na' and month != 'all':
        month = MONTH_OPTIONS[month]

    # get dow in correct format from what user types if it's in one of the listed options above        
    if dow != 'na' and dow != 'all':
        dow = DOW_OPTIONS[dow]
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df = df.drop(df.iloc[:, :1], axis = 1) #drops first column of seemingly random numbers that were in downloaded file from Udacity

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['dow'] = df['Start Time'].dt.dayofweek
    
    # filter by month if applicable
    if month != 'all' and month != 'na':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if dow != 'all' and dow != "na":
        # use the index of the months list to get the corresponding int
        dows = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        dow = dows.index(dow)
        
        # filter by day of week to create the new dataframe
        df = df[df['dow'] == dow]
    
    print("\nLoading data took %s seconds." % (time.time() - start_time))
    print('*'*60)
    return df

def time_stats(df):

    """
    Prints stats about time from the filtered city data 
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """       

    start_time = time.time()
    print('\nCalculating The Most Frequent Times of Travel...\n')
        
    # find the most common month to rent bikes    
    popular_month = df['month'].mode()[0]
    print('The most common month to rent bikes is: ',popular_month)

    # find the most common day to rent bikes
    popular_day = df['dow'].mode()[0]
    print('The most common day to rent bikes is: ', popular_day)

    # find the most common start hour to rent bikes
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour of the day to start renting a bike is: ', popular_hour)

    print("\nLoading data took %s seconds." % (time.time() - start_time))
    print('*'*60)

def station_stats(df):

    """
    Prints stats about bike stations from the filtered city data 
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """       

    start_time = time.time()
    print('\nCalculating The Most Popular Stations and Trip...\n')
        
    # find the most commonly used start station
    popular_start_sta = df['Start Station'].mode()[0]
    print('The most popular station to rent a bike from is: ', popular_start_sta)

    # find the most commonly used end station
    popular_end_sta = df['End Station'].mode()[0]
    print('The most popular station to drop off a bike at is: ', popular_end_sta)

    # create new column with trip combo (start to end)
    df['start to end'] = df['Start Station'] + ' to ' + df['End Station']

    # find the most common combination of start and end station trip
    popular_combo = df['start to end'].mode()[0]
    print('The most common trip to make is from : ', popular_combo)

    print("\nLoading data took %s seconds." % (time.time() - start_time))
    print('*'*60)

def trip_duration_stats(df):
    
    """
    Prints stats about trip durection from the filtered city data 
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """   
    # formatting for the 'relativedelta' imported library for how to format the time to make it more readable
    sumfmt = '{0.days} days {0.hours} hours {0.minutes} minutes {0.seconds} seconds'
    avgfmt = '{0.minutes} minutes {0.seconds} seconds'
    
    start_time = time.time()
    print('\nCalculating Trip Duration...\n')
    
    # find the total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is: ', sumfmt.format(rd(seconds=total_time)))

    # find the average travel time
    avg_time = df['Trip Duration'].mean()
    print('The average trip length is: ', avgfmt.format(rd(seconds=avg_time)))

    print("\nLoading data took %s seconds." % (time.time() - start_time))
    print('*'*60)

def user_stats(df, city):

    """
    Prints stats about bike renter info from the filtered city data 
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """       

    start_time = time.time()
    print('\nCalculating User Stats...\n')
        
    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts by User Type: \n', user_type_count, '\n')
    
    if city != 'washington':
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('Counts by Gender: \n', gender_count, '\n')

        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('The oldest person to rent a bikes birth year is: ', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('The youngest person to rent a bikes birth year is: ', most_recent_year)
        most_common_year = df['Birth Year'].mode()[0]
        print('The people with the most common birth year to rent a bike is: ', most_common_year)

    print("\nLoading data took %s seconds." % (time.time() - start_time))
    print('*'*60)

def display_raw(city):
    
    """
    Displays raw data from the selected city with filters applied that way user can see data used for calculations
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """   
    
    CITY_DATA = { 'chicago': 'chicago.csv',
                 'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv',
                 'new york': 'new_york_city.csv',
                 'nyc': 'new_york_city.csv' }
    
    # import raw data again, this is done to have original un-filtered data (df has been changed too much at this point)
    df = pd.read_csv(CITY_DATA[city])
    df = df.drop(df.iloc[:, :1], axis = 1) #drops first column of seemingly random numbers that were in downloaded file from Udacity
    
    # User input for if they want to see raw data
    display_data = input('\nWould you like to display the raw unfiltered data used for these calculations? Enter yes or no.\n')
    if display_data.lower() != 'no':
    
        istart = 0
        # Displays the first 5 rows of raw data
        print(df.loc[istart:istart+4])
        
        istart += 5
        
        # User input for if they want to see 5 more rows of data
        restart = input('\nWould you like to see the next 5 rows of raw data? Enter yes or no.\n')
        if restart.lower() != 'no':
    
            while True:
                print(df.loc[istart:istart+4])
                istart += 5
                
                # User input for if they want to see 5 more rows of data (this one will loop until user says no)
                restart = input('\nWould you like to see the next 5 rows of raw data? Enter yes or no.\n')
                if restart.lower() == 'no' or istart > (df.index.max() - 4): # Will break loop if at the end of the raw data
                    break

def main():
    while True:
        city, month, day_of_week = get_filters()
        df = load_data(city, month, day_of_week)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        display_raw(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#*****************************************************************

global month
global day_of_week

month = "na"
day_of_week = "na"

print("Welome to the bikeshare data repository!\n")
if __name__ == "__main__":
	main()

    
