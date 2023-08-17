import pyrebase
import os
import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import asyncio
import json
import re
import random
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from streamlit_card import card
import time
import bz2file as bz
import pickle as pkl

st.set_page_config(
    page_title="Know Tech",
    page_icon=":speech_balloon:",
    layout="wide",
    initial_sidebar_state="expanded"
)

style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# Firebase configuration

firebaseConfig = {
  "apiKey" : "AIzaSyB3yxLFzmBXCLpmsGNpNH_yAOP6W3D_kw0",
  "authDomain" : "source-code-server.firebaseapp.com",
  "projectId" : "source-code-server",
  "databaseURL" : "https://source-code-server-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket" : "source-code-server.appspot.com",
  "messagingSenderId" : "216240307167",
  "appId" : "1:216240307167:web:e5e30125f9a76f235b226a",
  "measurementId" : "G-M84SK9Y6EK"
}

# Firebase Authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.database()
storage = firebase.storage()

if "edit" not in st.session_state:
    st.session_state.edit = False 
if "resume_upload" not in st.session_state:
    st.session_state.resume_upload = False
if "resume" not in st.session_state:
    st.session_state.resume = False

uname = ""
# Page functions
def home_page():
    
    c1,c2 = st.columns([2,1])
    style = """
    <style>
        .css-115gedg.e1f1d6gn1,.css-1r6slb0.e1f1d6gn1{
            border: 1px solid #3D5A80;
            padding:20px;
            border-radius:15px;
            background-color:#0F1C2E;
        }
        .css-1r6slb0 e1f1d6gn1{
            display:flex;
            justify-content:center;
        }
        .css-115gedg.e1f1d6gn1 p{
            text-align:center;
        }
        .css-zt5igj.e1nzilvr3 .css-10trblm.e1nzilvr0{
            text-align:center;
        }
    </style>
    """
    st.markdown(style,unsafe_allow_html=True)
    with c1:
        st.title("Welcome to KnowTech")
        st.subheader("Let's Progress to Level 2")
        my_bar = st.progress(90)
        st.subheader("Your Streaks")
        st.write("0 🔥")
    with c2:
        skill = ["60%","70%","90%","20%"]
        label = ["Full Stack","Java","Cloud Computing","Data science"]
        your_skill = pd.DataFrame(
            {"skills":label,"score":skill}
        )
        st.write("####  Assessment Report ")
        st.markdown(your_skill.to_html(index=False),unsafe_allow_html=True)
    
    c11,c12,c13,c14,c15 = st.columns(5)
    with st.container():
        with c11:
            st.markdown("#### Become a Programming expert")
        with c12:
            st.markdown("#### FullStack")
            st.button("learn Web")
        with c13:
            st.markdown("#### cloud computing")
            st.button("learn CC")
        with c14:
            st.markdown("#### Learn cybersecurity")
            st.button("learn CS")
        with c15:
            st.markdown("#### Learn Data Science")
            st.button("learn Data Science")
    
    style_1 = """
    <style>
    .css-ocqkz7.e1f1d6gn3{
        border: 1px solid #3D5A80;
        padding:10px;
        border-radius:15px;
        background-color:#3D5A80;
    }
    .css-j5r0tf.e1f1d6gn1{
        border: 1px solid #3D5A80;
        padding:10px;
        border-radius:15px;
        background-color:#0F1C2E;
    }
    .row-widget.stButton button{
        width:100%;
    }
    </style>
    """
    st.markdown(style_1,unsafe_allow_html=True)
    
data = bz.BZ2File('model.pbz2', 'rb')
pipe = pkl.load(data)

