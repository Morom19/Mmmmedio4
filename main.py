import google.generativeai as genai

# Configure your Gemini API key
API_KEY = "AIzaSyAR1W8my5ETltKpwwZrld0zxF53VNYRsVo"
genai.configure(api_key=API_KEY)

def main():
    print("Chatbot initialized! Start your conversation below. Type an empty string to exit.\n")
    
    # Initialize the generative model
    model = genai.GenerativeModel('gemini-pro')  # Use the correct model name

    # Start a conversation
    chat = model.start_chat()

    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Break if input is empty
        if user_input == "":
            print("Chat ended. Goodbye!")
            break
        
        # Get chatbot response
        try:
            response = chat.send_message(user_input)
            print(f"Chatbot: {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()