import streamlit as st
from streamlit_option_menu import option_menu



course = {
    "Artificial Intelligence (AI) and Machine Learning (ML)" : {
        "the top 10 applications of AI in 2021" : "https://www.youtube.com/live/wnqkfpCpK1g?feature=share",
        "learn Machine Learning Algorithms in detail" :	"https://youtu.be/GwIo3gDZCVQ",
        "learn the Top 10 Artificial Intelligence Technologies In 2022":	"https://www.youtube.com/live/lTzHlU3OrXs?feature=share",
        "Artificial Intelligence concepts with hands"	: "https://youtu.be/JMUxmLyrhSk"
    },
    "Cloud Computing":{
        "Cloud Services and Deployment Models" : 	"https://youtu.be/2LaAJq1lB1Q",
        "important concepts of AWS, Azure, and the Google Cloud Platform":	"https://youtu.be/EN4fEbcFZ_E",
        "Practical implementation" :	"https://youtu.be/2LaAJq1lB1Q",
        "To learn azure & its services in details":	"https://www.youtube.com/live/wK3U7xSt31M?feature=share",
        "to learn AWS from scratch with examples and Hands-on":"https://youtu.be/k1RI5locZE4",
        "Trends in Computing, Distributed Computing":	"https://youtu.be/NzZXz3fJf6o"
    },
    "Cybersecurity":{
        "The fundamentals of Cyber Security" :	"https://www.youtube.com/live/lpa8uy4DyMo?feature=share",
        "The Cyber Security concepts" :	"https://www.youtube.com/live/nzZkKoREEGo?feature=share",
        "The importance of learning about cyber security" :	"https://youtu.be/zHqJcNP2ulY",
        "How it works, why cyber security"	 : "https://youtu.be/inWWhr5tnEA",
        "The Google Cybersecurity" :	"https://youtu.be/_DVVNOGYtmU",
        "Cisco Cyber Security" : "https://youtu.be/A_ZRUWdz6EQ"
    },
    "Internet of Things (IoT)" : {
        "Application and the future of IoT" :	"https://youtu.be/LlhmzVL5bm8",
        "It is extending its power beyond just traditional computers or smartphones" :	"https://youtu.be/7DZR5UaAM0E",
        "what are the characteristics of IoT"	: "https://youtu.be/Ic63-yf-zuc",
        "The efficiency and working of an IoT set-up" :	"https://youtu.be/KeaeuUcw02Q"
    },
    "Web development" : {
        "To prepare for companies like Microsoft, Amazon & Google" :	"https://youtu.be/l1EssrLxt7E",
        "Your Ultimate Guide to Begin Web Development" :	"https://youtu.be/FYErehuSuuw",
        "Learn Web Dev the way professionals do" :	"https://youtu.be/gQojMIhELvM",
        "How does a website work in internet" :	"https://youtu.be/_PUxUu79xFQ",
        "Web Design course" :	"https://youtu.be/C72WkcUZvco",
        "Web Development technologies" :	"https://youtu.be/Q33KBiDriJY"
    },
    "UI&UX" : {
        "What is UI/UX" :	"https://youtu.be/55NvZjUZIO8",
        "Foundation of user Experience Design" :	"https://youtu.be/6qLq7xkodA8",
        "User Interface Design" :	"https://youtu.be/qDUYIQZVQDE",
        "the satisfactory virtual experiences." :	"https://youtu.be/6yN2ZG_TaGM",
        "the process of UI / UX design" :	"https://youtu.be/c9Wg6Cb_YlU",
        "the core of UI UX Design" :	"https://www.youtube.com/live/spGDKJNq-EE?feature=share"
    },
    "C programming":{
        "Introduction" :	"https://youtu.be/gEJBFKDkqTE?si=CCC1_tJDyuDyfSSl",
        "Variables & DataTypes" :	"https://youtu.be/B-fcu5x8hws?si=_wJlQbho1JoMQxhJ",
        "Operators" :	"https://youtube.com/playlist?list=PLBlnK6fEyqRhqQV_MzlT8xsPQnsGcMdIo&si=SuKJz8vRyUhKxQ8M",
        "Control & Looping Statements" : "https://youtu.be/kfZEZj1IOBE?si=W35vlbJnzoEmQ6su",
        "Array" :	"https://youtu.be/MOeGnamlUP4?si=VBKbIp41MzWwwBVo",
        "String Handling"	: "https://youtu.be/b-5beEPeV0c?si=IcgQ2EgpxPaSJn4Z",
        "Functions" :	"https://youtu.be/Wp2OLv7L6LY?si=hZRG11BZ_32B5Qf8",
        "Pointers" :	"https://youtu.be/2GDiXG5RfNE?si=Yqv9KlBiO-pH6CXX",
        "Structures" :"https://youtu.be/c1d987iBBJ0?si=BdoVZ2-wAj5mlZH7",
        "Union" :	"https://youtu.be/-fNpaIH4JBA?si=y_rBv6rG9__lqkpd",
        "Dynamic memory Allocation" :	"https://youtu.be/xDVC3wKjS64?si=xvHCneQxyaoCa33l",
        "Linked List" :	"https://youtu.be/UoS2uWC2Aac?si=MXUJ3Fpe9xHXn33R",
        "Preprocessor" :	"https://youtu.be/D1LshjDhNg8?si=DfuUDvnWEH0vG4vz",
        "File Handling" :	"https://youtu.be/MQIF-WMUOL8?si=nogaGYXj3_MGBqTC",
        "Searching" :	"https://youtu.be/k4xVQhMERuQ?si=TToDCMjP10vtehEf",
        "Sorting" : "https://youtube.com/playlist?list=PLLOxZwkBK52CY_b7jorivUjYzjhoMA_6Z&si=FchB-9asoo600nLP",
        "Merging" :	"https://youtu.be/n1jgmsbCA6s?si=CDWDkqJx5BIkA8iH",
        "Recursion" :	"https://youtu.be/SUfe1UX1m4M?si=jX17faeF7IH1oYXh",
        "Random numbers" :	"https://youtu.be/oXEDMNXzuo4?si=bELK_RhQw5aHKzkJ"
    },
    "Data Science Basic" : {
        "Introduction about Python" :	"https://youtu.be/Y8Tko2YC5hA",
        "Datatypes in python"	: "https://youtu.be/gCCVsvgR2KU",
        "List in python" :	"https://youtu.be/lFzHFUvGL7I",
        "Tuples in python" :	"https://youtu.be/bdS4dHIJGBc",
        "Dictionary in python" :	"https://youtu.be/MZZSMaEAC2g",
        "Arrays in python" :	"https://youtu.be/Rldzskbnjgo",
        "Sets in python" :	"https://youtu.be/wf6-Kcqd3qU",
        "Vector and Matrix in python" :	"https://youtu.be/8d9v6UEIDqM",
        "Functions in python" :	"https://youtu.be/BVfCWuca9nw",
        "Loops in python" :	"https://youtu.be/94UHCEmprCY",
        "Conditional Statement in python" :	"https://youtu.be/PqFKRqpHrjw",
        "Searching and Sorting in python" :	"https://www.youtube.com/live/hpq9FzSfB7k?feature=share"
    },
    "Data Science Intermediate" : {
        "Numpy Tutorial in python" :	"https://youtu.be/8JfDAm9y_7s",
        "Pandas Tutorial in python" :	"https://youtu.be/fAxjxoNqU9o",
        "Matplotlib Tutorial in python" :	"https://youtu.be/c47ZFbAWaNg",
        "Seaborn Tutorial in python" :	"https://youtu.be/6GUZXDef2U0",
        "Scipy Tutorial in python" :	"https://youtu.be/ZlMP7tuLH2Q",
        "Scikit Tutorial in python" :	"https://www.youtube.com/live/7z8-QWlbmoo?feature=share"
    },
    "Data Science Advance" : {
        "Data wrangling in python" :	"https://www.youtube.com/live/pGsTw3P1D_4?feature=share",
        "Exploratory Data Science in python" :	"https://youtu.be/MoM6mighOJM",
        "Data Analysis using python" :	"https://youtu.be/GPVsHOlRBBI",
        "Data Engineering using  python" :	"https://youtu.be/5mpUFFtSxKk",
        "Mathematics and Statistics for Data science"	: "https://youtu.be/8ZI55Inh1_A",
        "Machine Learning using python" :	"https://youtu.be/7eh4d6sabA0",
        "Artificial Intelligence using python" :	"https://youtu.be/7O60HOZRLng"
    },
    "Java Basic" : {
        "Introduction(What is java?)" :	"https://youtu.be/-EKLATNy--o",
        "JDK,JRE,JVM Environment" :	"https://youtu.be/s7UgQ7_1KQY",
        "Java Buzzwords" :	"https://youtu.be/G9oyvA9e7Zg",
        "Compile and Run java program" :	"https://youtu.be/zBF1M8dTftk",
        "Hello World in java" :	"https://youtu.be/I2wvhRUVNTM",
        "Variables  in java" :	"https://youtu.be/haI01OWwFPk",
        "Datatypes in java" :	"https://youtu.be/0MFC_Vw9NxY",
        "Java Main method" :	"https://youtu.be/P-_Nzi_mCRo",
        "Access Modifiers" :	"https://youtu.be/O5nKEJnGR3M",
        "Operators in Java(3 operators) part-1" :	"https://youtu.be/oJLbb_Tgj7s",
        "Operators in Java(3 operators) part-2" :	"https://youtu.be/vwW9-VmYMUg",
        "Conditional Statements in java" :	"https://youtu.be/1hFwOwFJUv0",
        "Loop statements in java" :	"https://youtu.be/tCJZiHEpHbg",
        "Switch Statements in Java" :	"https://youtu.be/wcwWlasmLWs"
    },
    "Java Intermidiate" : {
        "Arrays in java":"https://youtu.be/ibTYCSsuuoI",
        "Single dimensional array in java"	:"https://youtu.be/9MSvQlSjPo4",
        "Two dimensional array in java":	"https://youtu.be/Gbz3Ao2xq_4",
        "Multi dimensional array in java":	"https://youtu.be/v4J2bEQF6jk",
        "Copying elements from array in java":	"https://youtu.be/gXxkKlHKdIM",
        "convert array into array list in java":	"https://youtu.be/87LxjcWR_KI",
        "covert arraylist into array in java":	"https://youtu.be/84CC2TEH6qg",
        "java.util.Arrays Class in java":"https://youtu.be/VJcK-n6G0zw",
        "String in java":"https://youtu.be/cV-sOpOgof8",
        "String class and String Methods in java":"https://youtu.be/DJbTlBPofk0",
        "String Buffer and String Builder class in java":"https://youtu.be/7WsU9SyS-Ui",
        "String Operations in java":"https://youtu.be/5J9o2Q7MqUQ",
        "String Comparison in java":"https://youtu.be/fFQOdtikThs",
        "String methods in java":"https://youtu.be/kYvMdwkM2zE",
        "Class and Objects in java":"https://youtu.be/BHk5Wj28Q5w",
        "Creating an object in java":"https://youtu.be/eKzD-mXrztc",
        "OOPS Concept in java":"https://youtu.be/pTB0EiLXUC8",
        "Java Interface":"https://youtu.be/GhslBwrRsnw",
        "Abstract Class and Methods in java":"https://youtu.be/HvPlEJ3LHgE",
        "Overloading vs Overriding in java":"https://youtu.be/ryDeTfmSY_o",
        "Nested class and Inner class in java":"https://youtu.be/J5_Dac4HX-A"
    },
    "Java Intermediate":{
        "Generics in java":"https://youtu.be/JY8-UMQ7vmY",
        "Exceptional Handling in java":"https://youtu.be/1XAfapkBQjk",
        "Threads in java":"https://youtu.be/b5sj13Z7aho",
        "Creating Threads in java":"https://youtu.be/4cunh9J--t0",
        "Life cycle of threads in java":"https://youtu.be/wE5zxwiiCLs",
        "Mulitasking vs Multiprocessing vs Multithreading":"https://youtu.be/Tn0u-IIBmtc",
        "Core java vs Advanced java":"https://youtu.be/adcEBzrZX48",
        "Advanced java frameworks":"https://youtu.be/VhO343rYXHk"
    }
}