def stud_pred():
    option = ['Semester Result Precdition','Placement Prediction']

    with st.sidebar:
        selected = option_menu(
            menu_title="Student Login",
            options=option,
            menu_icon="book"
        )


    if selected == option[0]:
        st.title("Semester Result Precdition:")
        c,c0 = st.columns([2,2])

        c1,c2,c3 = st.columns([3,1,3])

        
        with c:
            email = st.text_input("Enter your email-id : ")
        
        with c1:
            iat_1 = st.number_input("Enter your IAT-1 marks :",min_value=0,max_value=100)

            hos = st.number_input("Hour's spend for studying : ",min_value=0,max_value=8)
        with c3:
            iat_2 = st.number_input("Enter your IAT-2 marks :",min_value=0,max_value=100)

            hoe = st.number_input("Hour's spend for entertainment : ",min_value=0,max_value=8)

        attendence = st.slider("Your Attendence Precentage : ",min_value=0,max_value=100)

        if attendence < 75:
            st.warning("Note : If your attendence is less then 75% your are not eligible")
        
        if email != "" :
            btn = st.button("Submit")
            if btn:
                my_bar = st.progress(0, text="Prediction is going on...")

                for percent_complete in range(100):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1, text="Prediction is going on...")
                time.sleep(0.5)
                iat = (iat_1+iat_2)/2
                data = [hos,hoe,iat,attendence]
                res = pipe.predict([data])
                if res:
                    st.success(f"You may pass this examiniation.")
                else:
                    st.error(f"You may fail try to improve.")

                my_bar.empty()
    if selected == option[1]:
        data_2 = bz.BZ2File('model_2.pbz2', 'rb')
        pipe_2 = pkl.load(data_2)

        st.title("Placement Prediction")
        
        st.write("###")
        
        email=st.text_input("Enter your email-id :")

        c4,c5,c6 = st.columns([3,1,3])

        with c4:
            age = st.number_input("Enter your Age : ",min_value=19,max_value=30)

            st.write("###")
            option = st.selectbox(
            'Enter your stream : ',
            ('--Select--','Electronics And Communication', 'Computer Science', 'Information Technology','Mechanical','Electrical','Civil'))

            cgpa = st.number_input("Enter your CGPA: ",min_value=0.0,max_value=10.0,step=0.01)
        with c6:
            stream = {'Electronics And Communication':0, 'Computer Science':1,
                'Information Technology':2, 'Mechanical':3, 'Electrical':4, 'Civil':5}
            
            gender = st.selectbox(
                "Select your gender",
                ('Male', 'Female'))
            
            st.write("###")
            intern_c = st.number_input("Enter no. of Internships attended : ",min_value=0,max_value=8)

            Hostelers = st.selectbox(
                "Have you attended any placement related training before ?",
                ("Yes",'No')
            )
            
        hob = st.selectbox(
            'History Of Backlogs ? ',
            ('Yes','No')
        )

        if st.button("Submit"):
            stre = stream[option]
            if gender == 'Male':
                gen = 1
            else:
                gen = 0
            if Hostelers == "Yes":
                host = 1
            else:
                host = 0
            if hob == "Yes":
                hbl = 1
            else:
                hbl = 0

            res = pipe_2.predict([[age,gen,stre,intern_c,cgpa,host,hbl]])

            if res:
                st.success("You have the chance for getting placed...")
            else:
                st.error("You may not get placed... Try to improve yourself")

