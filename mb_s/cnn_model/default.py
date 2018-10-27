import logging
from keras.layers import Input, Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Model

class DefaultModel:
    @staticmethod
    def build_model(input_shape, class_num):
        input_img = Input(shape=input_shape)
        x = Conv2D(32, (5, 5), activation='relu')(input_img)
        x = MaxPooling2D(pool_size=(2, 2))(x) 
        x = Conv2D(64, (3, 3), activation='relu')(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)
        x = Flatten()(x)
        x = Dense(64, activation='relu')(x)
        x = Dropout(0.5)(x)
        output = Dense(class_num, activation='softmax')(x)
        model = Model(inputs=input_img, outputs=output)
        model.compile(loss='categorical_crossentropy',
            optimizer='rmsprop',
            metrics=['accuracy'])
        return model
