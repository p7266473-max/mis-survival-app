import google.generativeai as genai
import json
import logging

logger = logging.getLogger("resume_architect.engine")

def get_gemini_client(api_key: str):
    genai.configure(api_key=api_key)
    return genai

def run_research_pass(client, selected_roles, status_widget, selected_stream) -> str:
    status_widget.info("Searching the web for the best certification pathways...")
    roles_str = ", ".join(selected_roles)
    
    prompt = f"""
    Research the best free or open-source courses and certifications for a student pursuing:
    Stream: {selected_stream}
    Target Roles: {roles_str}
    
    Provide a concise summary of 3-4 top recommended certifications/courses with their platforms (e.g. Coursera, edX, Harvard CS50).
    """
    
    try:
        model = client.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Research pass failed: {e}")
        return "Failed to fetch online research. Using default academic curriculum pathways."

def run_extraction_pass(client, selected_roles, research_summary, status_widget, selected_stream, degree_placeholder) -> dict:
    status_widget.info("Synthesizing future resume profile...")
    roles_str = ", ".join(selected_roles)
    
    prompt = f"""
    You are an expert career architect. Generate a 3-year future resume for a student graduating with a {selected_stream} ({degree_placeholder}) who wants to become: {roles_str}.
    
    Incorporate these research certifications if relevant:
    {research_summary}
    
    Return the response as a valid JSON object with the following keys:
    - "Name": "Jane Doe" (or placeholder name)
    - "Location": "San Francisco, CA"
    - "Phone": "+1-555-0199"
    - "Email": "future.talent@example.com"
    - "LinkedIn": "linkedin.com/in/future-talent"
    - "Summary": "A concise executive summary of achievements in 3 years."
    - "Experience": [
        {{
          "Role": "Lead Developer / Systems Project",
          "Company": "Capstone Project / Internship",
          "Duration": "2027 - 2028",
          "Achievements": [
             "Accomplished X using Y resulting in Z metric.",
             "Developed A with B yielding C."
          ]
        }}
      ]
    - "Skills": ["Skill 1", "Skill 2", "Skill 3"]
    - "Education": [
        "{degree_placeholder}",
        "Free Certification Course 1 (Platform)",
        "Free Certification Course 2 (Platform)"
      ]
      
    Ensure the response is strictly JSON format only.
    """
    
    try:
        model = client.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
        return json.loads(response.text)
    except Exception as e:
        logger.error(f"Extraction pass failed: {e}")
        # Return structured fallback data
        return {
            "Name": "Alex Mercer",
            "Location": "New York, NY",
            "Phone": "+1-555-0143",
            "Email": "alex.mercer@academy.edu",
            "LinkedIn": "linkedin.com/in/alexmercer-future",
            "Summary": f"Aspiring professional specializing in {roles_str} with hands-on project experience.",
            "Experience": [
                {
                    "Role": f"Junior {selected_roles[0]}",
                    "Company": "Academic Capstone Project",
                    "Duration": "2027 - 2028",
                    "Achievements": [
                        "Designed and developed the core application system.",
                        "Optimized system latency by 25% through indexing."
                    ]
                }
            ],
            "Skills": [selected_roles[0], "Systems Analysis", "IT Governance"],
            "Education": [
                degree_placeholder,
                "Google IT Support Professional Certificate (Coursera)",
                "Introduction to Databases (edX)"
            ]
        }

def run_enhancement_pass(client, extracted_data: dict, status_widget) -> dict:
    status_widget.info("Enhancing vocabulary and grammar...")
    
    prompt = f"""
    You are a professional resume writer. Review and enhance the following resume data to use powerful action verbs, clear metrics, and premium professional vocabulary. Keep the structure identical.
    
    Resume Data:
    {json.dumps(extracted_data)}
    
    Return the enhanced data as a valid JSON object matching the input structure.
    """
    
    try:
        model = client.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
        return json.loads(response.text)
    except Exception as e:
        logger.error(f"Enhancement pass failed: {e}")
        return extracted_data
