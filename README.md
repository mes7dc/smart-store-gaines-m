# smart-store-gainesm
Before Starting

Open your project repository in VS Code.

Pull Changes

Run the following command from the project root directory. The command works in PowerShell, bash, zsh, Git Bash, and more.

git pull origin main

Activate

Run the following command from the project root directory. The command works in PowerShell.
.venv\Scripts\activate

Confirm activation by checking that the terminal shows the environment name (e.g., (venv)).
Git add-commit-push

Using a terminal in VS Code (PowerShell, zsh, or bash).

IMPORTANT: Replace the commit message with a clear and descriptive note about what you added or changed. Wrap the commit message in double quotes.

git add .

git commit -m "Add .gitignore and requirements.txt files"

git push -u origin main

Important

Always pull the latest changes before starting to avoid merge conflicts.
Test your project to ensure it works as expected before using git add-commit-push.
Make frequent commits when enhancing a project.

Commands to Manage Virtual Environment

py -m venv .venv

.\.venv\Scripts\activate

py -m pip install --upgrade pip setuptools wheel

py -m pip install --upgrade -r requirements.txt

Commands to Run Python Scripts
	Remember to activate your .venv before running files. Verify that all external packages imported into a file are included in requirements.txt (and have NOT been commented out).

py demo_script.py

py do_stats.py

py draw_chart.py

py greet_user.py


Commands to Git add-commit-push

git add .

git commit -m "custom message"

git push -u origin main


Run test script
Run the script with the command that works for your terminal. 
Either
py tests\test_data_scrubber.py
Or
python3 tests\test_data_scrubber.py
 

Pass All Tests
Keep editing the DataScrubber class and running the test script until tests run successfully without error.  You do NOT need to modify the test script at all for this exercise. Later, if you add functionality to your DataScrubber class, you may want to add additional tests as well. 

Use Your Data Scrubber 
Now that we've verified all these handy methods, you can create or update your data_prep.py script that cleans and prepares the data so it's ready for central storage (in a data warehouse or other store)..

Create or Edit Your Main Data Prep script(s)
In your main data preparation script (e.g., scripts\data-prep.py) - or scripts. There can be a LOT of work in cleaning, you might want to create and maintain one data_prep file for each of the raw tables, for example you might have either all in one:

scripts/data_prep.py 
Or several files:

scripts/data_prep_cutomers.py
scripts/data_prep_products.py
scripts/data_prep_sales.py
Use whatever works best for you. 

This project example helps illustrate a data-cleaning process that is somewhat standardized and reusable, facilitating efficient data preparation across multiple datasets and BI projects.

