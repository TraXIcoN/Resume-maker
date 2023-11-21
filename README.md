# Resume Builder using ChatGPT
## Motivation
Crafting a polished and concise resume is essential for job applications and interview success. The critical elements of resume construction include proper formatting and maintaining brevity and formality in content. While customizable templates address formatting concerns, content creation remains time-consuming, especially for students.

ChatGPT's capabilities surpass mere adequacy; OpenAI's tool significantly streamlines tasks, enhances efficiency, and ensures accuracy. To address this challenge, I've developed a resume builder utilizing GPT. This tool transforms informal data inputs into formal job descriptions, facilitating polished resume creation without requiring users to provide formalized descriptions.

## Run Instructions
* **Requirements** : [Python](https://www.python.org/downloads/)
* Install pdflatex (For Mac Users you can execute `brew install --cask mactex`
* Create an [OpenAI API Token](https://beta.openai.com/account/api-keys)
* Replace the API Token in `gpt_summary.py`
* Go to the desired folder and execute `make run`
* After submitting, for checking the result, go to `result/Resume.pdf`
* For further fine-tuning, edit  `resume/Resume.tex`. 
* To export to pdf run `pdflatex -interaction=nonstopmode result/Resume.tex` 

## Results
### UI
<img width="500" alt="image" src="https://user-images.githubusercontent.com/60289522/211463999-bd30781d-d4cd-46d0-98f1-c7d03fdafdd3.png">

### Resultant Resume
<img width="350" alt="image" src="https://user-images.githubusercontent.com/60289522/211461415-96f97ded-f909-4270-a589-8ba6887ff20c.png">

## Referenes
* [OpenAI API documentation](https://beta.openai.com/docs/introduction)
* [Resume Template](https://www.overleaf.com/articles/resume-shubhi-rani-apr-2019/fhxzrkcmjzjp)