def assessment_page():
    mcq_questions = {
        "Python": [
            "What is the result of the following code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)",
            "Which keyword is used for function definition in Python?",
            "What does the 'len()' function do in Python?",
            "What is the output of '3 * 2 ** 3'?",
            "Which data type is used to store a sequence of characters in Python?",
            "What is the purpose of the 'if' statement in Python?",
            "Which of the following is a mutable data type in Python?",
            "What will the 'pop()' method do on an empty list?",
            "Which operator is used for exponentiation in Python?",
            "What is the result of the expression '10 / 3'?",
            "In Python, which loop is used for iterating over a sequence?",
            "Which function is used to read input from the user in Python?",
            "What is the output of 'print(3, 1, 4, sep=\"-\")'?",
            "What is the purpose of the 'pass' statement in Python?",
            "Which module must be imported to work with dates and times in Python?",
            "What is the result of '10 > 5 and not 8 < 3'?",
            "Which method is used to remove leading and trailing whitespaces from a string?",
            "What is the output of 'print(list(range(2, 10, 3)))'?",
            "In Python, which symbol is used to begin a single-line comment?",
            "What is the data type of the result when you divide one integer by another?",
        ],
        "Java": [
            "Which keyword is used to declare a variable that cannot be changed after initialization?",
            "What is the parent class for all classes in Java?",
            "Which data structure uses a Last-In-First-Out (LIFO) approach?",
            "What does the 'static' keyword indicate in Java?",
            "Which loop is used to iterate over elements in an array in Java?",
            "Which Java access modifier provides the widest visibility?",
            "What is the result of '5 / 2' in Java?",
            "Which exception is thrown when an array index is out of bounds?",
            "What is the purpose of the 'break' statement in a loop?",
            "Which method is used to convert a String to an integer in Java?",
            "Which class is used to create an instance of the Scanner object to read user input?",
            "Which Java keyword is used to create a new instance of a class?",
            "Which operator is used for logical AND in Java?",
            "What is the output of 'System.out.println(10 % 3)'?",
            "Which type of inheritance allows a class to inherit from multiple classes?",
            "Which method is used to compare two strings lexicographically?",
            "Which statement is used to create an exception manually in Java?",
            "What is the return type of the 'main' method in Java?",
            "What is the purpose of the 'super' keyword in Java?",
            "Which statement is used to implement code that will always be executed in a try-catch block?"
        ],
        "HTML": [
            "What does HTML stand for?",
            "Which HTML tag is used for creating an ordered list?",
            "Which HTML element is used for line breaks?",
            "Which attribute is used to provide alternate text for an image?",
            "What does the HTML <a> tag represent?",
            "Which HTML tag is used to define a table row?",
            "In HTML, which tag is used to create a hyperlink?",
            "Which HTML tag is used for creating an unordered list?",
            "What does the HTML <p> tag stand for?",
            "Which attribute is used to specify the URL of the linked resource in the HTML <a> tag?",
            "Which HTML tag is used for creating a heading?",
            "What is the correct way to comment out multiple lines in HTML?",
            "Which attribute is used to specify an inline style for an HTML element?",
            "Which HTML tag is used to define the body of a document, containing visible content?",
            "Which HTML element is used for creating a horizontal line?",
            "In HTML, which attribute is used to provide additional information about an element?",
            "What is the purpose of the HTML <meta> tag?",
            "Which HTML tag is used to define an input field for entering text?",
            "What does the HTML <strong> tag represent?",
            "Which HTML tag is used to display an image on a web page?"
        ],
        "JavaScript": [
            "What type of language is JavaScript?",
            "Which keyword is used to declare a variable in JavaScript?",
            "What is the purpose of the 'this' keyword in JavaScript?",
            "Which JavaScript method is used to remove the last element from an array?",
            "What does the '=== ' operator do in JavaScript?",
            "Which built-in function is used to print content to the browser console in JavaScript?",
            "What does the 'NaN' value represent in JavaScript?",
            "Which JavaScript statement is used to create a loop?",
            "Which operator is used to concatenate strings in JavaScript?",
            "What is the purpose of the 'return' statement in a JavaScript function?",
            "Which event is triggered when an HTML element is clicked in JavaScript?",
            "How do you comment out multiple lines in JavaScript?",
            "What does the 'this' keyword refer to in JavaScript?",
            "Which method is used to convert a string to uppercase in JavaScript?",
            "What is the purpose of the 'typeof' operator in JavaScript?",
            "Which statement is used to jump out of a loop in JavaScript?",
            "What does the JavaScript 'slice()' method do?",
            "Which function is used to parse a string and return an integer in JavaScript?",
            "What is the result of '5 + '5' in JavaScript?",
            "Which method is used to round a number to the nearest integer in JavaScript?"
        ],
        "C": [
            "Which programming language is known as the mother of all programming languages?",
            "What is the extension of C source code files?",
            "Which operator is used to access the value at a memory address in C?",
            "What is the purpose of the 'sizeof' operator in C?",
            "Which header file is used to input and output operations in C?",
            "Which data type is used to store a single character in C?",
            "In C, which keyword is used to declare a function?",
            "What does the C 'printf' function do?",
            "Which operator is used to determine the address of a variable in C?",
            "What is the result of '10 / 3' in C?",
            "Which header file is used to perform mathematical operations in C?",
            "Which C keyword is used to define an alias for a data type?",
            "What is the purpose of the 'break' statement in a switch statement in C?",
            "Which C operator is used to access the value of a structure member?",
            "What is the output of 'printf('%d', 5)'?",
            "Which loop in C is executed at least once?",
            "What is the purpose of the 'continue' statement in C?",
            "In C, which symbol is used to indicate a preprocessor directive?",
            "What is the purpose of the 'return' statement in a C function?",
            "Which function is used to allocate memory dynamically in C?"
        ]
    }

    mcq_options = {
        "Python": [
            ["[1, 2, 3]", "[1, 2, 3, 4]", "[4, 2, 3]", "[1, 2, 4]"],
            ["func", "def", "fun", "define"],
            ["Returns the total count of elements in an iterable", "Reverses an iterable", "Converts an iterable to a string", "Returns the sum of an iterable"],
            ["24", "18", "48", "32"],
            ["char", "string", "txt", "str"],
            ["To create a loop", "To declare a function", "To handle exceptions", "To make decisions"],
            ["int", "float", "str", "tuple"],
            ["Raise an exception", "Remove the last element", "Remove the first element", "Do nothing"],
            ["^", "**", "^^", "//"],
            ["3.33", "3.0", "3", "3.333"],
            ["for", "while", "loop", "foreach"],
            ["input()", "read()", "get_input()", "scanf()"],
            ["3-1-4", "3 1 4", "3-14", "3-1-4-"],
            ["To terminate the program", "To skip the current iteration", "To print a message", "To generate random numbers"],
            ["datetime", "time", "date", "timedelta"],
            ["False", "True", "Error", "None"],
            ["trim()", "strip()", "remove()", "clear()"],
            ["[2, 5, 8]", "[2, 5, 8, 11]", "[2, 8]", "[2, 5, 8, 10]"],
            ["#", "//", "/*", "'"],
            ["float", "integer", "double", "decimal"],
            ["max()", "largest()", "maximum()", "top()"]
        ],
        "Java": [
            ["const", "static", "final", "immutable"],
            ["Object", "Super", "Parent", "Base"],
            ["Stack", "Queue", "Array", "List"],
            ["It signifies that the variable is unchangeable", "It indicates that the variable is shared among all instances", "It defines a constant variable", "It prevents memory leaks"],
            ["for", "while", "loop", "foreach"],
            ["public", "private", "protected", "default"],
            ["2.5", "2", "2.0", "2.1"],
            ["ArrayIndexException", "IndexOutOfBoundsException", "ArrayIndexOutOfBoundsException", "OutOfBoundsError"],
            ["Terminate the program", "Skip the current iteration", "Exit the loop", "Do nothing"],
            ["Integer.parseInt()", "stringToInt()", "parseInt()", "toInteger()"],
            ["Console", "Scanner", "InputReader", "Reader"],
            ["new", "create", "instance", "object"],
            ["&", "&&", "and", "&and"],
            ["1", "2", "0", "3"],
            ["Multiple inheritance", "Multilevel inheritance", "Hierarchical inheritance", "Single inheritance"],
            ["compareTo()", "compare()", "equals()", "isEqual()"],
            ["throw Exception('message')", "new Exception('message')", "create Exception('message')", "Exception('message')"],
            ["void", "int", "null", "public"],
            ["To refer to the superclass", "To call a static method", "To access global variables", "To exit a loop"],
            ["finally", "always", "end", "execute"]
        ],
        "HTML": [
            ["Hyperlink Text Markup Language", "HighText Machine Language", "HyperText and links Markup Language", "HyperText Markup Language"],
            ["<ol>", "<ul>", "<dl>", "<li>"],
            ["<lb>", "<br>", "<break>", "<newline>"],
            ["alt", "src", "image", "description"],
            ["Anchor", "Action", "Link", "Reference"],
            ["<td>", "<tr>", "<th>", "<table-row>"],
            ["<a>", "<link>", "<href>", "<hyperlink>"],
            ["<ul>", "<ol>", "<dl>", "<li>"],
            ["Paragraph", "Page", "Content", "Line"],
            ["url", "href", "link", "src"],
            ["<h>", "<head>", "<heading>", "<h1>"],
            ["/* ... */", "<!-- ... -->", "<# ... #>", "<{ ... }>"],
            ["style", "font", "class", "css"],
            ["<body>", "<document>", "<content>", "<main>"],
            ["<hr>", "<line>", "<break>", "<separator>"],
            ["id", "class", "tag", "name"],
            ["Define the character encoding", "Specify the document title", "Link to an external stylesheet", "Create a navigation bar"],
            ["<input>", "<text>", "<textfield>", "<type>"],
            ["Text emphasis", "Important text", "Bold text", "Underlined text"],
            ["<img>", "<image>", "<picture>", "<photo>"]
        ],
        "JavaScript": [
            ["Markup language", "Programming language", "Scripting language", "Query language"],
            ["var", "variable", "v", "let"],
            ["Refers to the current object", "Refers to the previous object", "Refers to the parent object", "Refers to a specific class"],
            ["pop()", "remove()", "delete()", "shift()"],
            ["Strict equality", "Loose equality", "Assignment", "Comparison"],
            ["log()", "print()", "console.log()", "output()"],
            ["Not a Number", "Not available Now", "No Argument", "Negative"],
            ["for loop", "loop", "while loop", "repeat loop"],
            ["+", "&", "concat", "++"],
            ["To terminate a function", "To specify the output", "To return a value from a function", "To exit a loop"],
            ["onclick", "onmouseover", "onchange", "onselect"],
            ["/* ... */", "<!-- ... -->", "// ... //", "# ... #"],
            ["The current function", "The previous object", "The window object", "The parent object"],
            ["toUpperCase()", "toUppercase()", "upperCase()", "upper()"],
            ["To check the type of a variable", "To return the size of an object", "To determine if a property exists", "To convert a value to a string"],
            ["end", "stop", "exit", "break"],
            ["Extracts a section of an array and returns a new array", "Removes a section of an array", "Adds elements to the end of an array", "Reverses the elements of an array"],
            ["Function", "Method", "Procedure", "Action"],
            ["document.write()", "print()", "console.log()", "echo()"],
            ["True", "False", "Error", "Undefined"],
            ["Math.random()", "random()", "rnd()", "Math.rnd()"],
            ["getElement", "selectElement", "queryElement", "querySelector"]
        ],
        "C": [
            ["Cobol", "Curly", "C", "C++"],
            ["Compiled language", "Interpreted language", "Markup language", "Scripting language"],
            ["printf()", "print()", "console.log()", "cout()"],
            ["const", "constant", "value", "let"],
            ["Semicolon", "Colon", "Period", "Comma"],
            ["int main()", "main()", "void main()", "int()"],
            ["===", "==", "=", "equals"],
            ["int", "double", "float", "string"],
            ["while", "for", "do-while", "loop"],
            ["continue", "next", "pass", "break"],
            ["#define", "#ifdef", "#preprocessor", "#ifdefine"],
            ["To exit a function", "To return a value from a function", "To declare a variable", "To print a message"],
            ["malloc()", "allocate()", "new()", "mallocptr()"],
            ["===", "==", "=", "equals"],
            ["int", "double", "float", "string"],
            ["while", "for", "do-while", "loop"],
            ["continue", "next", "pass", "break"],
            ["#define", "#ifdef", "#preprocessor", "#ifdefine"],
            ["To exit a function", "To return a value from a function", "To declare a variable", "To print a message"],
            ["malloc()", "allocate()", "new()", "mallocptr()"]
        ]
    }

    mcq_answers = {
        "Python": [
            2,   
            1,   
            1,   
            1,   
            0,   
            3,   
            3,   
            0,   
            0,   
            0,   
            1,   
            0,   
            1,   
            3,   
            1,   
            1,   
            0,   
            0,   
            0,   
            0    
        ],
        "Java": [
            1,  
            0,  
            2,  
            2,  
            0,  
            3,  
            1,  
            0,  
            2,  
            2,  
            0,  
            3,  
            0,  
            0,  
            1,  
            1,  
            1,  
            0,  
            1,  
            0   
        ],
        "HTML": [
            0,   
            0,  
            0,  
            0,  
            2,  
            2,  
            2,  
            1,  
            0,  
            2,  
            3,  
            1,  
            0,  
            3,  
            0,  
            1,  
            1,  
            0,  
            0,  
            0   
        ],
        "JavaScript": [
            3,   
            0,   
            0,  
            2,  
            0,  
            0,  
            0,  
            3,  
            1,  
            1,  
            0,  
            1,  
            1,  
            2,  
            0,  
            3,  
            2,  
            0,  
            0,  
            1   
        ],
        "C": [
            3,  
            0,  
            0, 
            2, 
            0, 
            0, 
            3, 
            1, 
            3, 
            1, 
            0, 
            2, 
            3, 
            0, 
            0, 
            2, 
            0, 
            1, 
            3, 
            0  
        ]
    }
    option = ["Python", "JavaScript",  "Java", "HTML" ,"C" , ]
    st.title("Programming Language MCQ Quiz")
    selected_language = st.multiselect("Select a language:", options=option)

    st.subheader("MCQ Quiz")

    if "user_answers" not in st.session_state:
        st.session_state.user_answers = [None] * 10000000
        st.session_state.crt_ans = [None] * 10000000

    question_no = 1

    # Loop through selected languages and questions
    for j in selected_language:
        for i, question in enumerate(mcq_questions[j]):
            options = mcq_options[j][i]
            user_answer = st.session_state.user_answers[i]
            user_answer = st.radio(f"Question {question_no}: {question}", options)
            st.session_state.user_answers[i] = options.index(user_answer)
            st.session_state.crt_ans[i] = mcq_answers[j][i]
            question_no += 1

    # Display submit button
    if st.button("Submit"):
        total_questions = question_no - 1
        scores = []
        tot_score = 0
        # Calculate scores for each selected language
        for j in selected_language:
            correct_count = sum([1 for user_ans, correct_ans in zip(st.session_state.user_answers, mcq_answers[j]) if user_ans == correct_ans])
            language_score = (correct_count / total_questions) * 100
            scores.append({"Language": j, "Score": language_score})

            st.write(f"{j} - Score: {language_score:.2f}%")
            tot_score+=language_score
        st.write(f"Total Score: {tot_score:.2f}%")
        c0,c01 = st.columns([1,1])
        with c0:
            # Display pie chart for all languages
            labels = [score["Language"] for score in scores]
            values = [score["Score"] for score in scores]
            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct="%1.1f%%", colors=plt.cm.Paired.colors)
            ax.set_title("Language Scores")
            st.pyplot(fig)

