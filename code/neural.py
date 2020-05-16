# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:54:34 2020

@author: srava
"""
from ase.io import read
from ase.io.trajectory import Trajectory
import numpy as np
from ase.calculators.emt import EMT

from amp import Amp
from amp.descriptor.gaussian import Gaussian
from amp.utilities import hash_images
from amp.model.neuralnetwork import NeuralNetwork

import matplotlib.pyplot as plt

calc = Amp(descriptor=Gaussian(), model=NeuralNetwork(),
           label='calc')
calc.model.lossfunction.parameters['convergence'].update(
    {'energy_rmse': 0.05,})
calc.train(images='training_data.traj')
