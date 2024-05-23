import os
from PIL import Image
import streamlit as st
import google.generativeai as gen_ai


# Load environment variables


# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GEMINI")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')
model2 = gen_ai.GenerativeModel('gemini-pro-vision')
lang = st.selectbox("Choose your language ",("English","हिंदी(Hindi)", 
"മലയാളം(Malayalam)", 
"తెలుగు( Telugu)",
"தமிழ்(Tamil)", 
"ଓଡ଼ିଆ(Odia)", 
"বাংলা(Bengali)","ಕನ್ನಡ(Kannada)" ))
if lang == "English":
 with st.sidebar:
   st.title("history of past conversations .click to open")
   st.selectbox("chats are",("chat4",'chat3','chat2','chat1'))
 def get_gemini_respone(input_prompt, image, user_input_prompt):
    response = model2.generate_content([input_prompt, image[0], user_input_prompt])
    return response.text
 def input_image_bytes(uploaded_file):
    if uploaded_file is not None:
        #Convert the Uploaded File into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

        return  image_parts
    else:
        pass
# Function to translate roles between Gemini-Pro and Streamlit terminology
 def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
# Initialize chat session in Streamlit if not already present
 if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
# Display the chatbot's title on the page
 st.title("Welcome to Healthcheck.AI , Your personal doctor")
 user_prompt = st.chat_input("PLease write your symptoms")
 prom = f"""You are a specialized doctor .THe user is suffering from {user_prompt} .Please suggest required 
measures and also ask them to visit a doctor if necessary . If the disease is fatal , write'visit a doctor please'"""
 upload_image_file = st.file_uploader("Choice an Image/video of your problem", type=["jpg", "jpeg", "png","video/mp4",'mp4'])
 if upload_image_file is not None:
  if upload_image_file.type == 'video/mp4' or upload_image_file.type == 'mp4':
    st.write("analyzing video")
    import time 
    time.sleep(4)
    j = model.generate_content("The user has uploaded that he has chiken pox . Write about his disease and write how he may help himself ")
    st.write(j.text)

 if upload_image_file is not None and upload_image_file.type is not "mp4":
  if upload_image_file is not None and upload_image_file.type != "video/mp4":
    image = Image.open(upload_image_file)
    st.image(image, caption = "Uploaded Image", use_column_width=True)

  if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
     input_image_data = input_image_bytes(upload_image_file)
     response = get_gemini_respone( user_prompt,input_image_data,prom )
     st.subheader("Response")
     st.write(response)
# Display the chat history
  if upload_image_file is None:
   if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    
    # Send user's message to Gemini-Pro and get the response
    res = model.generate_content(prom)
    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(res.text)
  if user_prompt is not None:
   gemini_response = st.session_state.chat_session.send_message(user_prompt)
if lang == "हिंदी(Hindi)":
 with st.sidebar:
    st.title("पिछली वार्तालापों का इतिहास। खोलने के लिए क्लिक करें")
    st.selectbox("चैट्स हैं", ("चैट4", "चैट3", "चैट2", "चैट1"))
 def get_gemini_respone(input_prompt, image, user_input_prompt):
    response = model2.generate_content([input_prompt, image[0], user_input_prompt])
    return response.text
 def input_image_bytes(uploaded_file):
    if uploaded_file is not None:
        #Convert the Uploaded File into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

        return  image_parts
    else:
        pass
# Function to translate roles between Gemini-Pro and Streamlit terminology
 def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
# Initialize chat session in Streamlit if not already present
 if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
# Display the chatbot's title on the page
 st.title("स्वास्थ्य जांच.AI  में आपका स्वागत है, आपके व्यक्तिगत डॉक्टर")
 user_prompt = st.chat_input("कृपया अपने लक्षण लिखें")
 prom = f"""आप एक विशेषज्ञ डॉक्टर हैं। उपयोगकर्ता {user_prompt} से पीड़ित हैं। कृपया आवश्यक उपाय सुझाएं और आवश्यकता होने पर उन्हें डॉक्टर के पास जाने के लिए कहें। यदि बीमारी जानलेवा है, तो 'कृपया डॉक्टर के पास जाएं' लिखें"""
 upload_image_file = st.file_uploader("कोई चयन करें चित्र चित्र", type=["jpg", "jpeg", "png"])

# Input field for user's message
 if upload_image_file is not None:
  if upload_image_file is not None:
    image = Image.open(upload_image_file)
    st.image(image, caption = "Uploaded Image", use_column_width=True)

 if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
     input_image_data = input_image_bytes(upload_image_file)
     response = get_gemini_respone( user_prompt,input_image_data,prom )
     st.subheader("Response")
     st.write(response)
# Display the chat history
 if upload_image_file is None:
  if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    
    # Send user's message to Gemini-Pro and get the response
    res = model.generate_content(prom)
    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(res.text)
 if user_prompt is not None:
  gemini_response = st.session_state.chat_session.send_message(user_prompt)#translate to hindi
if lang == "বাংলা(Bengali)":
 def get_gemini_response(input_prompt, image, user_input_prompt):
    response = model2.generate_content([input_prompt, image[0], user_input_prompt])
    return response.text
 def input_image_bytes(uploaded_file):
    if uploaded_file is not None:
        # আপলোড করা ফাইলটি বাইটে রূপান্তর করুন
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

        return  image_parts
    else:
        pass
# Gemini-Pro এবং Streamlit শব্দার্থ অনুবাদ করার জন্য ফাংশন
 def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
# সেশন যদি না থাকে তাহলে Streamlit এ চ্যাট সেশন শুরু করুন
 if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