def task_page():
    style = """
        <style>
            .css-ml2xh6.e1f1d6gn1,.css-12w0qpk.e1f1d6gn1{
                border: 1px solid #3D5A80;
                padding:20px;
                border-radius:15px;
                background-color:#0F1C2E;
            }
            .css-y73bov.e1f1d6gn0{
                display:flex;
                justify-content:center;
            }
            .css-1kn7chm.e1nzilvr4 p{
                text-align:center;
            }
            .css-zt5igj.e1nzilvr3 .css-10trblm.e1nzilvr0{
                text-align:center;
            }
            .css-ocqkz7.e1f1d6gn3{
                border: 1px solid #3D5A80;
                padding:10px;
                border-radius:15px;
                background-color:#3D5A80;
            }
            .css-j5r0tf.e1f1d6gn1{
                border: 1px solid #3D5A80;
                padding:10px;
                border-radius:15px;
                background-color:#0F1C2E;
            }
            .row-widget.stButton button{
                width:100%;
            }
        </style>
    """
    st.markdown(style,unsafe_allow_html=True)
    st.title("Practice Task")
    as1,as2 = st.columns([3,1])
    with as1:
        st.markdown("#### Task 1 - Create a simple HTML webpage with a header, navigation menu, content area, and footer using appropriate HTML tags. Style the page using CSS to make it visually appealing.")
    with as2:
        st.button("Task 1")
    as3,as4 = st.columns([3,1])
    with as3:
        st.markdown("#### Task 2 - Set up an S3 bucket and configure it for static website hosting.")
    with as4:
        st.button("Task 2")

