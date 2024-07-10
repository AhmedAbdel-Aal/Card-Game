import streamlit as st
from card_game.game import Game

def run_game():
    game = Game("Player 1", "Player 2")
    game.setup_game()

    result = []
    while True:
        winner = game.play_turn()
        if winner:
            result.extend(game.game_log)
            result.append(f"{winner.name} has won the game!")
            break
    return result

def format_log_message(message):
    if "Player 1" in message:
        return f"<span style='color:blue'>{message}</span>"
    elif "Player 2" in message:
        return f"<span style='color:green'>{message}</span>"
    elif "wins the game" in message:
        return f"<span style='color:red; font-weight:bold;'>{message}</span>"
    elif "wins this round" in message:
        return f"<span style='color:purple'>{message}</span>"
    elif "No winner in this round" in message:
        return f"<span style='color:orange'>{message}</span>"
    else:
        return message

st.title('Card Game')
st.markdown('### Welcome to the Card Game! Click the button below to start the game.')

if st.button('Run Game'):
    game_log = run_game()

    st.markdown('### Game Log')
    log_container = st.container()

    with log_container:
        st.markdown(
            """
            <div style="max-height: 400px; overflow-y: auto;">
            """,
            unsafe_allow_html=True,
        )
        for line in game_log:
            formatted_message = format_log_message(line)
            st.markdown(formatted_message, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)