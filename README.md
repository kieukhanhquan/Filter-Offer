tah# Filter-Offer
# Offers Filtering and Sorting Program

This Python program reads offer data from a JSON file, filters valid offers based on check-in date and category, sorts them by the merchant's distance, and selects the top 2 offers with different categories and the shortest distance.

## Requirements

- Python (version 3.x): [Download Python](https://www.python.org/downloads/)

## Usage

1. **Download Source Code and Data:**
   - Download the source code from the repository or copy the code to your computer.

2. **Open Command Line:**
   - Open a command line window (Command Prompt or Terminal).

3. **Navigate to the Source Code Folder:**
   - Use the `cd` command to navigate to the folder containing the Python source file.

     ```bash
     cd path_to_src_folder
     ```

4. **Run the Program:**
   - Use the following command to run the program:

     ```bash
     python FilterOffer.py <checkin_date> <path_to_input_file>
     ```
  - Or you can use exiting input.json file in src folder and change content of this file :

     ```bash
     python FilterOffer.py <checkin_date> ./input.json
     ```
     Example:

     ```bash
     python filter_ofFilterOfferfers.py 2023-12-25 ./input.json
     ```

5. **Check the Results:**
   - The results will be saved in the `output.json` file. You can check the content of this file to see the filtered and sorted offers as per your requirements.

## Notes

- Ensure you have Python installed on your computer.
- Modify the path to the data file if necessary.