def learn_page():
    st.title("Learn Modules")
    with st.sidebar:
        learn = option_menu(
            menu_title="Learn",
            options= ["Self Paced", "Mentoring" ],
        )
    if learn == "Self Paced":
        # it need to be seperated container
        st.subheader("Self Paced")
        try:
            card(
                title="C Programming",
                text="Click Here",
                image="https://static.skillshare.com/uploads/video/thumbnails/b9455fc40a4053509ef0a77b8ddb6a51/original",
                url="https://knowtech-learn.streamlit.app/?page=C",
            )
            card(
                title="Data Science Basics",
                text="Click Here",
                image="https://insidebigdata.com/wp-content/uploads/2019/04/DataScience_shutterstock_1054542323.jpg",
                url="https://knowtech-learn.streamlit.app/?page=DSB",
            )
            card(
                title="Java Basic",
                text="Click Here",
                image="https://th.bing.com/th/id/OIP.-PpueYZ_g4I0noGF_QSgCAHaEK?pid=ImgDet&rs=1",
                url="https://knowtech-learn.streamlit.app/?page=JB",
            )
            card(
                title="Web Development",
                text="Click Here",
                image="https://www.onlinecoursereport.com/wp-content/uploads/2020/07/shutterstock_394793860-1536x1177.jpg",
                url="https://knowtech-learn.streamlit.app/?page=WB",
            )
            card(
                title="Internet of Things (IoT)",
                text="Click Here",
                image="https://th.bing.com/th/id/OIP.K1m17o5mQh-jW0jrHKRtsAHaE8?pid=ImgDet&rs=1",
                url="https://knowtech-learn.streamlit.app/?page=IOT",
            )
        except:
            pass
    if learn == "Mentoring":
        st.subheader("Mentoring")
        left_column, right_column = st.columns(2)
        try:
            with left_column:
                card(
                    title="Viyasan S",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=V"
                )
                card(
                    title="Vishnu Balan O",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=VBO"
                )
                card(
                    title="Sathyaram R",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=SR"
                )
                card(
                    title="Sathish D",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=SD"
                )
            with right_column:
                card(
                    title="Swathi V",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=SS"
                )
                card(
                    title="Yuvasree M",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=YM"
                )
                card(
                    title="Shabari K S",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=SKS"
                )
                card(
                    title="Sathiskumar P",
                    text="View Details",
                    image=None,
                    url="https://knowtech-learn.streamlit.app/?page=SP"
                )
        except:
            pass

    
