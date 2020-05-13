Muscle dynamics
=================


.. _Github: https://github.com/antoinefalisse/solvemuscleredundancy_dev/




Muscle redundancy solver
-------------------------


In the human movement biomechanics group, we provided MATLAB code that solves the muscle redundancy problem using the direct collocation optimal control software GPOPS-II as described in *De Groote F, Kinney AL, Rao AV, Fregly BJ. Evaluation of direct collocation optimal control problem formulations for solving the muscle redundancy problem. Annals of Biomedical Engineering (2016)*. The main advantage of this formulation compared to CMC or static optimiation is that it:

* Simulates the full hill type muscle model (i.e. SO neglects tendons and parallel elastic elements)
* Optimizes the muscle excitations globally instead of locally (i.e. CMC)
* Is computationally efficient (especially with automatic differentation)

Link to the Github project: Github_.

Example: changes achilles tendon stiffness
--------------------------------------------

I made a small example to showcase the importance of simulating the full hill-type muscle dynamics for estiming muscle energetics during walking. In this example, we used Umbergers equations to compute muscle energetics form the neuromuscular state. The influence of achilles tendon stiffness on metabolic energy was computed under the assumption that the joint kinematics are fixed (plase note that this is a very big assumption!). The resulting figure shows that for a given walking pattern (i.e. kinemtics/kinetics) the energy cost of walking has a clear optimum around a normalized tendon stiffness of 14.


.. image:: {static}/images/MetabolicSimulation_Tendon.svg
	:align: center 
	:alt: Influence 
	:width: 80 %