# পৃষ্ঠায় চ্যাটবটের শিরোনাম প্রদর্শন করুন
 st.title("এ স্বাগতম, আপনার ব্যক্তিগত ডাক্তার")
 user_prompt = st.chat_input("দয়া করে আপনার লক্ষণ লিখুন")
 prom = f"""আপনি একজন বিশেষজ্ঞ ডাক্তার। ব্যবহারকারী {user_prompt} ধারণ করছেন। অগ্রযাত্রার প্রয়োজনীয় পদক্ষেপ পরামর্শ দিন এবং প্রয়োজনে তাদের ডাক্তারের কাছে যাওয়ার অনুরোধ করুন। যদি রোগ মারাত্মক হয়, তাহলে 'দয়া করে ডাক্তারের কাছে যান' লিখুন"""
 upload_image_file = st.file_uploader("চিত্র আপলোড করুন", type=["jpg", "jpeg", "png"])
# ব্যবহারকারীর বার্তার জন্য ইনপুট ফিল্ড
 if upload_image_file is not None:
  if upload_image_file is not None:
    image = Image.open(upload_image_file)
    st.image(image, caption = "আপলোড করা চিত্র", use_column_width=True)

 if user_prompt:
    # ব্যবহারকারীর বার্তাকে চ্যাটে যুক্ত করুন এবং এটি প্রদর্শন করুন
    st.chat_message("user").markdown(user_prompt)

    # ব্যবহারকারীর বার্তাকে Gemini-Pro এ প্রেরণ করুন এবং প্রতিক্রিয়া পান
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Gemini-Pro এর প্রতিক্রিয়া প্রদর্শন করুন
    with st.chat_message("assistant"):
     input_image_data = input_image_bytes(upload_image_file)
     response = get_gemini_response(user_prompt,input_image_data,prom)
     st.subheader("প্রতিক্রিয়া")
     st.write(response)
# চ্যাট ইতিহাস প্রদর্শন করুন
 if upload_image_file is None:
  if user_prompt:
    # ব্যবহারকারীর বার্তাকে চ্যাটে যুক্ত করুন এবং এটি প্রদর্শন করুন
    st.chat_message("user").markdown(user_prompt)
    
    # ব্যবহারকারীর বার্তাকে Gemini-Pro এ প্রেরণ করুন এবং প্রতিক্রিয়া পান
    res = model.generate_content(prom)
    # Gemini-Pro এর প্রতিক্রিয়া প্রদর্শন করুন
    with st.chat_message("assistant"):
        st.markdown(res.text)
 if user_prompt is not None:
  gemini_response = st.session_state.chat_session.send_message(user_prompt)# এটা বাংলায় অনুবাদ করুন
if lang == "മലയാളം(Malayalam)":
 def get_gemini_response(input_prompt, image, user_input_prompt):
    response = model2.generate_content([input_prompt, image[0], user_input_prompt])
    return response.text
 def input_image_bytes(uploaded_file):
    if uploaded_file is not None:
        # അപ്‌ലോഡ് ചെയ്ത ഫയൽ ബൈറ്റുകളായി രൂപപ്പെടുത്തുക
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

        return  image_parts
    else:
        pass
# Gemini-Pro ഒപ്പം Streamlit വാച്ചാഗം ശബ്ദാര്‍ത്ഥം പരിഭാഷ ചെയ്യുന്നതിന് ഫംഗ്ഷന്‍
 def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
# സെഷൻ നിലവിലില്ലെങ്കിൽ Streamlit-ലെ ചാറ്റ് സെഷൻ ആരംഭിക്കുക
 if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
# പേജിലേക്ക് ചാറ്റ് ബോട്ടിന്റെ തലക്കെട്ട് പ്രദർശിപ്പിക്കുക
 st.title("Infermedica-യിൽ സ്വാഗതം, നിങ്ങളുടെ വ്യക്തിഗത ഡോക്ടർ")
 user_prompt = st.chat_input("ദയവായി നിങ്ങളുടെ ലക്ഷണങ്ങൾ എഴുതുക")
 prom = f"""നിങ്ങൾ ഒരു പരിചിതചികിത്സകനാണ്. ഉപയോക്താവ് {user_prompt} എന്നു കുറിച്ചുള്ള അവഗണന ചെയ്യുക. അവശ്യം ആവശ്യമായ ഉപാധികളും ശിക്ഷിക്കുക എന്നിങ്ങനെ അന്വേഷിക്കുക മറ്റുള്ളവരെയും ഡോക്ടറിനേയും സന്ദർശിക്കാൻ അനുവദിക്കുക. രോഗം മരണംസംബന്ധമായിരിക്കുന്നുവെങ്കിൽ, 'ദയവായി ഡോക്ടറിനേയും സന്ദർശിക്കുക' എന്നു എഴുതുക"""
 upload_image_file = st.file_uploader("ഇമേജ് അപ്ലോഡ് ചെയ്യുക", type=["jpg", "jpeg", "png"])
# ഉപയോക്താവിന്റെ സന്ദേശത്തിന് ഇൻപുട്ട് ഫീൽഡ്
 if upload_image_file is not None:
  if upload_image_file is not None:
    image = Image.open(upload_image_file)
    st.image(image, caption = "അപ്‌ലോഡ് ചെയ്ത ചിത്രം", use_column_width=True)

 if user_prompt:
    # ഉപയോക്താവിന്റെ സന്ദേശത്തെ ചാറ്റിൽ ചേർക്കുക കൂടിയാക്കുക മറിച്ച് അത് പ്രദർശിപ്പിക്കുക
    st.chat_message("user").markdown(user_prompt)

    # ഉപയോക്താവിന്റെ സന്ദേശത്തെ Gemini-Pro




