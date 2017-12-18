from cnn_model.default import DefaultModel
from cnn_model.cnn_enum import CNNType


class CNNFactory:
    @staticmethod
    def make_cnn(cnn_type):
        if CNNType.DEFAULT_CNN.value == cnn_type:
            model = DefaultModel
        else:
            model = DefaultModel
        return model
