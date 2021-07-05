#!python

import os
from main import create_app
from waitress import serve

application = create_app('int')

if __name__ == "__main__":

    # For deploying to AWS Elastic beanstalk
    # application.debug = False
    # application.run()

    # For deploying using waitress
    serve(application , host='0.0.0.0' , port=8080)