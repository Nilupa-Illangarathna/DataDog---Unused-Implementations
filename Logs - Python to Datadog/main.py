try:
    # Import required modules
    import os
    import logging
    from logging import StreamHandler
    from datadog_api_client.v2 import ApiClient, ApiException, Configuration
    from datadog_api_client.v2.api import logs_api
    from datadog_api_client.v2.models import *
    from faker import Faker

except Exception as e:
    # Print error if module import fails
    print("Error : {} ".format(e))


# Custom logging handler that sends logs to Datadog using the Datadog API
class DDHandler(StreamHandler):
    def __init__(self, configuration, service_name, ddsource):
        StreamHandler.__init__(self)
        self.configuration = configuration
        self.service_name = service_name
        self.ddsource = ddsource

    def emit(self, record):
        # Format log message
        msg = self.format(record)

        # Send log to Datadog
        with ApiClient(self.configuration) as api_client:
            api_instance = logs_api.LogsApi(api_client)
            body = HTTPLog(
                [
                    HTTPLogItem(
                        ddsource=self.ddsource,
                        ddtags="env:{}".format(
                            os.getenv("ENV"),
                        ),
                        message=msg,
                        service=self.service_name,
                        status=record.levelname
                    ),
                ]
            )

            try:
                # Submit logs
                api_response = api_instance.submit_log(body)
            except ApiException as e:
                print("Exception when calling LogsApi->submit_log: %s\n" % e)


# Logger that uses the custom DDHandler to send logs to Datadog
class Logging(object):
    def __init__(self, service_name, ddsource, logger_name='demoapp'):

        self.service_name = service_name
        self.ddsource = ddsource
        self.logger_name = logger_name

        self.configuration = Configuration()

        # Define log format
        format = "[%(asctime)s] %(name)s %(levelname)s %(message)s"
        self.logger = logging.getLogger(self.logger_name)
        formatter = logging.Formatter(format)

        # Add custom DDHandler to logger
        dd = DDHandler(self.configuration, service_name=self.service_name, ddsource=self.ddsource)
        dd.setLevel(logging.INFO)
        dd.setFormatter(formatter)
        self.logger.addHandler(dd)

        # Set global log level to INFO
        if logging.getLogger().hasHandlers():
            logging.getLogger().setLevel(logging.INFO)
        else:
            logging.basicConfig(level=logging.INFO)


# Main function that generates fake data and sends logs to Datadog
def main():
    import time

    # Set Datadog API keys and site in environment variables
    os.environ['DD_API_KEY'] = "< YOUR-API-KEY >"
    os.environ['DD_APP_KEY'] = "< YOUR-APP-KEY >"
    os.environ['DD_SITE'] = "< YOUR-SITE >"

    # Set environment variable
    os.environ['ENV'] = "DEV"

    # Create logger and send logs to Datadog
    logger = Logging(service_name='first-service3', ddsource='my_python_program3', logger_name='my_service')
    for i in range(1, 15):
        _instance = Faker()

        _data = {
            "first_name": _instance.first_name()
        }

        # Send logs at different levels
        logger.logger.info(_data)
        logger.logger.warning(_data)
        logger.logger.error(_data)

        time.sleep(1)

main()
