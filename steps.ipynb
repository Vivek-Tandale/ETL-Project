{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Seattle Airbnb ETL Project\n",
    "### Data Source\n",
    "* Kaggle: https://www.kaggle.com/airbnb/seattle\n",
    "### Data Files\n",
    "* One listings.csv file that contains Airbnb listing information and Airbnb host information\n",
    "* One calendar.csv file that contains property availability information throughout the year\n",
    "* One reviews.csv file that contains Airbnb property reviews information\n",
    "### Idea of Relational Database Schema\n",
    "* Four tables:\n",
    "    * One table for listings information from the listings.csv file\n",
    "    * One table with hosts information from the listings.csv file\n",
    "    * One table with property availability information from the calendar.csv file\n",
    "    * One table with property reviews information from the reviews.csv file\n",
    "* How the tables are linked together:\n",
    "    * Listings and hosts tables linked together by host_id\n",
    "    * Listings and property availability tables linked together by listing_id\n",
    "    * Listings and property reviews tables linked together by listing_id\n",
    "## 1. Extract\n",
    "* CSV files are taken from a Kaggle web page and saved in the \"Resources\" folder\n",
    "* Data is extracted from the four CSV files in the \"Resources\" folder\n",
    "* Python code to extract data from the CSV files is listed below:\n",
    "\n",
    "## 2. Transform \n",
    "* Separate the listing_host_df into two dataframes; One dataframe for listings information and one dataframe for hosts information:\n",
    "   * listings dataframe:\n",
    "      ~~~~python\n",
    "      listing_df = listing_host_df[[\"id\",\"listing_name\",\"street\",\"neighbourhood_cleansed\",\"neighbourhood_group_cleansed\",\"city\",\"state\",\"zipcode\",\"latitude\",\"longitude\",\"is_location_exact\",\"property_type\",\"room_type\",\"accommodates\",\"bathrooms\",\"bedrooms\",\"beds\",\"bed_type\",\"square_feet\",\"price\",\"weekly_price\",\"monthly_price\",\"security_deposit\",\"cleaning_fee\",\"guests_included\",\"extra_people\",\"minimum_nights\",\"maximum_nights\",\"has_availability\",\"availability_30\",\"availability_60\",\"availability_90\",\"availability_365\",\"number_of_reviews\",\"first_review\",\"last_review\",\"review_scores_rating\",\"review_scores_accuracy\",\"review_scores_cleanliness\",\"review_scores_checkin\",\"review_scores_communication\",\"review_scores_location\",\"review_scores_value\",\"requires_license\",\"instant_bookable\",\"cancellation_policy\",\"require_guest_profile_picture\",\"require_guest_phone_verification\",\"reviews_per_month\",\"host_id\"]]\n",
    "      ~~~~\n",
    "   * hosts dataframe\n",
    "      ~~~~python\n",
    "      host_df = listing_host_df[[\"host_id\",\"host_name\",\"host_since\",\"host_location\",\"host_response_time\",\"host_response_rate\",\"host_acceptance_rate\",\"host_is_superhost\",\"host_neighbourhood\",\"host_listings_count\",\"host_has_profile_pic\",\"host_identity_verified\"]]\n",
    "     ~~~~\n",
    "* All columns in the calendar.csv file are used in the property availability dataframe\n",
    "* Reviews dataframe:\n",
    "     ~~~~python\n",
    "   review_df = reviews_df[['review_id', \"listing_id\", \"review_date\", \"reviewer_id\", \"reviewer_name\", \"comments\"]]\n",
    "     ~~~~\n",
    "### Cleaning\n",
    "* All four dataframes are cleaned using the following commands:\n",
    "   1. \"drop_duplicates\" to remove all duplicate entries in each dataframe\n",
    "   2. \".replace\" to remove all symbols from numerical columns (e.g. $,%,',', etc.)\n",
    "      * This is because some of the dataframe columns are initially registered as strings rather than as numbers\n",
    "   3. \".replace.\" to replace \"t\" and \"f\" string entries with the booleans \"True\" and False\"\n",
    "   4. \"to_datetime\" to convert columns to datetime format that are initially registered as strings\n",
    "   5. \"to_numeric\" to convert columns to numbers that are initially registered as strings\n",
    "## 3. Load\n",
    "### SQL -- Creating the Schema\n",
    "* In MySQL, we run the \"sql_scripts.sql\" script file in order to create the schema of the Final DataBase.\n",
    "\n",
    "### Python -- Connecting to MySQL database and adding in the data\n",
    "* A MySQL database connection is created and an engine is created in Python (**if reproducing, make sure to add in the appropriate computer password**):\n",
    "* Using the 'sqlalchemy' module, we create an 'engine' object which is used to feed the data to the SQL database in the LocalHost \n",
    "* The 'engine' object is used to populate all the SQL tables"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "data",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
