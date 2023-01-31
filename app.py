# test run of scanning a resume for matching to job descr
# make sure you have installed the OpenAI API client 
# using pip install openai.

# Import the openai module:
import openai

# import the pdf convert script (https://pypdf2.readthedocs.io/en/latest/index.html)
import PyPDF2

# create a file in this same project directory named 'secret' (see README file)
import secret

# Set your OpenAI API key:
openai.api_key = secret.key

job_description = """    Job title: DevOps Engineer 
Company Overview:
At Fake Company Inc., we’re building technology that empowers leaders to deliver efficient and secure widgets to customers, through our international cloud platform.

Job Overview:
Fake Company Inc. seeks a DevOps Engineer to maintain and scale our infrastructure. The DevOps Engineer will be responsible for automation, infrastructure reliability, configuration management, and scripting. Monitoring, logging and tracing are also key components of this role.

Responsibilities:
    Design, test and implement continuous integration and deployment pipelines using GitLab CI
    Design and develop automation tools and frameworks used across the entire development stack
    Optimize system performance, availability and scalability
    Troubleshoot source code management and deployment issues
    Build and maintain IaC for AWS cloud deployments with tools like Terraform
    Create and maintain documentation on configuration, troubleshooting, design etc.
    Perform security audits and assist with hardening servers and systems against attacks
    Assist with IT and compliance, as needed


Qualifications:
    AWS: Security consciousness, adhering to the principle of least privilege access; Exposure to IAM, S3, EKS, lambda, API Gateway, CloudWatch, Kinesis, VPC(s) networking
    CI/CD: Able to design and build CI/CD pipelines using any tool, preferably Gitlab
    Configuration Management: Knowledge and experience with configuration management tools such as: Salt, Ansible, Chef, Puppet
    Development: Familiarity with at least one programming language; Able to write a basic bash script for automation; Comfortable using git
    Kubernetes/Docker: An understanding of k8s infrastructure (Deployment, StatefulSet, Ingress, Certificates); An understanding of how to build docker images, run docker containers, and troubleshoot when a container doesn’t start correctly
    Monitoring: Strong knowledge of Datadog and cloudWatch or similar; In-depth knowledge of Linux server environments; Knowledge of database systems and security
    Terraform: Knowledge of basic module calls is a must; Knowledge advanced Terraform syntax such as ‘dynamic’ is a plus

Compensation and Benefits:
The salary range for this position is $100 - $150K. 
Benefits include:
    Fully paid health insurance (Medical/Vision/Dental)
    Unlimited PTO, Sick and Mental Health Benefits
    11 paid company holidays
    401k with a 4% match
    Generous parental leave
    Annual Professional Development Stipend
    One time Home Office Setup Stipend
"""

# Open the PDF file in read-binary mode
with open(secret.resume_file, "rb") as file:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Initialize a string to hold the resume text
    resume_text = ""
    
    # Iterate over the pages of the PDF
    for page in pdf_reader.pages:
        resume_text += page.extract_text()
        # print(resume_text)
        # Extract the text from

# Use the openai.Completion.create() method to 
# send your resume text to GPT-3 and receive the analysis (handling errors):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            max_tokens=1024,
            temperature=1,
            prompt="I want you to act as a technical recruiter. I will give you a candidate resume and the target job description. You will determine whether or not the candidate has the needed skills to carry out the role, and tell me the result:"
            + job_description
            + resume_text
        )
    except Exception as e:
        print("Error sending request to GPT-3:", e)
        exit()
    
    # The response object will contain the analysis 
    # of your resume, which you can access using the 
    # response.text attribute. 
    # You can then print or process the analysis as needed.

    # Check if the response object has a "text" field
    if "text" in response["choices"][0]:
        # Extract the text field from the response
        text = response["choices"][0]["text"]
        print(text)
    else:
        print("Error: response does not have a 'text' field")



