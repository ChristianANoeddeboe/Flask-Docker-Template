
class ApplicationAPIContext():

    app_service = None
    request_handler_service = None

    def register_application_service(self, application):
        self.app_service = application

    def register_request_handler_service(self, request_handler):
        self.request_handler_service = request_handler

    def get_application_service(self):
        return self.app_service

    def get_request_handler_service(self):
        return self.request_handler_service



    
application_api_context = ApplicationAPIContext()
