# Day 23 - Virtual Environments & pip
#
# This day also didn't involve writing new application code - it was
# about setting up my Python environment properly.
#
# What I did:
# - Created a virtual environment inside my project folder:
#       python -m venv venv
# - Hit a Windows permissions error when activating it, fixed with:
#       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# - Activated the virtual environment:
#       venv\Scripts\Activate
#   (confirmed by seeing "(venv)" appear at the start of my terminal prompt)
# - Installed my first external package:
#       pip install requests
# - Saved my installed packages to a file for future reference:
#       pip freeze > requirements.txt
#
# Why this matters:
# - Virtual environments keep each project's packages isolated
# - This setup was required before I could use the "requests" library
#   in Day 24's API task