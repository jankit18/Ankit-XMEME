# XMEME :tophat:
### An online platform for gate aspirants.
### Check out the Demo Deploment here: ( https://xmeme-ankit.herokuapp.com/ ) 


# FEATURES :fire:
- CREATE MEME
- UPDATE MEME
- RECENT 100 MEME DISPLAY
- PORT EXPOSED 8081

# API STRUCTURE :open_file_folder:

- [**GET,POST**]()
  - http:127.0.0.1:8081/memes/
  - GET for Fetching Recent 100 MEMES Sorted in Ascending Order of Submission Time
  - POST for Posting New Meme


- [**GET,PATCH**]()
  - http:127.0.0.1:8081/memes/<int:pk>
  - GET for Fetching the meme with (id=pk)
  - PATCH for Updating the meme with (id=pk)

- [**API Documentation**]()
  - http:127.0.0.1:8081/swagger-ui
  - For displaying API data using swagger API Documentation.
  
# Script Automation :
  - install.sh for complete requirement installation. 
  - sleep.sh to sleep the procees for 60 seconds.
  - server_run.sh for running the server at port 8081.
  - test_server.sh for complete installation and server testing, 
    it invokes install.sh, sleep.sh, server_run.sh.
  

*Thank you*
