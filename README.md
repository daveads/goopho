### Instructions for backend
// instructions for me incase i forget this shit


**python version for project** : python 3.8.3


# Run commands

```bash
 python -m venv env
 
 source env/bin/activate
 
 pip install -r requirements.txt
 
 //To run app 
 
 python run.py
 
```
//to turn of the virtualenv "deactivate"



# Goopho backend **white paper**


# REQUEST ACCESS

## LOGIN
login in requires "basic auth"
basic auth : username
             password 

then the username, email and token would be sent to you
-----------------------------------








signup details:
-----------------------------------------------

//should include this details

email
first_name
last_name
password
username


**json example format**

{

"name" : "Adejumo David Adewale"

"username" : "daveads"

"email": "daveads@gmail.com",

"password" : "12345",

}

then the name, email and token would be sent to you (for user access)
-----------------------------------------------


headers requirements

access_token (jwt): This would be sent to you but will be save to the cookies

X-CSRF-TOKEN: needed when a **[POST PUT PATCH DELETE]** is method is sent


// would have to create a proper doc for this as time goes
