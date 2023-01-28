Resume Checker

This Python script checks a job candidate's PDF resume against a given job description and asks ChatGPT3 to assess whether the candidate is qualified for the role described.

To use this script:

1. Clone this repository
git clone git@github.com:studiozandra/gpt3-resume-checker.git

2. Go to your account at OpenAI and create an API key. 
3. Create a Python file in this project directory called secret.py, and add the following code, replacing the example strings with your own information:

key = "YOUR_API_KEY_HERE"
resume_file = "C:/Users/your_user_name/Documents/Your_Resume_File.pdf"

4. double-check to make sure that secret.py is listed inside your .gitignore file.

5. create a virtual environment (like a virtual machine running python locally) by either typing:

python -m venv myenv

...or by running:

pip install virtualenv

...then typing:

virtualenv myenv

6. Start up the new virtual environment with this command:
# on Linux or Mac
source myenv/bin/activate

# on Windows
myenv\Scripts\activate

(When you're done working in the virtual environment, you can deactivate it by running the 'deactivate' command.)