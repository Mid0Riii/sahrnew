import datetime

JWT_AUTH = {
    'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=300),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}