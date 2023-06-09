# Deploying An App to Health Universe

**Welcome to the [Health Universe](https://www.healthuniverse.com) community!**

Health Universe is an open-source cloud deployment platform and community for machine learning (ML) and AI from science to medicine.
This tutorial will guide you through packaging a Python model into [FastAPI](https://fastapi.tiangolo.com) and [Streamlit](https://streamlit.io) apps for deploying to Health Universe.

## Prerequisites

- Python Model.
- Familiarity with FastAPI and Streamlit.
- [GitHub](https://github.com/) Account.

## Step 1: Set Up Repo

1. Create a new GitHub repo to host your project.
2. Clone the repo to your local machine.

## Step 2: Package App

In your local repo, create the following files:

- ```model.py```: Python Model.
- ```main.py```: FastAPI App.
- ```app.py```: Streamlit App.
- ```requirements.txt```: Project Dependencies.

For this deploy tutorial, I created a clinical calculator to determine CHA₂DS₂-VASc score for atrial fibrillation stroke risk.

## Step 3: Deploy to Health Universe

1. Push local repo to GitHub.
2. Go to https://www.healthuniverse.com.
3. Log in or create an account.
4. Click **Deploy App**.
5. Fill out fields.    
6. Press **Deploy**. This process may take a few minutes.

Congratulations! Once you've completed these steps, your Python model should be available as a FastAPI or Streamlit app on Health Universe!