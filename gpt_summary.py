from openai import OpenAI

client = OpenAI(api_key="API_KEY")


def get_summary_for_resume(description):
    response = client.completions.create(model="gpt-3.5-turbo-instruct",
    prompt="Summarize the following in bullet points for my resume \n\n"+description,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
    if len(response.choices[0]) > 0:
        points = response.choices[0].text.split("\n")
        s = ""
        # Remove the Bullet point from the response text
        for point in points:
            s += point[1:]+"\n"
        return s
    return ""

def get_summary_for_projects(description):
    response = client.completions.create(model="gpt-3.5-turbo-instruct",
    prompt="Summarize the following in 2 bullet points for my resume \n\n"+description,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
    if len(response.choices[0]) > 0:
        points = response.choices[0].text.split("\n")
        s = ""
        # Remove the Bullet point from the response text
        for point in points:
            s += point[1:]+"\n"
        return s
    return ""
