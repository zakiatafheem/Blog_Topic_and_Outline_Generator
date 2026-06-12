import streamlit as st

from main import generate_blog



st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="📝"
)


st.title(
    "📝Blog Topic & Outline Generator"
)


topic = st.text_input(
    "Enter Blog Topic"
)


audience = st.text_input(
    "Enter Target Audience"
)



if st.button("Generate Outline"):


    if not topic or not audience:

        st.warning(
            "Please enter topic and audience"
        )


    else:

        with st.spinner(
            "Generating..."
        ):

            result = generate_blog(
                topic,
                audience
            )


        st.success(
            "Generated Successfully"
        )


        st.subheader(
            "📌 Blog Title"
        )

        st.write(
            result.blog_title
        )


        st.subheader(
            "📋 Outline Sections"
        )


        for i,section in enumerate(
            result.outline_sections,
            start=1
        ):
            st.write(
                f"{i}. {section}"
            )


        st.subheader(
            "🎯 Target Audience"
        )

        st.write(
            result.target_audience
        )


        st.subheader(
            "🚀 Writing Goal"
        )

        st.write(
            result.writing_goal
        )
