import os
from google import genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()

def summarize_email(email_text: str) -> str:
    """Uses Google Gemini to analyze and summarize email content."""
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = f"""
    You are an intelligent email summarizer. Analyze the email below and extract:
    1. Key Summary (2-3 sentences max)
    2. Action Items (Bullet points of actions required, including deadlines/names if mentioned)
    
    Email Content:
    ---
    {email_text}
    ---
    """
    
    response = client.interactions.create(
        model="gemini-2.5-flash",
        input=prompt
    )
    return response.output_text

if __name__ == "__main__":
    sample_email = """
    Hi Team,
    
    Following up on our Q3 roadmap meeting today. We agreed that Sarah will finalize 
    the API architecture documentation by this Friday, October 2nd. 
    Alex needs to complete the database migration script by next Tuesday, October 6th.
    
    Please review the attached project board and add your estimates by EOD tomorrow.
    Our next sync is on Monday at 10 AM EST.
    
    Best,
    David
    """
    
    print("--- Processing Email ---")
    summary = summarize_email(sample_email)
    print(summary)
