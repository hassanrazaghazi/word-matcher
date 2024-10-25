import streamlit as st
import json
import os
import re

# Load settings from keywords.json
def load_settings():
    if not os.path.exists('keywords.json'):
        default_settings = {
            "keywords": [
                "fyp", "final year project", "project", "smart debate arena", "however",
                "upcoming", "context of", "realm of", "overall", "in summary", "in conclusion",
                "delve", "this", "landscape", "contemporary", "finally", "further more",
                "in conclude", "in future", "in the future", "in the near future", "currently",
                "current times", "current era", "at present", "conclusively", "lastly"
            ],
            "highlight_color": "#00FF00"  # Default highlight color (green)
        }
        save_settings(default_settings)
    
    with open('keywords.json', 'r') as file:
        return json.load(file)

# Save updated settings to keywords.json
def save_settings(data):
    with open('keywords.json', 'w') as file:
        json.dump(data, file, indent=4)

# Highlight matched words based on settings
def highlight_matched_words(user_input, settings):
    highlighted_text = user_input  # Start with the user input

    # Create a regex pattern for all keywords (escaping any special characters)
    pattern = r'\b(?:' + '|'.join(re.escape(kw) for kw in settings['keywords']) + r')\b'
    
    # Use re.sub to highlight matched keywords
    highlighted_text = re.sub(pattern, 
                               lambda match: f'<span style="color:{settings["highlight_color"]}">{match.group(0)}</span>', 
                               highlighted_text, 
                               flags=re.IGNORECASE)  # Case insensitive matching

    return highlighted_text.strip()

# Streamlit App
def main():
    # Load current settings
    settings = load_settings()

    # Sidebar for settings
    st.sidebar.title("Settings")

    # Option to update keywords
    st.sidebar.subheader("Update Keywords")
    new_keywords = st.sidebar.text_area("Enter keywords (comma separated):", ", ".join(settings['keywords']))
    
    # Option to update highlight color (dropdown)
    st.sidebar.subheader("Highlight Color")
    color_options = {
        "Green": "#00FF00",
        "Red": "#FF0000",
        "Blue": "#0000FF",
        "Yellow": "#FFFF00",
        "Orange": "#FFA500",
        "Purple": "#800080",
        "Pink": "#FFC0CB",
        "Black": "#000000",
        "Gray": "#808080"
    }
    
    new_color_name = st.sidebar.selectbox("Choose a highlight color:", list(color_options.keys()))
    new_color = color_options[new_color_name]  # Get the corresponding hex code for the selected color
    
    # Save changes button
    if st.sidebar.button("Save Changes"):
        settings['keywords'] = [word.strip() for word in new_keywords.split(",")]
        settings['highlight_color'] = new_color
        save_settings(settings)
        st.sidebar.success("Settings updated successfully!")

    # Main page
    st.title("Dynamic Word Matcher")

    # User input field
    user_input = st.text_area("Enter your text here:")

    # Submit button
    if st.button("Submit"):
        if user_input:
            # Get the highlighted text
            result = highlight_matched_words(user_input, settings)

            # Display the result using Streamlit's HTML display
            st.markdown(f"<div style='font-size:18px'>{result}</div>", unsafe_allow_html=True)
        else:
            st.error("Please enter some text.")

if __name__ == '__main__':
    main()
