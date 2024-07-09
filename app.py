from transformers import pipeline

# Load a pre-trained model
try:
    nlp = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", pad_token_id=50256, eos_token_id=50256)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Function to generate text with context
def generate_text(context, prompt):
    try:
        combined_prompt = context + "\n" + prompt
        result = nlp(combined_prompt, max_length=150, temperature=0.7, top_k=50, num_return_sequences=1, truncation=True)
        generated_text = result[0]['generated_text']
        print(f"Generated text: {generated_text}")
        return generated_text
    except Exception as e:
        print(f"Error generating text: {e}")
        return "I'm sorry, I couldn't process that request."

# Main function to handle conversation
def start_conversation():
    context = "AI: Hello! How can I help you today?"
    print("AI: Hello! Type '/start' to begin the conversation or '/end' to end it.")
    conversation_started = False
    
    while True:
        try:
            user_input = input("You: ")
            print(f"User input: {user_input}")

            if user_input.strip().lower() == "/start":
                conversation_started = True
                context = "AI: Conversation started! You can start typing your questions."
                print(context)
            elif user_input.strip().lower() == "/end":
                print("AI: Conversation ended. Goodbye!")
                break
            elif conversation_started:
                context += "\nYou: " + user_input
                response = generate_text(context, "AI:")
                
                # Split the response into lines and take only the last line starting with "AI:"
                ai_responses = [line for line in response.split("\n") if line.startswith("AI:")]
                if ai_responses:
                    ai_response = ai_responses[-1].strip()
                else:
                    ai_response = "I'm sorry, I couldn't process that request."

                print(f"AI: {ai_response}")
                context += "\n" + ai_response

                # Truncate context if it becomes too long
                if len(context.split()) > 500:
                    context = "AI: How can I help you further?"

            else:
                print("AI: Please type '/start' to begin the conversation or '/end' to end it.")
        except Exception as e:
            print(f"Error during conversation: {e}")

# Example usage
if __name__ == "__main__":
    try:
        start_conversation()
    except Exception as e:
        print(f"Unexpected error: {e}")
