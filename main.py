from prompt import get_prompt
from parser import BlogOutline
from model import llm, langfuse


def generate_blog(
    topic,
    audience
):

    prompt = get_prompt()

    formatted_prompt = prompt.format(
        topic=topic,
        audience=audience
    )


    trace = langfuse.trace(
        name="blog_generator"
    )


    structured_llm = (
        llm.with_structured_output(
            BlogOutline
        )
    )


    result = (
        structured_llm.invoke(
            formatted_prompt
        )
    )


    trace.update(
        input={
            "topic":topic,
            "audience":audience
        },

        output=result.model_dump()
    )


    return result