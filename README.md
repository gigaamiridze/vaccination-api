## Vaccination API
I created this app to find out how many people have been vaccinated with the **Covid vaccine.** Using the app, a person is able to enter their data and eventually a **database of vaccinated people** is created.
### How it works
It is necessary for a person to register and then log in with his / her email and password. The application has four main functions, they are:

 - **Get**
 - **Post**
 - **Edit**
 - **Delete**

> **Get**

To get the information it is necessary for the user to enter the **correct domain** and **ID**.

To get information about a ***specific user***, you first need to specify the domain and then the ID number that belongs to the user. `{{domain}}/user/ID`
	
And to get information about ***all users*** you need to enter the following address: `{{domain}}/user/000`

As for getting information about ***vaccinated people*** in a ***particular case*** we have to do the same as in the case of the user. We only need to enter the ***vaccine*** in the address instead of the ***user***.

To get information about ***all vaccinated people***, we need to enter the following address: `{{domain}}/vaccine/777`

>**Post**

In the case of this feature, the logged in user creates their own data about the vaccination. To do this, you need to enter the following address: `{{domain}}/vaccine/ID`

**Users can only enter the following data:**

 - *name*
 - *surname*
 - *age*
 - *vaccine_type*
 - *dose*
 - *date*
 - *user_id*

> **Edit**

In case of updating the information, we need to retrieve the entered data and then change it at our discretion.

> **Delete**

When deleting user information, it is enough to enter the correct address and a ***specific user*** ID. The following address is: `{{domain}}/user/ID`

As for deleting a ***vaccinated person***, it is necessary to enter the following address with the vaccinated person ID number: `{{domain}}/vaccine/ID`
### Download
The ***libraries*** used in my project can be downloaded by running the following code in the ***terminal***:

    pip install -r requirements.txt