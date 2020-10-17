This is my submission for the task for the Python Backend Developer position at Smart Steel Technologies GmbH.

How to Run:
------
First of all download the necessary libraries that are found in the requirements.txt file.
Then simply run the run.py script and you're set.
The Database is already provided as a .db file in the app folder.

The app uses the port 8000, after running the script, open https://localhost:8000 on your browser.
If everything is working fine you will see the home page as such:

![ScreenShot](/snapshots/home.PNG)

How to Use:
------
There's a tab bar on top of the page (Data, Upload CSV, Logs) each tab will change the contain of the page:
  - Upload CSV:
      This page is for uploading CSV files so the app adds the data to the database
      The CSV file should have the following columns (temperature, duration, timestamp)
      
  - Logs:
      This page has a table showing the list of Logs sorted by date.
      There's also a date filter option.
      
  - Data:
      This page also has a table showing the list of temperature measures similar to the one in the Logs page.
      The rows are fetched from the database 20 as a time using pagination.
      
      Pressing a row in the table opens a module containg the data of the specific row. You can then change the data or delete the current row.
      
      ![ScreenShot](/snapshots/change-popup.PNG)
      
      Pressing the top right + button will open another module that lets you add a new row to the table.
      
      ![ScreenShot](/snapshots/add-popup.PNG)
      
      Below the table, we have a chart that plot the temperture over the timestamp. The chart is zoomable and pannable.
      
      ![ScreenShot](/snapshots/chart.PNG)
  
Technologies Used:
------
For the Backend:
  - Flask
  - SQLite 3 (Database)
  - SQLAlchemy (for Database Manipulation)
  - Pandas (for reading CSV and add to Database)

For the Frontend:
  - Bootstrap 3 (for the design)
  - JQuery
  - ChartJS (for the chart)
  - DateTimePicker/MomentJS (for the date filter)
