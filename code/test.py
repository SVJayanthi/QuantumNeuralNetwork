# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:53:47 2020

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

list_of_atoms = []
emt_energies = []
traj = Trajectory("validation_data.traj")
for atoms in traj:
    atoms.set_calculator(EMT())
    emt_energies.append(atoms.get_potential_energy())


calc = Amp.load('calc.amp')


NN_potential_energies = []
for atoms in traj:
    atoms.set_calculator(calc)
    NN_potential_energies.append(atoms.get_potential_energy())


plt.scatter(emt_energies, NN_potential_energies)
plt.savefig('scatter.png')

plt.plot(min(emt_energies), max(emt_energies))
plt.ylabel('NN Predicted Energy')
plt.xlabel('EMT Energy')
plt.savefig('predict.png')

# make the parity line
combined = emt_energies + NN_potential_energies
minumum = min(combined)
maximum = max(combined)
plt.plot([minumum, maximum],[minumum, maximum])
plt.savefig('parity.png')


sse = [(a - b) ** 2 for a, b in zip(emt_energies, NN_potential_energies)]
mse = np.mean(sse)
rmse = np.sqrt(mse)
print(rmse)