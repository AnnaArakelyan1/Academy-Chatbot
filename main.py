from chatbot import AcademyChatBot

def main():
  cb=AcademyChatBot()
  print("Type 'exit' to quit.")
  while True:
    user_input=input('You: ')
    if user_input=='exit':
        print("ChatBot: Goodbye!")
        break
    elif not user_input.strip():
            print("ChatBot: Please type something.")
    else:
      print('ChatBot: ',cb.process_user_request(user_input))


if __name__=='__main__':
    main()