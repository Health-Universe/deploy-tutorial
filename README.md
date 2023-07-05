# Deploying An App to Health Universe

[Health Universe](https://www.healthuniverse.com) is an open-source cloud deployment platform for ML/AI from science to medicine.
This tutorial will guide you through packaging a Python model into FastAPI and Streamlit apps for deploying to Health Universe.

## Prerequisites

- Python Model.
- Familiarity with FastAPI and Streamlit.
- [GitHub](https://github.com/) Account.

## Step 1: Set up repo

1. Create a new GitHub repo to host your project.
2. Clone the repo to your local machine.

## Step 2: Package app

In your local repo, create the following files:

- ```model.py```: Python Model.
- ```main.py```: FastAPI App.
- ```app.py```: Streamlit App.
- ```requirements.txt```: Project Dependencies.

In this repo, I created a clinical calculator to determine CHA₂DS₂-VASc score for atrial fibrillation stroke risk.

## Step 3: Deploy to Health Universe

1. Push local repo to GitHub.
2. Go to [https://www.healthuniverse.com](https://www.healthuniverse.com) and navigate to "APPS".
3. Click "Add App".
4. Log in or create an account.
5. Fill out the fields.    
6. Press "Add App" to deploy. This process may take a few minutes.

Congratulations! Once you've completed these steps, your Python model should be available as a FastAPI or Streamlit app on Health Universe!