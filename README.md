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



