from ai import ai_convo
from storage import load_history, save_history


    
history = load_history()
while True:
    user_input = input("You: ")
    if user_input.lower() in [ "/quit"]:
        break
    history.append({"role": "user", "content": user_input})
    reply = ai_convo(history)
    history.append({"role": "assistant", "content": reply})
    print(f"AI: {reply}")

save_history(history)