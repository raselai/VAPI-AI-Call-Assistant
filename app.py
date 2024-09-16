import streamlit as st
import requests

def send_call(customer_name, customer_number):
    url = "https://api.vapi.ai/call/phone"
    payload = {
        "phoneNumberId": "Your Phone Number ID",
        "customer": {
            "number": customer_number,
            "name": customer_name
        },
        "assistant": {
            "name": "Lisa",
            "voice": {
                "voiceId": "2zRM7PkgwBPiau2jvVXc",
                "provider": "11labs",
                "stability": 0.5,
                "similarityBoost": 0.75
            },
            "model": {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an AI customer support assistant of a company named R&B Global Consultancy. \n\n#About Company:\n\nR&B Global Consultancy is a consulting farm that helps students who want to go to abroad for study. It gives list of university(depending on the course the student want study) and colleges to choose students to pick his suitable university. \n\nAnd rest to the work like apply for university, getting scholarship and Visa everything is done by the company.\n\n#Company Address:\n\nB.K tower, Chand Mia Road, Chawk Bazar, Chittagong. \n\nIt is open for Saturday to Thursday at 10am-6pm\n\n**Instructions for AI Agent:**\n1. **Introduction**: Begin by introducing yourself and the company. Example: \"Hi, this is Lisa calling from R&B Global Consultancy, am I talking to Nazmul?\"\n2. **Purpose of Call**: Clearly state the purpose of the call early on. Example: \"I'm reaching out to see if you are interested to study abroad.\"\n3. **Use of Fillers**: Use fillers like \"uhm\", \"ah\", and \"gotcha\" to make the conversation feel more natural and less scripted.\n4. **Engage the User**: If the user seems distracted or hesitant, use phrases that refocus the conversation. Example: \"I understand it's a big decision! Just wondering, have you ever thought about it, or is it something you might consider in the future?\"\n5. **Information Gathering**: If the user expresses interest, gather basic information such as what he is doing now, Which degree he is interested to study. If the user mention any subject he is interested on, ask him wich university he wants to get the degree from. If user can't decide then go to your knowladgebase and suggest a university for his subject.\n7. **Bring the Conversation Back**: Always try to steer the conversation back to the user's potential interest in study abroad.\n8. **Friendly and Positive Tone**: Maintain a friendly and positive demeanor throughout the call to foster a comfortable and engaging conversation.\n\n**End of Call**: Ensure the call ends on a positive note, reinforcing the company's dedication to assisting the customer. Example: \"We really appreciate your time talking to us. We're here to help whenever you're ready.\" \n\n\n\n"
                    }
                ],
                "provider": "openai",
                "maxTokens": 250,
                "temperature": 0.7,
                "knowledgeBase": {
                    "topK": 2,
                    "fileIds": [
                        "58860911-4a96-4187-855e-c2fc680e33df"
                    ],
                    "provider": "canonical"
                },
                "emotionRecognitionEnabled": True
            },
            "recordingEnabled": True,
            "firstMessage": "Hello, this is Lisa from R and B Consultancy. am I talking to " + customer_name + "?",
            "voicemailMessage": "You've reached our voicemail. Please leave a message after the beep, and we'll get back to you as soon as possible.",
            "endCallMessage": "Thank you for contacting us. Have a great day!",
            "transcriber": {
                "model": "general",
                "language": "en",
                "provider": "deepgram"
            },
            "clientMessages": [
                "transcript", "hang", "function-call", "speech-update", "metadata", "conversation-update"
            ],
            "serverMessages": [
                "end-of-call-report", "status-update", "hang", "function-call"
            ],
            "endCallPhrases": [
                "goodbye"
            ]
        }
    }
    headers = {
        "Authorization": "Your Bapi API key",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text

st.title('Outbound Call Interface')

customer_name = st.text_input("Please input your name")
customer_number = st.text_input("Please input your number with prefix")

if st.button('Make Call'):
    if customer_name and customer_number:
        result = send_call(customer_name, customer_number)
        st.text_area("Response:", value=result, height=300)
    else:
        st.error("Please enter both name and number.")
