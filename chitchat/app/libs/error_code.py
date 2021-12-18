# from werkzeug.exceptions import HTTPException
from app.libs.error import APIException

# class Custom(APIException):
#     def __init__(self, code, msg, error_code):
#         Custom.code = code
#         Custom.msg = msg
#         Custom.error_code = error_code

# 数据处理错误



# 成功标志
class Success(APIException):
    code = 201
    msg = 'Success'
    error_code = 0



# 模型错误
class ModelExist(APIException):
    code = 500
    msg = 'Model foder exist,please rename model folder'
    error_code = 1

class ModelInitializeFail(APIException):
    code = 400
    msg = 'The model was not initialized successfully'
    error_code = 1

class ModelTrainSuccess(Success):
    code = 200
    msg = 'Model training successful'

class ModelTrainFail(APIException):
    code = 500
    msg = 'Model training failure'
    error_code = -1

# 训练错误
class TrainFileNotFound(APIException):
    code = 400
    msg = 'Train file not found'
    error_code = 1

class TrainSuccess(APIException):
    code = 200
    msg = 'Begin train, Check your training log in time'
    error_code = 0

class ValidDataGenerateFail(APIException):
    code = 400
    msg = 'Validation data generation failed'
    error_code = 1


class RawFileProcessError(APIException):
    code = 500
    msg = 'raw file process error'
    error_code = -1

class ModelInitializeSuccess(APIException):
    code = 200
    msg = 'the model was initialized successfully'
    error_code = 0

class FileUploadSuccess(APIException):
    code = 200
    msg = 'file uploaded successfully'
    error_code = 0

class DeleteSuccess(Success):
    code = 202
    msg = '删除成功'
    error_code = -1  # 删除成功


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake'
    error_code = 999

class FILEEXISTS(APIException):
    code = 401
    msg = 'file already exists'
    error_code = 999


class ClientTypeError(APIException):
    code = 400  # 代表参数错误
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401  # 授权失败
    error_code = 1005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403  # 权限不够，禁止访问
    error_code = 1004
    msg = 'forbidden'
