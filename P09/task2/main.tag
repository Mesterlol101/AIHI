// This flow demonstrates usage of datatables to run a flow multiple times, once per line in a csv
// IMPORTANT: run this sample with 'form_data.csv' behind,
// like 'tagui 6_datatables.tag form_data.csv'
 
// TagUI runs this flow once for each data row in 'form_data.csv',
// using the variable values in that row.
 
echo "------------------------------------------------------------"
echo "Task 2 start"
echo "------------------------------------------------------------"
 
// Visit the web page
//https://www.w3schools.com/html/html_forms.asp
//https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit
 
https://submit.pages.dev
 
// Clear the input and then type the 'firstname'/'lastname'
// from the right row in 'form_data.csv'
 
// frame iframeResult
//     click //input[@id="fname"]
//     wait 1
//     type //input[@id="fname"] as [clear]`name`
//     type //input[@id="lname"] as [clear]`age`
//     click //input[@id="lname"]/following-sibling::input[@type="submit"]
//     wait 2
 
// click //button[@id="runbtn"]
 
type //input[@id="name"] as [clear]`name`
type //input[@id="email"] as [clear]`email`
select referers as Facebook
click //button[@type="submit"]
wait 5
 
chrome.back()
 
 
 
echo "------------------------------------------------------------"
echo "Task 3 Ends"
echo "------------------------------------------------------------"