def datascience(name):
    st.subheader(f"{name} Community")
    if "fullstack_community_mesages" not in st.session_state:
        st.session_state.fullstack_community_messages = []

    for message in st.session_state.fullstack_community_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if msg := st.chat_input("Enter your message here"):
        st.session_state.fullstack_community_messages.append({"role": "user", "content": msg})
        with st.chat_message("user"):
            st.markdown(msg)

def community_page():
    with st.sidebar:
        community = option_menu(
            menu_title="KnowTech Community",
            options= ["Full Stack","Data Science","Cloud Computing", "AI & ML", "Cyber Security", "DevOps", "Blockchain", "IOT", "AR/VR", "Quantum Computing"],
        )

    if community == "Full Stack":
        datascience("Full Stack")
    if community == "Data Science":
        datascience("Data Science")
    if community == "Cloud Computing":
        datascience("Cloud Computing")
    if community == "AI & ML":
        datascience("AI & ML")
    if community == "Cyber Security":
        datascience("Cyber Security")
    if community == "DevOps":
        datascience("DevOps")
    if community == "Blockchain":
        datascience("Blockchain")
    if community == "IOT":
        datascience("IOT")
    if community == "AR/VR":
        datascience("AR/VR")
    if community == "Quantum Computing":
        datascience("Quantum Computing")
