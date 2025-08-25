# XML Data Improver Tool

This Python script is designed to parse and modify an XML file with programs for CNC mashine. The main functionality includes:
* Modifying Specific Angle Values: Allows the user to update all instances of specific angle nodes (ANGL and ANGR) with new values.
* Counting Program Entries: Counts how many <BAR> elements exist in the XML file.
* Removing Duplicate Entries: Identifies and removes duplicate <BAR> elements based on their barcode value (<BCOD>), while keeping track of the number of duplicates removed.
* Updating Duplicate Counters: After removing duplicates, updates the <MLT> element within each <BAR> with the count of how many duplicates were removed for that specific barcode.
* Saving the Modified XML: Writes the updated XML content into a new file called Improved_CNCDATA.XML.

Key Features:
* Uses the lxml library for efficient XML parsing and manipulation.
* Maintains data integrity by ensuring only duplicates are removed and counters are properly updated.
* Provides clear console output of the number of program entries before and after deduplication.
Usage:
* For the first time, open a terminal and navigate to the project folder and execute command "pip install -r requirements.txt"
* Place your input XML file (e.g., CNCDATA.XML) in the same directory as the script.
* Run the script using Python 3.
* The improved XML will be saved as Improved_CNCDATA.XML.

