# How would I improve this project/next steps?

## Error Handling:

Currently, the form has minimal error handling and the errors are not raised on the front-end. 
I would look to add error handling into the front-end. 
E.g. flag to a user that they are missing a response for a required field.
I would also update the back-end to handle different status codes, 
e.g. returning a message to the front-end for a status 400 adding 
the error reasoning from the API response to the message (I noted the JSON response included a descriptive reasoning for status 400 codes). 

Given this project is written within Django, 
I would use Django's messages system to achieve error-handling for 400 status codes.

I would also add in a redirects to a 404 page for 404 errors.

## Displaying Data:

I would incorporate a JS tables package (e.g. https://datatables.net/) to
better populate/represent data provided for the 'watt hours' section of 
the response.

## Saving Data:

I would incorporate a relational db like Postgres and create some Models to save responses from the request.
This could be extended to some auth for the User so their previous searches/solar records are saved.
E.g. I would possibly incorporate a metrics page comparing the solar production of the panel used within the request against their products 


# 1) How to clone the project:
### Via bash terminal:

Execute the following command:
#### git clone https://github.com/Patrick-Messiter/forecast-solar

### Via SourceTree:

Open sourcetree and under the file tab selec the clone option.

Paste under the source path: https://github.com/Patrick-Messiter/forecast-solar

# 2) How to run forecast_solar project:

### Via Docker:

Navigate to the root directory of the project and run the following commands:
Build the container:
#### docker build -t forecast_solar .

Execute the run server command:
#### docker compose up

Alternatively you can use Python's virtualenv. The specific commands for creating your venv would be dependent upon your OS.
Once your virtualenv has been created and activated navigate to the root directory of this project.

Execute the following commands:
#### Install required packages for this project:
#### pip install -r requirements.txt

Execute the run server command:
#### python manage.py runserver