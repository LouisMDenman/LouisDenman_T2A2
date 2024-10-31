# Louis Denman T2A2: API Web Server

## Project Setup

The following guide can be used to replicate this API Web Server working environment, assuming Linux or MacOS is being used.

1. Clone the repository [available here](https://github.com/LouisMDenman/LouisDenman_T2A2) to your machine.
2. Open the `'src'` folder in terminal.
3. Run `python3 -m venv .venv`
4. Run `source .venv/bin/activate`
5. Run `pip3 install -r requirements.txt` to install all project dependancies.
6. Create a relevant database table and user, such as grocery_db and grocery_dev to associate with this project in PostgreSQL.
7. Create a `.env` file in the same format as `.env_sample` and add a personal secret key and database URI.
8. Run `flask db create` to create all database tables.
9. Run `flask db seed` to establish sample data in the database.
10. Run `flask run` to start the flask server. Recommended that it is run on `http://localhost:8080`
11. Run `flask db drop` and then repeat steps 8-10 to begin the server again with only the seeded data.

It should be noted that all code comments and documentation are in reference to the [python PEP8 style guide.](https://peps.python.org/pep-0008/)

## R1: Project Significance

In Australia, moving to and living in shared accommodation is a common practice amongst university-level students, especially in light of the cost-of-living crisis seen within the last few years following the COVID-19 pandemic. To be able to attend these universities, many students are required to move from their current residences to locations that make university tuition accessible. This behaviour was displayed within the Australian Council for Educational Research (ACER) analysis of Census data in 2013, which analysed the data of university attendees from 2006-2011 compared with the greater Australian population. Within this analysis, ACER found that from 2006 to 2011, university students had a 4.2% increase in address change from 5 years prior, going from 34.7% in 2006 to 38.9% in 2011. Comparatively, the entire population of Australia only experienced a 1.9% increase in address change from 5 years prior during 2006-2011, seeing 31% go to 32.9% from 2006 to 2011 (ACER, 2013). Whilst there is not a more relevant study currently published that looks at these statistics, this analysis shows that as time progresses and degrees are more valued, higher amounts of students will move to accommodate study. Regarding the total number of university students enrolled in the country, the number has decreased over a decade by 12% in 2023, which is largely associated with the cost of living issues and younger generations being more conscious of HECS-debt (Cassidy, 2023). Despite this, cost of living has also driven younger people who are not studying higher education to increasingly move into shared accommodation options, so that they may pursue greater living conditions in the future (Hutchens, 2023). As a result, for both students and working young Australians alike, shared accommodation is a likely reality that they will have to experience to progress their financial wellbeing and combat the effects of the cost of living crisis. One of the most important life expenses to consider other than locational expenses is grocery/food expenses. With dining experiences from fast food to Fine Dining all increasing in expense, more and more younger people are eating out less, and are trying to save money by purchasing groceries and cooking. 

When these shared houses are considered in relation to food and groceries, it is clear that it can become convoluted and difficult to communicate with multiple roommates what ingredients are present in the household, what ingredients are required for the next grocery period, etc. To combat this issue, the idea behind this project is to create a grocery list API web server. The main function of this grocery API allows individuals to create unique grocery lists with their selected assortment of ingredients. On top of this, users will have the ability to add friends and comment on these friend's lists, as a way of encouraging the collaboration and communication of roommates/shared households when purchasing groceries. As a result, when this API is used: its users can avoid buying items they already have, get ingredients that all household members want, and comment on others' grocery lists if they have forgotten items or would like to include new items. This, in turn, allows all members of shared accommodation to more efficiently get all the groceries they want, whilst saving money during the current cost of living crisis.

ACER. (2013, July 15). _Leaving home to study_. Australian Council for Educational Research. https://www.acer.org/au/discover/article/leaving-home-to-study

Cassidy, C. (2023, November 16). _Number of Australians enrolled in bachelor degrees falls by 12% in less than a decade_. The Guardian. https://www.theguardian.com/australia-news/2023/nov/16/australia-higher-education-university-enrolment-decline-falls-why-cost

Hutchens, G. (2023, November 8). _Demand for share housing keeps rising as cost-of-living crisis continues_. ABC News. https://www.abc.net.au/news/2023-11-09/demand-for-sharehousing-keeps-growing-cost-of-living-crisis/103079102#

## R2: Project Allocation and Tracking

Within this API Web server project, the kanban agile workflow was utilised for project management and tracking. The below screenshots show the project kanban at the beginning and end of the project, while the full board can be viewed [here.](https://trello.com/invite/b/669dfff3a6a527f7acdc79ec/ATTI3fe3d3cf86aec22fe64e9ce62121d2ea7F19C70C/t2a2)

![Trello project start](/docs/trello_1.png)

![Trello project end](/docs/trello_2.png)

## R3: Third Party Dependancies

#### Flask:

Flask is a lightweight WSGI framework that is specifically designed to be simplistic to use and scale applications with. It is classed as a micro-framework, due to the fact that it does not require any particular libraries or tools to function, allowing developers to choose whatever is relevant to their application. This means Flask only covers the essentials for creating web applications, such as request handling and routing, in which the framework maps URLs to python functions and provides built-in support for HTTP methods. Any other function required can be handled by other tools or libraries as mentioned above, which makes Flask very flexible in its range of function that it can provide when creating web applications, and is a very flexible framework that can handle very simple small projects all the way to larger complex web applications. Flask also includes built-in development server settings, which allow developers to locally test and debug applications, and like the rest of Flask it is very simplistic and easy to use for beginners and experienced developers alike. Finally, Flask is an open source framework that has a very large community supporting it, and is very well documented which further contributes to its simplicity to use.

#### Postgresql:

Postgresql is a popular open-source relational database and database management system (RDBMS), that was built to be robust, extensible and reliable. Since its conception, there has been a large community in support and growing documentation about its features and functionality. Some of these are: full ACID (Atomicity, Consistency, Isolation, Durability) compliance, which ensures reliable transaction processing and data integrity; high extensibility, allowing for developers to create new operators, types, functions and extensions in a range of different programming languages; a high level of SQL compliance, along with support for advanced SQL features like complex queries, joins, views, triggers and stored procedures; high levels of concurrency and the ability to handle large datasets well, even with high traffic loads. These reasons, along with the benefits listed in R4 below, make postgresql a very suitable choice for this web application.

#### Marshmallow:

Marshmallow is a popular python library that simplifies the conversion of complex data types into python data types, and vice versa. It does so by taking the complex data types such as database models, and changes these data types into native python data types such as lists or dictionaries, and thus serializes the data. The opposite process is also supported, where python native data in lists or dictionaries gets converted to more complex data such as database models, and is hence deserialized. To allow the serilalization and deserialization process to occur more robustly, Marshmallow allows developers to create schemas by the using python classes, which instruct how objects are serialized and deserialized. These schemas can also define any data validation that is required to occur, which is the other main compenent of Marshmallow, and ensures any user entry conforms to the required validations that developers specify. Marshmallow is designed to be extensible, allowing the developers to specify their own schemas and validators, as well as being compatible with a range of other popular libraries and solutions used for other parts of the application. The library also has extensive documentation, which ensures it is easy to use and implement.

#### Bcrypt:

Bcrypt is a password hashing library that is designed to increase the security of web applications. The library takes standard string formats, and converts them into a hashed string format that by design cannot be reverse-hashed to discover what the original password was. The library is able to do so through a number of processes, including salt generation, which is where a random value is added to the password before hashing so that identical passwords cannot be detected. Bcrypt also allows developers to control the cost factor of the computational expensiveness of the hashing process, meaning that as an applications scales and is more likely to be targeted by malicious attacks, that cost of hashing increases and thus is more likely to be secure. Bcrypt was designed as a more simplistic security library to use, and with its extensive documentation is easy to implement and a good option for smaller scale web applications.

#### SQLAlchemy:

SQLalchemy is an open-source python library that functions as an SQL toolkit and Object-Relational Mapping (ORM) system. The library introduces a large number of number of API interfaces to a working environment that allow developers to interact with underlying database systems through programmatic means. Utlising SQLAlchemy, developers are not required to use raw SQL statements, but can instead utilise python functions and classes to control database interaction and data.

#### Flask-JWT:

Flask-JWT is an extension for the Flask framework that allows the use of JSON web tokens (JWT) for authentication purposes, allowing developers to seamlessly manage the authentication and authorization of users. The extensison adds a range of decorator functions that can be used for authentication or authorization requirements, including the creation of JWT tokens, verifying JWT tokens and protecting routes from invalid users. Flask-JWT also allows developers to control the configuration of JWT handling, including how long JWT tokens are valid for, algorithms used for signing the tokens, and what the secret key value is (which is used for signing tokens). Furthermore, Flask-JWT includes built-in error handling for common problems that occur such as missing, invalid or expired tokens, and allows developers to custom display these errors so that they have more value and meaning to users.

#### Psycopg2-binary:

Psycopg2-binary is a library specific to Postgresql, that acts as an adapter between python and SQL commands. Where SQLAlchemy is a higher-level abstraction that interacts with databases in an object-oriented manner, Psycopg2-binary serves as a lower-level abstraction that is more suitably used for when fine control and execution of very specific queries is required. It is also built to interface well with SQLAlchemy, where Psycopg2-binary serves as an underlying adapter/driver that SQLAlchemy utilises when connecting to and interacting with a Postgresql database.

#### Python Dotenv:

Python-dotenv is a library that allows .env files to be read and their variable contents be loaded into the working environment of a python workspace. This allows developers to configure sensitive details relating to applications or projects such as database credentials, API keys or access token settings, without hard coding them into the project as to stop anyone with malicious intent accessing the data.

## R4: Underlying Project Database Benefits and Drawbacks

As mentioned above in the third party dependancies section of this documentation, Postgresql is the underlying database system being used for this API web server project. Below are some of the benefits and drawbacks of the Postgresql database system:

### Benefits:

* __Flexibility:__ Postgresql is a highly flexible database system, being able to support a large range of standard/custom data types, supporting both standard SQL and NoSQL, and allowing developers to define personal functions and operators. Postgresql also interfaces with the majority of programming languages that are used currently, and is far more compatible in this regard that many other database system options available, allowing developers to create their applications or soultions in whatever languages are the most applicable.
* __Reliability:__ Postgresql as a database is highly stable, and was built to be able to handle large amounts of data without any threat of data loss or crashing. As well as this, the database is fully ACID compliant, which ensure that all transactions occuring in the database are highly reliable and fault-tolerant.
* __Scalability:__ Postgresql was also designed to be scalable, and as a result can be used as a single instance on a given machine or server, as well as multiple instances that are distributed over a multitude of servers. The database also has a range of supported optimisations that were implemented specifically for ensuring that Postgresql can be used just as smoothly and reliably at a larger scale with multiple instances. One such optimisation is support for high concurrency, which allows multiple users to access a piece of data at the same time, as opposed to locking other users out of the data until the current transaction is finished like some other databases do.
* __Security:__ Postgresql has a solid level of security protocol built in, and interfaces with a wide range of extensions that can increase the databases security even further comparitively with other databases.
* __Code Commentation:__ The ability to create code comments within the database is a feature that Postgresql possesses where some other relational databases do not. Being able to add code comments greatly helps all levels of developers, and contributes in making a clear database system design that can be easily followed and used by other developers or users.

### Drawbacks:

* __Performance:__ In general, Postgresql is a compartively quick database system to use compared to other relational database options, but there are some specific use cases in which Postgresql becomes fairly slow and can degrade total performance. An example of this is backup and recovery procedures; Postgresql is designed as a highly reliable database that is fault tolerant as mentioned before, so backup and recovery procedures are rarely if at all needed, but when they are performance is affected.
* __Complexity:__ Whilst the extensive amount of support for general configurability and extensions can be beneficial for the extensibility of large scale complex applications, it can make the intialisation and maintenance of smaller projects more difficult than other relational database options, especially for individuals that are not as familiar with the RDBMS.
* __Open Source:__ Despite possessing a large supporting community that drives innovation and development of Postgresql due to being open-source, it's non-proprietary nature means that there is no warranty or liability and indemnity protection, which puts developers at risk if they face these issues as their web application scales up.

## R5: Project ORM Features, Purpose and Functionality

The Object-Relational Mapping (ORM) system used within this project is the SQLAlchemy library for python. SQLAlchemy is an open-source library that provides an SQL toolkit, as well as a range of API interfaces that allow developers to interact with databases using python objects. This in turn allows a more flexible and streamlined workflow to occur for developers, in which raw SQL does not have to be used. Some of the most notable features and functionality of SQLAlchemy are:

* __ORM not required:__ SQLAlchemy consists of two major components: the core, and the ORM. The core is the lower level component of the library, and is responsible for the direct execution of SQL statements from python, providing a more programatic method of controlling databases. The ORM, however, is a higher level component of the library that builds on top of the core functionality. This provides developers with an abstraction layer of functionality that allows the use of object-oriented programming and classes to control database tables and records, but is not required to be used, giving developers the freedom to choose if they require just the core functionality or further ORM functionality as well.
* __Non-opinionated:__ To ensure that there is no confliction with pre-existing or other database and application architechture, SQLAlchemy does not generate schemas or relies on specific naming conventions of any form, which is not the case with many other ORMs. As a result, SQLAlchemy provides wider support for a larger range of architechtual designs compared with many other ORM systems.
* __Unit of work:__ Unit of Work is a system implemented within the SQLAlchemy ORM, which organises any pending delete, update or insert statements into queues, and then processing these queues all at once. To achieve this, the system makes use of a dependacy sort on the queues, which accounts for dependancies between rows and combines redundant statements. As a result, transactions are more efficient and safe, and there is a lower likelyhood of deadlocks occuring within the database.
* __Function-based query construction:__ SQLAlchemy core allows the creation of functions and expressions in python that control database queries, including those with conditions, operators, subqueries, commands and joins. These functions can also be customised to interface with functionality specific to particular underlying database systems if applicable.
* __Modularity & Extensibility:__ SQLAlchemy is designed to be fully modular and extensible. The ORM functionality is not required to be used if not nessessary, and within the core component, the different functionalities can be used independantly as nessessary. For the features and functionality that are being used, SQLAlchemy supports a range of plugins that extend these functionalities further.
* __Composite Primary Keys:__ SQLAlchemy was designed to be able to handle complex primary and foreign key scenarios, such as being able to handle mutability and compatibility of meaningful primary keys with ON UPDATE CASCADE, and handling many-to-many relationships that contain extra detail for each link.
* __Database support:__ SQLAlchemy was built to work well with any choice of underlying database system, and has compatibility with nearly any system today, including Postgresql, MySQL, MariaDB, Oracle, etc.

## R6: ERD Design and Explanation

![Project Start Database ERD](/docs/APIERD-5.jpg)

ERD Legend:
- Table names are listed in their own row at the top of each box.
- Table attributes are listed below the table names in the right column.
- Primary keys are underlined, and also denoted by a 'PK' in the left column next to the relevant attribute.
- Foreign keys are not underlined, but are denoted by an 'FK' in the left column next to the relevant attribute.
- All relationships are one-to-many, with the two prong side facing the relevant primary key attribute, and the crow foot side facing the relevant foreign key attribute.

Pictured above is the established Entity Relationship Diagram (ERD) at the conception of the Web Server API Project. Each table within this ERD is normalised, meeting the nessessary three normal forms. Each table has atomic values that are indivisible and contain values of a single type, meeting the first normal form; all non-key attributes are fully functionally dependant on the primary key, which meets the second normal form; and finally, all non-key attributes are not dependant on anything except the candidate key, meeting the third form.

An example seen below of the first iteration of this ERD shows a less normalised example, as intially there was a many to many relationship present between grocery_lists and products, which meant that multiple values were being stored in some of the rows and thus is not meeting the normal forms.

![Initial Database ERD](/docs/APIERD.jpg)

## R7: Implemented Models Explanation

In the implemented version of the API web project, the same ERD and models from R6 were used. In regard to relationships:
* connections.friend1_id and connections.friend2_id are both foreign keys in a many to one relationship with primary key users.user_id
* grocery_lists.user_id is a foreign key in a many to one relationship with primary key users.user_id
* comments.user_id is a foreign key in a many to one relationship with primary key users.user_id
* comments.list_id is a foreign key in a many to one relationship with primary key grocery_lists.list_id
* productlist.list_id is a foreign key in a many to one relationship with primary key grocery_lists.list_id
* productlist.product_id is a foreign key in a many to one relationship with primary key products.product_id

## R8: Project API Endpoints Guide

Within this API Web Server project, there are a number of API endpoints that each serve their unique purposes. The Endpoints are described below:

* __Route:__ http://localhost:8080/auth/register
    * __HTTP Verb:__ POST
    * __Required body example:__ {"first_name": "Bruce", "last_name": "Wayne", "email": "Wayneindustries@gmail.com", "password": "TheJokeris1ame!"}
    * __Authorisation__ None
    * __Explanation:__ This route is responsible for allowing a new user to register in the project. A successfull registration will return the users details apart from their password, whereas a JSON field listing an error will be returned if there is something invalid about the process.
    * __Successful Output:__ {
	"user_id": 4,
	"first_name": "Bruce",
	"last_name": "Wayne",
	"display_name": "BruceWayne",
	"email": "Wayneindustries@gmail.com",
	"grocery_list": [],
	"comments": [],
	"connections": []
}
    * __Unsuccessful Output:__ {
	"error": "That email is already in use, please try another email."
}

* __Route:__ http://localhost:8080/auth/login
    * __HTTP Verb:__ POST
    * __Required body example:__ {"email": "LouisDenman@gmail.com", "password": "Lou1sdenman!"}
    * __Authorisation__ None
    * __Explanation:__ This route is responsible for allowing a current user to login. A successfull login will return the users email and a JSON token, whereas a JSON field listing an error will be returned if the login is invalid.
    * __Successful Output:__ {
	"email": "LouisDenman@gmail.com",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjE2ODY3NCwianRpIjoiNjZlYmU4MzQtNjY1MC00YjgzLTk1YTktZGQyZDQ3MDI4ZTQ0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3MjIxNjg2NzQsImNzcmYiOiI4OTFmZjBhMi1kOWFjLTRmMjktYTU0MS1kNzExMTU2YmEzMDIiLCJleHAiOjE3MjIxNzk0NzR9.thfENpeAWa8X6VrsQYKEpi3_k-2_0u5LPo4JSZbT0v4"
}
    * __Unsuccessful Output:__ {
	"error": "Invalid email or password"
}

* __Route:__ http://localhost:8080/grocery_lists
    * __HTTP Verb:__ GET
    * __Required body example:__ {}
    * __Authorisation__ None
    * __Explanation:__ This route is responsible for viewing all grocery lists.
    * __Successful Output:__ [
	{
		"list_id": 1,
		"list_name": "Housemates grocery list",
		"user": {
			"user_id": 1,
			"display_name": "LouisD",
			"email": "LouisDenman@gmail.com"
		},
		"product_list": [],
		"comments": [
			{
				"comment_id": 1,
				"message": "We are making tacos this week, make sure you grab the spice mix",
				"timestamp": "22:08:07/28/24",
				"user": {
					"display_name": "MJparker",
					"email": "Maryjane@gmail.com"
				}
			}
		]
	},
	{
		"list_id": 2,
		"list_name": "Family grocery list",
		"user": {
			"user_id": 2,
			"display_name": "Jsmith",
			"email": "Johnsmith@gmail.com"
		},
		"product_list": [
			{
				"id": 1,
				"products": {
					"product_id": 6,
					"product_name": "Watermelon",
					"product_price": 4.0
				},
				"quantity": 5
			},
			{
				"id": 2,
				"products": {
					"product_id": 9,
					"product_name": "Cucumber",
					"product_price": 1.0
				},
				"quantity": 3
			},
			{
				"id": 3,
				"products": {
					"product_id": 14,
					"product_name": "Pork",
					"product_price": 9.0
				},
				"quantity": 2
			},
			{
				"id": 4,
				"products": {
					"product_id": 24,
					"product_name": "Bread",
					"product_price": 3.0
				},
				"quantity": 7
			},
			{
				"id": 5,
				"products": {
					"product_id": 30,
					"product_name": "Magazine",
					"product_price": 5.0
				},
				"quantity": 1
			}
		],
		"comments": [
			{
				"comment_id": 2,
				"message": "grab apples pls thx",
				"timestamp": "22:08:07/28/24",
				"user": {
					"display_name": "LouisD",
					"email": "LouisDenman@gmail.com"
				}
			}
		]
	},
	{
		"list_id": 3,
		"list_name": "Groceries",
		"user": {
			"user_id": 2,
			"display_name": "Jsmith",
			"email": "Johnsmith@gmail.com"
		},
		"product_list": [
			{
				"id": 6,
				"products": {
					"product_id": 10,
					"product_name": "Eggplant",
					"product_price": 1.5
				},
				"quantity": 6
			},
			{
				"id": 7,
				"products": {
					"product_id": 12,
					"product_name": "Turkey",
					"product_price": 6.5
				},
				"quantity": 2
			},
			{
				"id": 8,
				"products": {
					"product_id": 20,
					"product_name": "Cottage Cheese",
					"product_price": 3.0
				},
				"quantity": 6
			},
			{
				"id": 9,
				"products": {
					"product_id": 22,
					"product_name": "Brown Rice",
					"product_price": 5.0
				},
				"quantity": 4
			},
			{
				"id": 10,
				"products": {
					"product_id": 28,
					"product_name": "Containers",
					"product_price": 15.0
				},
				"quantity": 1
			}
		],
		"comments": []
	}
]
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/grocery_list/<int:list_id>
    * __HTTP Verb:__ GET
    * __Required body example:__ {}
    * __Authorisation__ None
    * __Explanation:__ This route is responsible for viewing 1 single grocery list.
    * __Successful Output:__ {
	"list_id": 2,
	"list_name": "Family grocery list",
	"user": {
		"user_id": 2,
		"display_name": "Jsmith",
		"email": "Johnsmith@gmail.com"
	},
	"product_list": [
		{
			"id": 1,
			"products": {
				"product_id": 6,
				"product_name": "Watermelon",
				"product_price": 4.0
			},
			"quantity": 5
		},
		{
			"id": 2,
			"products": {
				"product_id": 9,
				"product_name": "Cucumber",
				"product_price": 1.0
			},
			"quantity": 3
		},
		{
			"id": 3,
			"products": {
				"product_id": 14,
				"product_name": "Pork",
				"product_price": 9.0
			},
			"quantity": 2
		},
		{
			"id": 4,
			"products": {
				"product_id": 24,
				"product_name": "Bread",
				"product_price": 3.0
			},
			"quantity": 7
		},
		{
			"id": 5,
			"products": {
				"product_id": 30,
				"product_name": "Magazine",
				"product_price": 5.0
			},
			"quantity": 1
		}
	],
	"comments": [
		{
			"comment_id": 2,
			"message": "grab apples pls thx",
			"timestamp": "22:08:07/28/24",
			"user": {
				"display_name": "LouisD",
				"email": "LouisDenman@gmail.com"
			}
		}
	]
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/create_grocery_list
    * __HTTP Verb:__ POST
    * __Required body example:__ {
	"list_name": "Weekly Groceries"
}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for creating grocery lists.
    * __Successful Output:__ {
	"list_id": 4,
	"list_name": "Weekly Groceries",
	"user": {
		"user_id": 1,
		"display_name": "LouisD",
		"email": "LouisDenman@gmail.com"
	},
	"product_list": [],
	"comments": []
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/delete_grocery_list/<int:list_id>
    * __HTTP Verb:__ DELETE
    * __Required body example:__ {}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for the deletion of grocery lists.
    * __Successful Output:__ {
	"message": "Grocery List 'Weekly Groceries' deleted successfully."
}
    * __Unsuccessful Output:__ {
	"error": "Grocery List with list_id '4' not found"
}

* __Route:__ http://localhost:8080/update_grocery_list_name/<int:list_id>
    * __HTTP Verb:__ PUT, PATCH
    * __Required body example:__ {
	"list_name": "Test grocery list"
}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for changing the name of a grocery list.
    * __Successful Output:__ {
	"list_id": 1,
	"list_name": "Test grocery list",
	"user": {
		"user_id": 1,
		"display_name": "LouisD",
		"email": "LouisDenman@gmail.com"
	},
	"product_list": [],
	"comments": [
		{
			"comment_id": 1,
			"message": "We are making tacos this week, make sure you grab the spice mix",
			"timestamp": "21:52:07/28/24",
			"user": {
				"display_name": "MJparker",
				"email": "Maryjane@gmail.com"
			}
		}
	]
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/grocery_list/<int:list_id>/comments
    * __HTTP Verb:__ POST
    * __Required body example:__ {
	"message": "Make sure you don't forget the eggs"
}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for creating a comment on a grocery list.
    * __Successful Output:__ {
	"comment_id": 3,
	"message": "Make sure you don't forget the eggs",
	"timestamp": "22:00:07/28/24",
	"user": {
		"display_name": "LouisD",
		"email": "LouisDenman@gmail.com"
	},
	"grocery_list": {
		"list_id": 1,
		"list_name": "Test grocery list",
		"user": {
			"user_id": 1,
			"display_name": "LouisD",
			"email": "LouisDenman@gmail.com"
		},
		"product_list": []
	}
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/grocery_list/<int:list_id>/comments/<int:comment_id>
    * __HTTP Verb:__ DELETE
    * __Required body example:__ {}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for the deletion of comments on grocery lists.
    * __Successful Output:__ {
	"message": "Comment 'We are making tacos this week, make sure you grab the spice mix' has been deleted successfully"
}
    * __Unsuccessful Output:__ {
	"error": "Comment with comment_id 1 not found"
}

* __Route:__ http://localhost:8080/grocery_list/<int:list_id>/comments/<int:comment_id>
    * __HTTP Verb:__ PUT, PATCH
    * __Required body example:__ {
	"message": "Could you grab apples mate, please and thank you."
}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for updating existing comments on grocery lists.
    * __Successful Output:__ {
	"comment_id": 2,
	"message": "Could you grab apples mate, please and thank you.",
	"timestamp": "22:00:07/28/24",
	"user": {
		"display_name": "LouisD",
		"email": "LouisDenman@gmail.com"
	},
	"grocery_list": {
		"list_id": 2,
		"list_name": "Family grocery list",
		"user": {
			"user_id": 2,
			"display_name": "Jsmith",
			"email": "Johnsmith@gmail.com"
		},
		"product_list": [
			{
				"id": 1,
				"products": {
					"product_id": 6,
					"product_name": "Watermelon",
					"product_price": 4.0
				},
				"quantity": 5
			},
			{
				"id": 2,
				"products": {
					"product_id": 9,
					"product_name": "Cucumber",
					"product_price": 1.0
				},
				"quantity": 3
			},
			{
				"id": 3,
				"products": {
					"product_id": 14,
					"product_name": "Pork",
					"product_price": 9.0
				},
				"quantity": 2
			},
			{
				"id": 4,
				"products": {
					"product_id": 24,
					"product_name": "Bread",
					"product_price": 3.0
				},
				"quantity": 7
			},
			{
				"id": 5,
				"products": {
					"product_id": 30,
					"product_name": "Magazine",
					"product_price": 5.0
				},
				"quantity": 1
			}
		]
	}
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/connections
    * __HTTP Verb:__ GET
    * __Required body example:__ {}
    * __Authorisation:__ Token required
    * __Explaination:__ This route displays connections in the app.
    * __Successful Output:__ [
	{
		"id": 1,
		"friend1_id": 1,
		"friend2_id": 2
	},
	{
		"id": 2,
		"friend1_id": 3,
		"friend2_id": 2
	}
]
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/new_connection/<int:friend_id>
    * __HTTP Verb:__ POST
    * __Required body example:__ {}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for adding a new connection in the app.
    * __Successful Output:__ {
	"id": 3,
	"friend1_id": 1,
	"friend2_id": 3
}
    * __Unsuccessful Output:__ {
	"error": "You are already friends with this user."
}

* __Route:__ http://localhost:8080/remove_connection/<int:friend_id>
    * __HTTP Verb:__ DELETE
    * __Required body example:__ {}
    * __Authorisation:__ Token required
    * __Explaination:__ This route is responsible for the removal of connections between users in the app.
    * __Successful Output:__ {
	"message": "This connection has been removed."
}
    * __Unsuccessful Output:__ {
	"error": "You are not connected with this user or the user cannot be found."
}

* __Route:__ http://localhost:8080/products
    * __HTTP Verb:__ GET
    * __Required body example:__ {}
    * __Authorisation:__ None
    * __Explaination:__ This route displays all products available in the app.
    * __Successful Output:__ [
	{
		"product_id": 1,
		"product_category": "Fruits & Vegetables",
		"product_name": "Tomato",
		"product_price": 1.5
	},
	{
		"product_id": 2,
		"product_category": "Fruits & Vegetables",
		"product_name": "Capsicum",
		"product_price": 2.0
	},
	{
		"product_id": 3,
		"product_category": "Fruits & Vegetables",
		"product_name": "Apple",
		"product_price": 1.0
	},
	{
		"product_id": 4,
		"product_category": "Fruits & Vegetables",
		"product_name": "Banana",
		"product_price": 1.5
	},
	{
		"product_id": 5,
		"product_category": "Fruits & Vegetables",
		"product_name": "Orange",
		"product_price": 2.0
	},
	{
		"product_id": 6,
		"product_category": "Fruits & Vegetables",
		"product_name": "Watermelon",
		"product_price": 4.0
	},
	{
		"product_id": 7,
		"product_category": "Fruits & Vegetables",
		"product_name": "Lemon",
		"product_price": 1.7
	},
	{
		"product_id": 8,
		"product_category": "Fruits & Vegetables",
		"product_name": "Coconut",
		"product_price": 5.0
	},
	{
		"product_id": 9,
		"product_category": "Fruits & Vegetables",
		"product_name": "Cucumber",
		"product_price": 1.0
	},
	{
		"product_id": 10,
		"product_category": "Fruits & Vegetables",
		"product_name": "Eggplant",
		"product_price": 1.5
	},
	{
		"product_id": 11,
		"product_category": "Meat & Dairy",
		"product_name": "Beef",
		"product_price": 7.0
	},
	{
		"product_id": 12,
		"product_category": "Meat & Dairy",
		"product_name": "Turkey",
		"product_price": 6.5
	},
	{
		"product_id": 13,
		"product_category": "Meat & Dairy",
		"product_name": "Chicken",
		"product_price": 7.0
	},
	{
		"product_id": 14,
		"product_category": "Meat & Dairy",
		"product_name": "Pork",
		"product_price": 9.0
	},
	{
		"product_id": 15,
		"product_category": "Meat & Dairy",
		"product_name": "Bacon",
		"product_price": 7.0
	},
	{
		"product_id": 16,
		"product_category": "Meat & Dairy",
		"product_name": "Cheddar Cheese",
		"product_price": 4.0
	},
	{
		"product_id": 17,
		"product_category": "Meat & Dairy",
		"product_name": "Shredded Cheese",
		"product_price": 5.0
	},
	{
		"product_id": 18,
		"product_category": "Meat & Dairy",
		"product_name": "Light Milk",
		"product_price": 6.0
	},
	{
		"product_id": 19,
		"product_category": "Meat & Dairy",
		"product_name": "Full Cream Milk",
		"product_price": 5.0
	},
	{
		"product_id": 20,
		"product_category": "Meat & Dairy",
		"product_name": "Cottage Cheese",
		"product_price": 3.0
	},
	{
		"product_id": 21,
		"product_category": "Carbohydrates",
		"product_name": "White Rice",
		"product_price": 4.0
	},
	{
		"product_id": 22,
		"product_category": "Carbohydrates",
		"product_name": "Brown Rice",
		"product_price": 5.0
	},
	{
		"product_id": 23,
		"product_category": "Carbohydrates",
		"product_name": "Pasta",
		"product_price": 4.0
	},
	{
		"product_id": 24,
		"product_category": "Carbohydrates",
		"product_name": "Bread",
		"product_price": 3.0
	},
	{
		"product_id": 25,
		"product_category": "Carbohydrates",
		"product_name": "Tortillas",
		"product_price": 4.0
	},
	{
		"product_id": 26,
		"product_category": "Miscellaneous",
		"product_name": "Knife Set",
		"product_price": 10.0
	},
	{
		"product_id": 27,
		"product_category": "Miscellaneous",
		"product_name": "Cutting Board",
		"product_price": 8.0
	},
	{
		"product_id": 28,
		"product_category": "Miscellaneous",
		"product_name": "Containers",
		"product_price": 15.0
	},
	{
		"product_id": 29,
		"product_category": "Miscellaneous",
		"product_name": "Baking Pack",
		"product_price": 20.0
	},
	{
		"product_id": 30,
		"product_category": "Miscellaneous",
		"product_name": "Magazine",
		"product_price": 5.0
	}
]
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/products/<int:product_id>
    * __HTTP Verb:__ GET
    * __Required body example:__ {}
    * __Authorisation:__ None
    * __Explaination:__ This route displays one specific product from the app.
    * __Successful Output:__ {
	"product_id": 5,
	"product_category": "Fruits & Vegetables",
	"product_name": "Orange",
	"product_price": 2.0
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/custom_product
    * __HTTP Verb:__ POST
    * __Required body example:__ {
	"product_category": "Fruits & Vegetables",
	"product_name": "Dragonfruit",
	"product_price": "5"
}
    * __Authorisation:__ None
    * __Explaination:__ This route allows users to create custom products for the app.
    * __Successful Output:__ {
	"product_id": 31,
	"product_category": "Fruits & Vegetables",
	"product_name": "Dragonfruit",
	"product_price": 5.0
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/add_to_grocery_list/<int:list_id>
    * __HTTP Verb:__ POST
    * __Required body example:__ {
	"quantity": "3",
	"product_id": "8"
}
    * __Authorisation:__ Token required
    * __Explaination:__ This route allows users to add items to their grocery lists.
    * __Successful Output:__ {
	"list_id": 1,
	"list_name": "Housemates grocery list",
	"user": {
		"user_id": 1,
		"display_name": "LouisD",
		"email": "LouisDenman@gmail.com"
	},
	"product_list": [
		{
			"id": 11,
			"products": {
				"product_id": 8,
				"product_name": "Coconut",
				"product_price": 5.0
			},
			"quantity": 3
		}
	],
	"comments": [
		{
			"comment_id": 1,
			"message": "We are making tacos this week, make sure you grab the spice mix",
			"timestamp": "10:10:07/27/24",
			"user": {
				"display_name": "MJparker",
				"email": "Maryjane@gmail.com"
			}
		}
	]
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}

* __Route:__ http://localhost:8080/remove_from_grocery_list/<int:list_id>
    * __HTTP Verb:__ DELETE
    * __Required body example:__ {
	"id": "11"
}
    * __Authorisation:__ Token required
    * __Explaination:__ This route allows users to remove items from their grocery lists.
    * __Successful Output:__ {
	"list_id": 1,
	"list_name": "Housemates grocery list",
	"user": {
		"user_id": 1,
		"display_name": "LouisD",
		"email": "LouisDenman@gmail.com"
	},
	"product_list": [],
	"comments": [
		{
			"comment_id": 1,
			"message": "We are making tacos this week, make sure you grab the spice mix",
			"timestamp": "10:10:07/27/24",
			"user": {
				"display_name": "MJparker",
				"email": "Maryjane@gmail.com"
			}
		}
	]
}
    * __Unsuccessful Output:__ {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}


