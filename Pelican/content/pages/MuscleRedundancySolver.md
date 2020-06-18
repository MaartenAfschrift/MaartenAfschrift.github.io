Title: Muscle Redundancy Solver

You can download the code on github: <https://github.com/tomvanwouwe1992/MuscleTendonEstimator>


## Purpose of the software

The original intent of the provided MATLAB code was to solve the muscle redundancy problem using direct collocation as described in De Groote F, Kinney AL, Rao AV, Fregly BJ. Evaluation of direct collocation optimal control problem formulations for solving the muscle redundancy problem. Annals of Biomedical Engineering (2016). <http://link.springer.com/article/10.1007%2Fs10439-016-1591-9>. 

From v3.0, there are possibilities to, concurrently with solving the muscle redundancy problem, estimate parameters of the modeled muscle-tendon units by using collected EMG and ultrasound data. Optimal fiber length, tendon slack length and tendon stiffness can be set as free variables within the muscle redundancy problem. Experimentally measured fiber-lengths can be tracked (US-tracking), the tracking error is a part of the objective function. Details on this parameter estimation problem can be found in Delabastita et al. 2020 (<https://link.springer.com/article/10.1007/s10439-019-02395-x>). Collected EMG can either be tracked (EMG-tracking) or imposed exactly (EMG-driven). Details on using EMG data in the parameter estimation can be found in (<https://ieeexplore.ieee.org/document/7748556>). Another important feature is that the user can estimate muscle-tendon parameters over different trials of the same movement or from different movements. This allows to make estimation more reliable. We reckon that for solving the muscle redundancy problem OpenSim Moco (<https://www.biorxiv.org/content/10.1101/839381v1>) might be a more user-friendly and straightforward alternative. However, our software allows the combination of different trials to estimate muscle-tendon parameters. Another difference is in that we use automatic differentiation, while this is not (yet) enabled in Moco. 

## Presentation

Here you can find a presentation where we explain the main concepts of the muscle redundancy solver.

<a href="https://maartenafschrift.github.io/html/Presentation1.html" target="_blank">Presentation Muscle redundancy solver!</a> 

## Source code

You can find the source code, a manual and some documented examples on our github account:

<a href="https://github.com/tomvanwouwe1992/MuscleTendonEstimator" target="_blank">Github muscle tendon estimation</a> 

## References

This work is based on

1. De Groote2016: <http://link.springer.com/article/10.1007%2Fs10439-016-1591-9>
2. Falisse 2016: <https://ieeexplore.ieee.org/document/7748556).>
3. Delabastita et al. 2020 (<https://link.springer.com/article/10.1007/s10439-019-02395-x>)

Any questions? Please contact us:
maarten.afschrift@kuleuven.be and tom.vanwouwe@kuleuven.be for questions on the parameter optimization algorithm;  friedl.degroote@kuleuven.beantoine.falisse@kuleuven.be.