st.set_page_config(page_title="Self Paced", page_icon=":smiley:")

style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

def Courses_played(Courses):
    with st.sidebar:
        selected = option_menu(f"{Courses}", list(course[Courses].keys()))
    
    st.write(f"**{selected}**")
    st.video(course[Courses][selected])


page = st.experimental_get_query_params().get('page', ['default'])[0]

if page == "C":
    Courses_played("Data Science Intermediate")
elif page == "JB":
    Courses_played("Java Basic")
elif page == "JI":
    Courses_played("Java Intermidiate")
elif page == "JA":
    Courses_played("Java Advance")
elif page == "DSB":
    Courses_played("Data Science Basic")
elif page == "DSI":
    Courses_played("Data Science Intermediate")
elif page == "DSA":
    Courses_played("Data Science Advance")
elif page == "Py":
    Courses_played("Python")
elif page == "WB":
    Courses_played("Web development")
elif page == "IOT":
    Courses_played("Internet of Things (IoT)")
elif page == "CS":
    Courses_played("Cybersecurity")
elif page == "AI":
    Courses_played("Artificial Intelligence (AI) and Machine Learning (ML)")
elif page == "CC":
    Courses_played("Cloud Computing")


def Mentorship(Mentors):

    st.subheader(f"{Mentors}")
    if st.button("Request"):
        st.success("Request Sent Successfully! He/She will contact you soon")
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
        """
    - ✔️ 7 Years expereince extracting actionable insights from data
    - ✔️ Strong hands on experience and knowledge in Python and Excel
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )


    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - 📊 Data Visulization: PowerBi, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decition trees
    - 🗄️ Databases: Postgres, MongoDB, MySQL
    """
    )


    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Senior Data Analyst | Ross Industries**")
    st.write("02/2020 - Present")
    st.write(
        """
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
    - ► Redesigned data model through iterations that improved predictions by 12%
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write(
        """
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    st.write(
        """
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """
    )






if page == "V":
    Mentorship("Viyasan")
if page == "VBO":
    Menorship("Vishnu Balan O")
if page == "SR":
    Menorship("Sathyaram R")
if page == "SKS":
    Menorship("Shabari K S")
if page == "SD":
    Mentorship("Sathish D")
if page == "SP":
    Mentorship("Sathiskumar P")
if page == "SS":
    Mentorship("Swathi S")
if page == "YM":
    Mentorship("Yuvasree M")

