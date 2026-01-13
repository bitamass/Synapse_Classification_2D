"""ResNet-based binary classifier for synapse E/I prediction."""

import torch
import torch.nn as nn
from torchvision import models


class SynapseEINet(nn.Module):
    """ResNet-50 adapted for grayscale EM images and binary output."""

    def __init__(self):
        super().__init__()

        # Load ImageNet-pretrained ResNet-50
        self.model = models.resnet50(
            weights=models.ResNet50_Weights.IMAGENET1K_V1
        )

        # Modify first convolution for 1-channel EM data
        # Kernel size, stride, and padding match the standard ResNet-50 defaults.
        self.model.conv1 = nn.Conv2d(
            1,       # single-channel input
            64,
            kernel_size=7,
            stride=2,
            padding=3,
            bias=False
        )

        # Replace classifier head (2 classes: excitatory vs inhibitory)
        in_features = self.model.fc.in_features
        self.model.fc = nn.Linear(in_features, 2)

    def forward(self, x):
        """Forward pass."""
        return self.model(x)
