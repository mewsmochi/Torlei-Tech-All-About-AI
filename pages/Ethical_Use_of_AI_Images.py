import streamlit as st

left_col, main_col = st.columns([0.30, 0.95], gap="small", vertical_alignment="top")

with main_col:
        st.image("images/ai_ethical.png")

        st.write("""
        Although the use of AI has a negative stigma surrounding it, AI has created a surplus of different opportunities and resources. 
        It can be helpful in numerous ways as long as it is used “ethically.” Now, what does this ***actually*** mean? To ethically use AI, you have to guarantee that AI is created and applied fairly, transparently, and in a way that benefits all parties involved. 
        Some of the biggest concerns with AI are its occasional unreliability, bias, and overall controversy, specifically regarding the many infringing copyright lawsuits numerous AIs are currently facing. 
        This controversy surrounds AI art and images. The main issue is that occasionally, AI will replicate pictures or text while using copyrighted material to complete that task. 
        Still, with all of these concerns, it is possible to use AI ethically; here are some essential concepts you should know to make sure that you're use of AI is ethically correct: 

        """)

        st.markdown("""
        - **DIVERSITY:** If you're training a model, ensure that your data is diverse and inclusive. 
        This is crucial to prevent your AI from perpetuating stereotypes. 
        
        - **TRANSPARENCY:** Please ensure that you are transparent about your use of AI or how your AI system works. 
        You must specify your process when using AI to prevent any misunderstandings. 
        
        - **RESEARCH:** You must fact-check every piece of data AI gives you. 
        Although AI can usually be reliable for simple questions, the more complex the question or request gets, the more critical it is that you fact check or do background research to see how old the AI is, 
        if the dataset it was trained with is older, or if the AI has a low accuracy rate. 

        - **DATA PROTECTION:** You must ensure your AI complies with data protection regulations. 
        Privacy needs to be safeguarded and encouraged throughout the AI's lifespan. 
        Frameworks for adequate data protection should also be put in place.
                
        - **AI AWARENESS:** If you're going to utilize AI in any piece of work or for general use, ensure that whatever parties you're sharing this information with are informed about AI and how it works. 
        Transparency when using AI is critical, and all parties must be fully aware of what is happening behind the scenes. 

                

        """)

        st.image("images/references.png")

        st.markdown("""
        Inclusion Cloud. (2023, March 17). ***10 Steps to More Ethical Artificial Intelligence***. Inclusion Cloud. 
                Retrieved October 24, 2024, 
                from https://inclusioncloud.com/insights/blog/ethical-artificial-intelligence/

        UNESCO. (\). ***Ethics of Artificial Intelligence***. UNESCO. Retrieved October 24, 2024, 
                from https://www.unesco.org/en/artificial-intelligence/recommendation-ethics

        Wiggers, K. (2023, January 27). ***The current legal cases against generative AI are just the beginning***. 
                TechCrunch. Retrieved October 24, 2024, from 
                https://techcrunch.com/2023/01/27/the-current-legal-cases-against-generative-ai-are-just-the-beginning/

        """)

with left_col:
        st.image("images/victoria_robot.png")