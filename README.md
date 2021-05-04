**Ensemble search API**

Instructions to run this web service:

This application requires:

    Python 3.8.6

Install the requirements using:

pip install -r requirements.txt

To run the application (this will start the flask server - default port is 5000):

python run_server.py

Hit the endpoint using [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) 
or any other API platform your prefer:

```
    http://localhost:5000/gene_suggest?query=nd&species=rhinopithecus_roxellana&size=5
```

You should see the response:

```
 {
    "results": {
        "geneNames": [
            "ND1",
            "ND2",
            "ND3",
            "ND4",
            "ND4L"
        ],
        "query": "nd",
        "species": "rhinopithecus_roxellana"
    }
}
```

To format the code, [Black](https://github.com/psf/black) formatter is used which follows PEP8 standards:

```
black .
```


**Deployment**

There can be different ways to deploy this application:
1. Easiest would be to deploy this web service to AWS EC2 instance, using gunicorn for server and nginx for reverse proxy and load balancing and if there is a front-end for this web service,
that could be deployed to S3 bucket.
OR
2. The web service could be deployed to Heroku (free tier) but if we need to scale then we need a paid plan which does load balancing
to handle the number of requests. OR

3. Deploy to AWS elastic beanstalk - Elastic Beanstalk sets up an environment including 
EC2 instances, load balancers etc. (easier to scale if the traffic increases)

To make the solution more scalable, a more sophisticated architectural solution can be used so as to balance the load when number of requests increases.
Most of the deployment solutions above help in scaling when the load increases. For example: The auto 
scaling group in AWS Elastic Beansktalk will spawn more EC2 instances when the traffic increases.


**Testing**

To test the application:

1. Write unit tests using pytest to mock the api and validate
 the input and response of the api (testing the routes).
 
2. If the production db is very large, it is best to create a new mock database with limited values to test the routes.

3. To automate the testing, the use of CI pipelines is essential. Using a framework like CircleCI, Jenkins, Concourse etc., the tests can be automated to run on each build.