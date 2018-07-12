import logging
import numpy as np
from image_prediction.services import ImagePredictServices
from django.test import TestCase
from PIL import Image

logger = logging.getLogger(__name__)

class ImagePredictServicesTestCase(TestCase):
    def setUp(self):
        self.service = ImagePredictServices()

    def test_preprocess_test_images(self):
        # given
        test_images = [np.array(Image.new("RGB", (120, 60), (255, 0, 0))) for i in range(10)]
        logger.info("test_images num: {}".format(len(test_images)))
        # when
        test_images = self.service.preprocess_test_images(test_images)
        self.assertEqual(test_images.shape, (10, 150, 150, 3))

