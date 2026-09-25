import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

genai.configure(api_key=API_KEY)


class GeminiDocumentGenerator:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        dates
    ):
        prompt = f"""
You are a legal document generation assistant.

Create a professional and well-structured legal document.

Document Type:
{document_type}

Parties Involved:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{dates}

Requirements:
1. Give the document a clear title.
2. Include the parties involved.
3. Include the effective date.
4. Organize the document into clear sections.
5. Include the provided terms and conditions.
6. Use professional and formal language.
7. Do not invent important personal information.
8. Format the output so it can be easily converted
   into TXT, DOCX, or PDF.

Generate only the document content.
"""

        response = self.model.generate_content(prompt)

        return response.text
