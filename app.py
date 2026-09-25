import streamlit as st
import requests

st.set_page_config(
    page_title="LegalEase AI",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ LegalEase AI")
st.write("AI-Powered Legal Document Generator")

document_type = st.text_input(
    "Document Type",
    placeholder="Example: Employment Contract"
)

parties = st.text_area(
    "Parties Involved",
    placeholder="Example: John Doe (Employee), ABC Corp (Employer)"
)

terms = st.text_area(
    "Terms & Conditions",
    placeholder="Enter terms separated by semicolons (;)"
)

dates = st.text_input(
    "Effective Date",
    placeholder="Example: 10/04/2025"
)

if st.button("Generate Document"):

    if not document_type or not parties or not terms or not dates:
        st.warning("Please fill in all fields.")

    else:
        data = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json=data
            )

            if response.status_code == 200:
                result = response.json()["document"]

                st.success("Document Generated Successfully!")

                edited_document = st.text_area(
                    "Edit Document",
                    value=result,
                    height=400
                )

                st.download_button(
                    "Download TXT",
                    data=edited_document,
                    file_name="LegalEase_Document.txt",
                    mime="text/plain"
                )

            else:
                st.error("Failed to generate document.")

        except Exception as e:
            st.error(f"Connection Error: {e}")
