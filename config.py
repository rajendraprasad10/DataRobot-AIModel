from dotenv import load_dotenv
import os

load_dotenv()

DEPLOYMENT_ID=os.getenv("DEPLOYMENT_ID")

API_KEY=os.getenv("API_KEY")

DR_URL=f"https://app.datarobot.com/api/v2/deployments/{DEPLOYMENT_ID}/predictions"




print("DEPLOYMENT", DEPLOYMENT_ID, "API_KEY", API_KEY, "DR_URL", DR_URL)