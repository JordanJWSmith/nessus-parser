# Nessus Parser

This application allows users to upload .nessus files, save the contents to a SQL database and display the results. 

The home-page dashboard provides the option to upload the desired .nessus files (for example the provided example.nessus file). The upload process contains error validation to notify the user if the file extension is incompatible, the file already exists in the database or if there is a parsing error. The upload process can be summarised in three stages:
1. Parse XML file to build data structures
2. Validate all data structures against model serializers
3. Upload all data to SQL database

The structure of the Nessus XML files is understood according to the [Tenable Nessus V2 File Format documentation](https://static.tenable.com/documentation/nessus_v2_file_format.pdf)

The dashboard displays a button to view the contents of each uploaded file. Clicking this button will redirect the user to the /report page. 

The report page contains two sections to represent the 'Policy' and 'Report' sections of the file. In the Policy section, users can use the radio buttons to view a breakdown of each of the four Policy subsections:
* Server Preferences
* Plugin Preferences
* Family Selection
* Individual Plugin Selection

In the Report section, users can use the select box to choose one of the report hosts. They can then use the radio buttons to toggle between viewing the host attributes or the report items contained within that host. When viewing the breakdown of report items, users can click the 'See Detail' option on each item to view the details of that item. 


## Next Steps
* Explore more efficient upload process to decrease upload time
* Add loading graphics
