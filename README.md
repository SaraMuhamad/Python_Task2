# Python_Task2
 a script that can transform the JSON files to a DataFrame and commit each file to a sparete CSV file in the target directory 
Problem Descripition

In 2012, URL shortening service Bitly partnered with the US government website USA.gov to provide a feed of anonymous data gathered from users who shorten links ending with .gov or .mil.

The text file comes in JSON format and here are some keys and their description. They are only the most important ones for this task.
key 	description
a 	Denotes information about the web browser and operating system
tz 	time zone
r 	URL the user come from
u 	URL where the user headed to
t 	Timestamp when the user start using the website in UNIX format
hc 	Timestamp when user exit the website in UNIX format
cy 	City from which the request intiated
ll 	Longitude and Latitude

Required

Write a script can transform the JSON files to a DataFrame and commit each file to a sparete CSV file in the target directory and consider the following:

All CSV files must have the following columns

    web_browser

      The web browser that has requested the service

    operating_sys

      operating system that intiated this request

    from_url

      The main URL the user came from

    note:

    If the retrived URL was in a long format http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf

    make it appear in the file in a short format like this www.facebook.com

    to_url

     The same applied like `to_url`

    city

      The city from which the the request was sent

    longitude

      The longitude where the request was sent

    latitude

      The latitude where the request was sent

    time_zone

      The time zone that the city follow

    time_in

      Time when the request started

    time_out

      Time when the request is ended

NOTE :

Because that some instances of the file are incomplete, you may encouter some NaN values in your transforamtion. Make sure that the final dataframes have no NaNs at all.
Script Details

The Script itself must do the following before and after trasforamtion:

    One positional argument which is the directory path with that have the files.

    One optional argument -u. If this argument is passed will maintain the UNIX format of timpe stamp and if not passed the time stamps will be converted.

    Check if the files have any dublicates in between checksum and print a messeage that indicate that.

    Print a message after converting each file with the number of rows transformed and the path of this file

    At the end of this script print the total excution time.



