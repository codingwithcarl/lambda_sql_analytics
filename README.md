<div id="top"></div>

<!-- HEADER -->
<br />
<div align="center">

  <h3 align="center">Lambda SQL Analytics</h3>

  <p align="center">
    Automate SQL queries with a Python Lambda Function.
    <br />
    <br />
  </p>
</div>

<!-- ABOUT -->
## About

This is a lambda function which queries an RDS database, writes the results to an Excel file, and saves the file to an S3 bucket.

### Built With

* [Python](https://python.org/)
* [AWS Lambda](https://aws.amazon.com/lambda/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

1. An AWS account
2. An RDS database to run the queries against
3. Permissions for RDS, Lambda, S3, and EventBridge (CloudWatch Events)

### Installation

1. Clone the repo
2. Modify `lambda.py` to match your specific environment: database connection details, queries you want to run, name your Excel sheets, name the file, and specify the S3 bucket name.
3. If you wish to have this run on a schedule, add an EventBridge trigger and specify an interval number of days when this function is executed. 

<!-- USAGE EXAMPLES -->
## Usage

This function is very useful if you have a need to re-run the same SQL queries on a set schedule, like every week or two, or even every day. The Excel file generated could be useful to a business analyst to track any kind of change to your database: number of users, emails for a newsletter, telemetry, etc.  

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/MyGreatFeatureRequest`)
3. Commit your Changes (`git commit -m 'Add some features'`)
4. Push to the Branch (`git push origin feature/MyGreatFeatureRequest`)
5. Open a Pull Request