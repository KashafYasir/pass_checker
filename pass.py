import re
import streamlit as st
import random
import string

# ---------- Page Config ----------
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# ---------- Dark Mode Toggle ----------
dark_mode = st.toggle("🌙 Dark Mode")
if dark_mode:
    st.markdown("""
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stTextInput > div > div > input {
                background-color: #333; color: white;
            }
            .stButton button { background-color: #444; color: white; }
        </style>
    """, unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Check your password strength & generate secure passwords</p>", unsafe_allow_html=True)

# ---------- Show/Hide Toggle ----------
show_password = st.checkbox("👁 Show Password")

# ---------- Password Input ----------
password = st.text_input("Enter your password", type="default" if show_password else "password")

# ---------- Password Generator ----------
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

if st.button("🔁 Generate Strong Password"):
    new_password = generate_password()
    st.success(f"✅ Generated Password: {new_password}")

# ---------- Strength Checker ----------
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8: score += 1
    else: feedback.append("❌ Minimum *8 characters* required.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): score += 1
    else: feedback.append("❌ Use both *uppercase and lowercase* letters.")

    if re.search(r"\d", password): score += 1
    else: feedback.append("❌ Include at least *one number (0–9)*.")

    if re.search(r"[!@#$%^&*]", password): score += 1
    else: feedback.append("❌ Add at least *one special character (!@#$%^&)**.")

    return score, feedback

# ---------- Real-time Feedback ----------
if password:
    score, feedback = check_password_strength(password)
    st.markdown("### Strength Meter:")
    st.progress(score / 4)

    if score == 4:
        st.success("✅ *Strong Password* – Looks great!")
    elif score == 3:
        st.info("⚠️ *Moderate Password* – Can be improved.")
    else:
        st.error("❌ *Weak Password* – Needs attention.")

    if feedback:
        st.markdown("### Suggestions:")
        for fb in feedback:
            st.warning(fb)
else:
    st.info("Enter a password to check its strength.")

