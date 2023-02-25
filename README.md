# artista
The Django Intern Assignment requires the creation of a backend structure consisting of three tables: Client, Artist, and Work. The Client table should have a foreign key to a User instance, while the Artist table should have a many-to-many relationship with the Work table.
The Work table should have a link and a work type, which can be "YouTube," "Instagram," or "Other."

After each registration for a new user, a new Client object should be created using signals. The backend should also include REST API endpoints for displaying works, filtering works by work type or artist name, and registering a new user with a username and password.

The API endpoints should follow the format:

http://127.0.0.1:8000/
http://127.0.0.1:8000/loggedin
http://127.0.0.1:8000/signedin
http://127.0.0.1:8000/api
http://127.0.0.1:8000/search
http://127.0.0.1:8000/filter

The filter works with only 'Instagram' and 'Youtube' which are case sensetive

Please Search for artist from the following list as we do not have an extensive databse right now:
Anuv Jain
Abhishek Upmanyu
Anubhav Singh Bassi
Selena Gomez
Alia Bhatt
Robert Downey
