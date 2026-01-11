## Amsterdam High School Selector Helper

Helps fetch some general information about high schools around the city of Amsterdam such as enrolment, programs, types and such. The app produces a CSV file for you that will hopefully help you find the right school for your children.  

Use at your own discretion. Remember that AI does make mistakes, so take some time to validate the output produced. 

<img src="ams_school.png" alt="System Diagram" width="350"/>

### To use this app:
1. Clone the repo
2. Get the libraries: `pip install -r requirements.txt`
3. Get an OpenAI account
4. Add some API credits to your OpenAI account
5. Create an API token
6. Add the token & your postal code as environment variables: `export OPENAI_API_KEY="[...]"` and `export BASE_POSTAL_CODE="[...]"`