class Chatbot:
    @classmethod
    async def create(cls, cookies):
        return cls()

    async def ask(self, prompt, conversation_style, simplify_response):
        # Simulate chatbot response
        return {'text': 'Chatbot response'}
    
def chatbot_page():
    
    def ask(prompt):
        res = asyncio.run(ask_bot(prompt))
        return res

    async def create_chatbot():
        cookies = json.loads(open("./cookies.json", encoding="utf-8").read())
        return await Chatbot.create(cookies=cookies)

    async def ask_bot(prompt):
        bot = await create_chatbot()
        response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative, simplify_response=True)
        
        bot_response = response['text']
        bot_response = re.sub(r"\[\^\d+\^\]", " ", bot_response)
        
        await bot.close()
        
        return bot_response

    st.header("Ai Chatbot")


    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()

            full_response = await ask_bot(prompt)

            
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
        st.experimental_rerun()
    
    
def profile_page():
    nImage = db.child(st.session_state.user['localId']).child("Image").get().val()
    
    if nImage is not None:
        Image = db.child(st.session_state.user['localId']).child("Image").get()
        for img in Image.each():
            img_choice = img.val()
        image_url = img_choice
        uname = db.child(st.session_state.user['localId']).child("Handle").get().val()
        left, right = st.columns([1,3])
        with left:
            st.markdown(
                f"""
                <style>
                    .circle-avatar {{
                        margin-left:-5px;
                        width: 200px;
                        height: 275px;
                        border-radius: 25px;
                        overflow: hidden;
                        display: inline-block;
                        background-image: url('{image_url}');
                        background-size: cover;
                    }}
                </style>
                <div class="circle-avatar"></div>
                """,
                unsafe_allow_html=True,
            )
            resume_upload = st.button("Upload Resume")
            if resume_upload:
                st.session_state.resume_upload = resume_upload
        with right:
            r4,r5,r6 = st.columns([2,1,1])
            with r4:
                st.markdown(f"#### {uname}")
                st.write("Level : 1")
            with r5:
                st.button("Become a Mentor")
            with r6:
                edit=st.button("Edit Profile")
                st.session_state.edit = edit
            r1,r2,r3 = st.columns([1,1,1])
            with r1:
                st.markdown(f"#### 0 🔥")
            with r2:
                st.markdown(f"#### 0 📝")
            with r3:
                st.markdown(f"#### 0 🏆")
            r7,r8 = st.columns([1,3])
            with r7:
                st.subheader("Badges")
            with r8:
                st.markdown(f"#### 0 🥈")
            
        if st.session_state.edit:
            newimgpath = st.file_uploader("Upload Image", type=['png','jpg','jpeg'])
            if st.button("Upload"):
                fireb_upload = storage.child("images").child(st.session_state.user['localId']).put(newimgpath)
                a_imgdata_url = storage.child("images").child(st.session_state.user['localId']).get_url(fireb_upload['downloadTokens'])
                db.child(st.session_state.user['localId']).child("Image").push(a_imgdata_url)
                st.success("Successfully uploaded")
                st.exprerimental_rerun()
            if st.button("Cancel"):
                st.session_state.edit = False
    else:
        st.info("No Profile Picture Yet")
        newimgpath = st.file_uploader("Upload Image", type=['png','jpg','jpeg'])
        upload = st.button("Upload")
        if upload:
            uid = st.session_state.user['localId']
            fireb_upload = storage.child("images").child(uid).put(newimgpath)
            a_imgdata_url = storage.child("images").child(uid).get_url(fireb_upload['downloadTokens'])
            db.child(uid).child("Image").push(a_imgdata_url)
    c1,c2 = st.columns([3,1])
    style = """
    <style>
        .css-ml2xh6.e1f1d6gn1,.css-12w0qpk.e1f1d6gn1{
            border: 1px solid #3D5A80;
            padding:20px;
            border-radius:15px;
            background-color:#0F1C2E;
        }
        .css-y73bov.e1f1d6gn0{
            display:flex;
            justify-content:center;
        }
        .css-1kn7chm.e1nzilvr4 p{
            text-align:center;
        }
        .css-zt5igj.e1nzilvr3 .css-10trblm.e1nzilvr0{
            text-align:center;
        }
        .css-ocqkz7.e1f1d6gn3{
            border: 1px solid #3D5A80;
            padding:10px;
            border-radius:15px;
            background-color:#3D5A80;
        }
        .css-j5r0tf.e1f1d6gn1{
            border: 1px solid #3D5A80;
            padding:10px;
            border-radius:15px;
            background-color:#0F1C2E;
        }
        .row-widget.stButton button{
            width:100%;
        }
    </style>
    """
    st.markdown(style,unsafe_allow_html=True)


    if st.session_state.edit == False:
        with c1:
            st.write("Welcome to KnowTech")
            st.subheader("Let's Progress to Level 2")
            my_bar = st.progress(90)
        with c2:
            st.subheader("Your Streaks")
            st.write("0 🔥") 
    if st.session_state.resume_upload:
        st.subheader("Upload Resume")
        resume = st.file_uploader("Upload Resume", type=['pdf'])
        if st.button("Upload"):
            uid = st.session_state.user['localId']
            fireb_upload = storage.child("resume").child(uid).put(resume)
            a_imgdata_url = storage.child("resume").child(uid).get_url(fireb_upload['downloadTokens'])
            db.child(uid).child("Resume").push(a_imgdata_url)
            st.success("Successfully uploaded")
            st.session_state.resume = True
            st.session_state.resume_upload = False
            st.experimental_rerun()
        if st.button("Cancel"):
            st.session_state.resume_upload = False
    # display the resume by fetching it from firebase
    response = storage.child("resume").child(st.session_state.user['localId']).get_url(None)
    if response:
        st.markdown(f'<embed src="{response}" type="application/pdf" width="100%" height="600px">', unsafe_allow_html=True)
    else:
        st.error("PDF download failed.")
    



