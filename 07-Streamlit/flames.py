import streamlit as st  

# Function to calculate the relationship status
def calculate_relationship(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Removing common characters
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
    
    # Counting the remaining characters
    count = len(name1) + len(name2)
    
    # Determining the relationship status
    status = ""
    flames = "FLAMES"
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[:index] + flames[index+1:]
        else:
            flames = flames[:len(flames)-1]
    
    # Mapping the relationship status to the result
    if flames == "F":
        status = "Friends"
    elif flames == "L":
        status = "Lovers"
    elif flames == "A":
        status = "Affectionate"
    elif flames == "M":
        status = "Married"
    elif flames == "E":
        status = "Enemies"
    elif flames == "S":
        status = "Siblings"
    
    return status

# Set page title and configure layout
st.set_page_config(page_title="FLAMES Game", layout="centered")

# Display application title and description
st.title("FLAMES Game")
st.write("Enter two names and find out the relationship status!")

# Get user input
name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

# Calculate the relationship status
if st.button("Calculate"):
    if name1 == "" or name2 == "":
        st.write("Please enter both names.")
    else:
        result = calculate_relationship(name1, name2)
        st.write("Relationship Status:", result)
