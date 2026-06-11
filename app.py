import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("spam_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Page Config
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩"
)

st.title("📩 SMS Spam Detection System")

st.write(
    "Enter a message below to check whether it is Spam or Ham."
)

# User Input
message = st.text_area(
    "Enter SMS Message",
    height=150
)

# Prediction
if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:

        transformed_message = vectorizer.transform([message])

        prediction = model.predict(
            transformed_message
        )[0]

        probability = model.predict_proba(
            transformed_message
        )[0]

        spam_prob = probability[1]

        st.subheader(
            f"Spam Probability: {spam_prob*100:.2f}%"
        )

        st.progress(float(spam_prob))

        if prediction == 1:

            st.error("🚨 SPAM MESSAGE")

            st.markdown("""
            ### Possible Indicators

            - Promotional language
            - Urgency-based wording
            - Prize or reward claims
            - Suspicious call-to-action
            - Marketing keywords
            """)

        else:

            st.success("✅ HAM (Not Spam)")

            st.markdown("""
            ### Characteristics

            - Appears conversational
            - No suspicious links detected
            - No prize/reward language
            - Typical personal or business communication
            """)