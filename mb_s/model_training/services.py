import shutil, os, uuid
from mbs_db.models import Challenge, ImageFile, ImageClass, ModelInfo
from cnn_model.cnn_factory import CNNFactory
from keras.preprocessing.image import ImageDataGenerator

class ModelTrainingServices:
    @staticmethod
    def run(challenge_id):
        train_dir = "train_dir"
        imageclass_list = ImageClass.objects.filter(challenge_id=challenge_id)
        ModelTrainingServices.export_dataset(imageclass_list, train_dir)
        # training model
        train_info = ModelTrainingServices.train_from_dir(train_dir)
        model = train_info['model']
        label_dict = train_info['label_dict']

        model_name = str(uuid.uuid1()) + ".h5"
        model_dir = "model_dir"
        challenge = Challenge.objects.get(pk=challenge_id)
        model_info = ModelInfo(
            name = model_name, 
            model_path = model_dir + "/" + model_name,
            train_challenge = challenge.name,
            label_dict = label_dict)
        model_info.save()
        # save model to model_dir
        if not os.path.exists(model_dir):
            os.mkdir(model_dir)
        model.save("model_dir/" + model_name)
        del model
    
    @staticmethod
    def export_dataset(imageclass_list, training_dir):
        if os.path.exists(training_dir):
            shutil.rmtree(training_dir)
        os.mkdir(training_dir)

        for imageclass in imageclass_list:
            train_class_path = training_dir + "/" + imageclass.name
            os.mkdir(train_class_path)
            imagefile_list = ImageFile.objects.filter(imageclass_id=imageclass.id)
            train_image_list = imagefile_list
            for imagefile in train_image_list:
                shutil.copy(imagefile.model_pic.path, train_class_path)
    
    @staticmethod
    def train_from_dir(train_dir):
        img_height = 150
        img_width = 150
        input_shape = (img_height, img_width, 3)
        epochs = 10
        batch_size = 32
        nb_train_samples = 1000

        # image data generator
        train_datagen = ImageDataGenerator(
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)
        
        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(img_height, img_width),
            batch_size=batch_size,
            class_mode='categorical')
        
        class_num = train_generator.num_class
        # get class label mapping
        label_dict = train_generator.class_indices
        # choose cnn type
        cnn_template = CNNFactory.make_cnn("default")
        model = cnn_template.build_model(input_shape, class_num)
        # train model
        model.fit_generator(
            train_generator,
            steps_per_epoch=nb_train_samples // batch_size,
            epochs=epochs)
        
        train_info = {
            'model': model,
            'label_dict': label_dict
        }
        return train_info
