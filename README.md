# QuantumNeuralNetwork
<div align="center"><img src="images/scatter.png" style="text-align:center"/>
            <p><i>Predicted Energy (kJ/mol) vs EMT Energy (kJ/mol)</i></p></div>

## Author
Sravan Jayanthi

## Machine Learning with Density Functional Theory
The purpose of developing a neural network forcefield model is to represent the potential energy surface of molecular interactions. It has notable performance and memory benefits as opposed to performing Density Functional Thoery simulations with the drawbacks of requiring a large training set and potential for error in predicting reaction energies. The model takes atomic images that describe the energy configuration and atomic coordinates of entities involved in the reaction as input. The model uses two descriptors, radial and angular Guassian functions. The output is ultimately the predicted reaction energy and forces experienced by the atoms.


## Description
This folder contains the two scripts, the forcefield, the training data, the testing data, and the outputted validation plots for the neural network model. The main libraries used are the AMP (Atomistic Machine-learning Package) and ASE (Atomic Simulation Environment).

*neural.py- script to train the model*

*test.py- script to test the model*

*training_data.traj- data used to train the model*

*validation_data.traj- data used to test the model*

*calc.amp- the outputted model*


### Code
Sample code of setting up and training the neural net model.

            calc = Amp(descriptor=Gaussian(), model=NeuralNetwork(), label='calc')
            calc.model.lossfunction.parameters['convergence'].update(
                {'energy_rmse': 0.05,})
            calc.train(images='training_data.traj')


## License
[MIT](LICENSE)
