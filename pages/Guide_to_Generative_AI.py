import streamlit as st

main_col, right_col = st.columns([0.95, 0.3], gap="small", vertical_alignment="top")

with main_col:
    st.image("images/guide_to_ai.png")

    st.write("#### Intro to Machine Learning and Deep Learning")

    st.markdown("""
        - Generative AI stems from scientists' introduction of **machine learning** in the late 1950s. 
        Machine learning lets computers learn from data to make decisions or predictions without being manually programmed to do so. 
        However, machine learning is not the same as **deep learning**, which is used to create generative AI models; 
        deep learning can learn from its own errors, while machine learning needs a human to intervene. 
        Deep learning also requires much more data than machine learning, which requires significantly more computational power.

        - Generative AI was born from a type of machine learning called neural networks, programs that teach computers to process data in a way inspired by the human brain. 
        **Generative Adversarial Networks (GANs)** are a specific deep learning architecture that gives generative AI its power. 
        They work by training two neural networks against each other to generate more authentic new data from a given training dataset.
        Other neural networks have quickly gained popularity, like **Convolutional Neural Networks (CNNs)** and **Long Short-Term Memory networks (LSTMs)**, 
        but those are outside the scope of this brief guide.


    """)

    st.write("#### Popular Generative AI Tools")

    st.markdown("""
        - There are many useful generative AI tools out there today, but here are some of our favorites out of the most popular ones:

        - ##### **1. ChatGPT:**
            - ChatGPT, created by OpenAI, is a dynamic language model that produces lifelike, engaging, and natural text. 
            ChatGPT can generate content like essays, summaries, product descriptions, news articles, etc. 
            However, the introduction of ChatGPT has brought a rise in plagiarism in academia, 
            and it is also known for providing information from non-existent or unreliable sources.
        
        - ##### **2. Alpha Code:**
            - Alpha Code is a coding assistant that uses generative AI to help developers with their programs. 
            It can generate code, perform debugging, and suggest ways to improve code efficiency. 
            Alpha Code has programming capabilities in Python, C++, and more! 
            However, It is very user-dependent and is not always completely accurate with its code generation and suggestions.

        - ##### **3. GitHub Copilot:**
            - GitHub Copilot is an AI tool for completing code. 
            It offers real-time code snippets, explanations, and context-based guidance on your program. 
            However, using GitHub Copilot can create an over-dependence on auto-complete in beginner programmers, 
            and its suggestions aren't always 100\%\ accurate.
        
        - ##### **4. DALL-E 2**
            - DALL-E 2 is one of the most popular AI tools for generating images. 
            It is known for creating unique and captivating artwork. 
            It takes a text prompt from the user and generates multiple images based on that prompt. 
            However, DALL-E 2, like most AI image generators, is not always anatomically correct, 
            and many people argue that it is not as creative as humans.
    """)

    st.write("#### What does this mean for humans?")

    st.markdown("""
        - We just want to start with **DON'T PANIC**. 
        While AI will continue to become more integrated into our technology, it doesn't mean that the world is going to become a re-creation of IRobot (at least, not yet 😉). 
        However, by allowing AI to automate the more tedious tasks handled by humans today, 
        we can create more free time and enable people to participate in actions that are meaningful to them. 
        The important thing is that as generative AI improves and we use it more frequently, 
        we enforce ethical and legal guidelines specific to the uses of generative AI to protect ourselves and others.

    """)

    st.image("images/references.png")

    st.markdown("""
    Crabtree, M. (2023, July 19). ***What is Machine Learning? Definition, Types, Tools & More. DataCamp***. 
        Retrieved October 24, 2024, 
        from https://www.datacamp.com/blog/what-is-machine-learning

    Duggal, N. (2024, October 16). ***Top Generative AI Tools | Gen AI Tools for 2025***. 
        Simplilearn.com. Retrieved October 24, 2024, 
        from https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/top-generative-ai-tools

    Marr, B. (2023, June 16). ***A Simple Guide To The History Of Generative AI***. 
        Bernard Marr. Retrieved October 24, 2024, 
        from https://bernardmarr.com/a-simple-guide-to-the-history-of-generative-ai/

    Sharma, A. (2024). ***11 Best Generative AI Tools and Platforms in 2024***. 
        Turing. Retrieved October 24, 2024, 
        from https://www.turing.com/resources/generative-ai-tools#1.-chatgpt

    Stackpole, B. (2024, August 6). ***The impact of generative AI as a general-purpose technology***. 
        MIT Sloan. Retrieved October 24, 2024, 
        from https://mitsloan.mit.edu/ideas-made-to-matter/impact-generative-ai-a-general-purpose-technology


    """)

with right_col:
    st.image("images/leila_robot.png")