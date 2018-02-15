# bicycle-store
Bicycle store API with Google Cloud Endpoints Framework and datastore

## Setup

Create a `lib` directory in which to install the Endpoints Frameworks v2 library. For more info, see [Installing a library](https://cloud.google.com/appengine/docs/python/tools/using-libraries-python-27#installing_a_library).

Install the Endpoints Frameworks v2 library:

    $ pip install -t lib -r requirements.txt
    
## Test

On root location, write the following command:

    $ python runner.py <google-cloud-sdk-path> --test-path services/tests/ --test-pattern=*_test.py

Example:
    
    $ python runner.py /home/cf2017/google-cloud-sdk/ --test-path services/tests/ --test-pattern=*_test.py
    
## Deploy

Deploy the generated service spec to Google Cloud Service Management: `gcloud endpoints services deploy bicyclestorev1openapi.json`

The command returns several lines of information, including a line similar to the following:

   Service Configuration [2018-02-15r0] uploaded for service [bicycle-store-195204.appspot.com]

Open the `app.yaml` file and in the `env_variables` section, replace `2018-02-15r0` with your uploaded service management configuration.

Then, deploy the sample using `gcloud`:

    $ gcloud app deploy
