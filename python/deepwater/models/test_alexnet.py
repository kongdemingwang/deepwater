import unittest

from deepwater.models import alexnet
from deepwater import optimizers

from deepwater.models.test_utils import CIFAR10_must_converge
from deepwater.models.test_utils import MNIST_must_converge


class TestVGG(unittest.TestCase):
    def test_vgg_must_converge_on_MNIST(self):
        MNIST_must_converge("alexnet", alexnet.AlexNet,
                            optimizers.RMSPropOptimizer,
                            batch_size=32,
                            epochs=3,
                            initial_learning_rate=0.2,
                            summaries=False,
                            use_debug_session=False)

    def test_vgg_must_converge_on_CIFAR10(self):
        CIFAR10_must_converge("alexnet", alexnet.AlexNet,
                              optimizers.RMSPropOptimizer,
                              batch_size=32,
                              epochs=3,
                              initial_learning_rate=0.2,
                              summaries=False,
                              use_debug_session=False)


if __name__ == "__main__":
    unittest.main()
