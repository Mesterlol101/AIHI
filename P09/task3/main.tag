// visit DBS website with a table of foreign currency exchange rates
https://www.dbs.com/in/treasures/rates-online/foreign-currency-foreign-exchange.page
 
// create a blank csv file with the header row containing 2 columns
dump Currency,Rate to numbers.csv
 
// extract only the main forex rates table with 6 rows of data
for row from 1 to 6
{
    // XPath is a powerful way to identify webpage UI elements
    // intro to XPath - https://builtvisible.com/seo-guide-to-xpath
 
    // form XPath element identifiers for cells in table
    read ((//*[contains(@class,"tbl-primary")]/tbody/tr)[`row`]//td)[1] to currency
    read ((//*[contains(@class,"tbl-primary")]/tbody/tr)[`row`]//td)[3] to rate
 
    // show the forex rate as it is being extracted
    echo 1 `currency` to S$`rate`
 
    // save current row of forex rate to the csv file
    // by using csv_row() function on an array of fields
    forex_rate = [currency, 'S$' + rate]
    write `csv_row(forex_rate)` to numbers.csv
}