if 'user' not in st.session_state:
    st.session_state.user = None

choice = None
if not st.session_state.user:
    choice = option_menu(
        menu_title=None,
        options= ["Login","Sign Up"],
        icons=["🔑","📝"],
        orientation='horizontal',
    )
else:
    choice = None

if choice == "Sign Up":
    st.title(":blue[Sign Up]")
    handle = st.text_input("username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("signup"):
        user = auth.create_user_with_email_and_password(email,password)
        st.success("You have successfully created an account")

        # Sign In

        user = auth.sign_in_with_email_and_password(email,password)
        st.session_state.authenticated_user = user
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])

if choice == "Login":
    st.title(":blue[Login]")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success(f"Logged in as {user['displayName']}")
            st.session_state.user = user
            st.experimental_rerun()
        except Exception as e:
            st.error("Authentication Failed. Please check your credentials.")

if st.session_state.user:
    pages = ["Home", "Assessment", "Learn", "Task", "Community","Chatbot", "Prediction","Profile"]
    with st.sidebar:
        st.image(
            "logo.png"
        )
        sty_img = """
        <style>
            .css-1kyxreq.e115fcil2,.css-1v0mbdj.e115fcil1,.css-1v0mbdj.e115fcil1{
                width:200px;
                height:100px;
            }
        </style>
        """
        st.markdown(sty_img,unsafe_allow_html=True)
        selected_page = option_menu(
            menu_title=None,
            options= pages,
            icons=["house","check","book","list-task","people","chat", "activity","gear"]
        )

    if selected_page == "Home":
        home_page()
    elif selected_page == "Assessment":
        assessment_page()
    elif selected_page == "Learn":
        learn_page()
    elif selected_page == "Task":
        task_page()
    elif selected_page == "Community":
        community_page()
    elif selected_page == "Chatbot":
        chatbot_page()
    elif selected_page == "Profile":
        profile_page()
    elif selected_page == "Prediction":
        stud_pred()
    st.sidebar.markdown("---")
    uname = db.child(st.session_state.user['localId']).child("Handle").get().val()
    st.sidebar.text("Logged in as:")
    st.sidebar.text(uname)
    if st.sidebar.button("Logout"):
        choice = 'Login'
        selected_page=None
        st.session_state.user = None
        st.session_state.messages = []
        st.experimental_rerun()
else:
    st.warning("Please login to access the navigation.")
