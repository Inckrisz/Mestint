import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Egyszerű tanító adathalmaz
texts = [
    'Free money now!!!',
    'Hi Mom, how are you?',
    'Win a million dollars today!',
    'Reminder: Meeting at 10am tomorrow.',
    'You have been selected for a prize!',
    'Can we have lunch tomorrow?',
    'Congratulations, you are a winner!',
    'Hey, are you coming to the party?',
    'I\'m African prince from Ethiopia and my inheritance is yours!',
    'Will you go to the cinema tomorrow?',
    'You\'ve won my family\'s jewels!',
    'Can I copy your AI homework?',
    'With this course you will be a millionaire in minutes!',
    'Sorry to hear that!',

]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Ham

# 2. Szöveg vektorizálás és modell tanítása
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# 3. Streamlit app
st.title('Spam vagy Ham? - Naiv Bayes osztályozó')

user_input = st.text_input('Írj be egy üzenetet:')

if user_input:
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]

    if prediction == 1:
        st.error('Ez valószínűleg SPAM üzenet!')
    else:
        st.success('Ez egy normális (HAM) üzenet.')
