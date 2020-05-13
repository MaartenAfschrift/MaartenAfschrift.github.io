Human balance control
===========================

.. image:: {static}/images/GaitPerturb_Figure.jpg
	:align: center 
	:alt: GaitPerturbation gigure by Adriaan Marin
	:width: 50 %


Introduction
-------------

This project focusses on how humans control balance during standing and walking. To most of us, standing and walking are easy. This is remarkable, given the fact that from a mechanical point of view walking is highly unstable and therefore requires well-coordinated active control. This becomes apparent in the elderly. There is a high incidence of falls in the elderly, often resulting in significant injuries and loss of independence.

Deterioration of balance control may contribute to increased fall risk in older adults. Impaired balance was indeed correlated with an increased risk of falls. Simple tests, such as standing on a narrow beam or a near-tandem standing test with eyes open and closed can differentiate between elderly with and without a history of falls. During these tasks, larger corrective movements have been recorded in fallers compared to non-fallers. Therefore, the inability to control balance during standing has been reported as a significant risk factor for future falls in older adults. 

However, correlations between age-related decrease in balance performance and the incidence of falling only provide limited insight in the underlying mechanisms by which aging alters balance control. An improved understanding of age-related changes in balance control and the contribution of changes in the neural and muscular system to the control of balance could improve therapeutic approaches aiming at fall prevention. For example, these insights may steer neuromuscular training programs to target the age-related changes that affect balance control most efficiently.


The mechanisms behind balance control
-------------------------------------

The human musculoskeletal system is mechanically unstable because of its many degrees of freedom combined with the high location of the center of mass (COM) above a small base of support. Reactive and anticipatory mechanisms contribute to the control of balance during standing and walking. Reactive control of balance relies on different components of the neuro-musculoskeletal system including (1) the musculoskeletal system, (2) the sensory system, and (3) sensory and cognitive processing in the nervous system. 


The musculoskeletal system consists of the skeletal structure, actuated by muscles. In a static situation, the musculoskeletal system is stable if the projection of the center of mass position is within the base of support. The conditions for stability are more complex during dynamic tasks. The extrapolated center of mass (Xcom) or capture point was introduced to extend the static definition of stability by correcting the COM position with the COM velocity. The Xcom is derived from a linear inverted pendulum model and represents the point on the ground where the center of pressure (COP) has to be placed to result in a vertical position of the inverted pendulum (i.e. kinetic energy is transferred into potential energy). The distance between the Xcom and the boundaries of the base of support can be used to quantify the stability of the skeletal system under the inverted pendulum assumption and is referred to as margin of stability. Both active (muscle activity) and passive (e.g. passive muscle properties, ligaments) musculoskeletal components contribute to balance control as they provide resistance to perturbations and assist in keeping the Xcom position within the base of support. Using the passive and active muscle properties, stability of the skeletal system can be maintained in the presence of internal and external perturbations by adjusting stiffness and damping in the joints (i.e. mechanical impedance). Muscle force is controlled by the nervous system to compensate for instability of the skeletal system. Muscle strength, joint range of motion and segmental inertial and kinematic properties are referred to as musculoskeletal constraints for balance control.


The sensory systems involved in the control of balance are the visual, vestibular and somatosensory systems, which provide information about the state of the musculoskeletal system. The somatosensory system consists of muscle splindles, Golgi tendon organs, cutaneous receptors and other mechanoreceptors that provide the centeral nervous system with tactile, proprioceptive and kinesthetic information. The vestibular system provides information about the tilt of the head with respect to gravity and its angular acceleration. The visual system provides information about the body orientation with respect to the environment. Sensory integration is important in balance control and can be defined as the fusion of information from visual, vestibular and somatosensory systems to estimate the current orientation of the body in space \cite{Franklin2011}. Several studies described that the relative importance of visual, somatosensory and vestibular information in the sensory integration process varies when the sensory environment changes (i.e. sensory reweighting) \cite{Franklin2011}. For example, Peterka et al. estimated that healthy young subjects rely on somatosensory (70\%), vision (10\%), and vestibular (20\%) information to control balance during standing. When the sensory environment was manipulated by means of a non-rigid support surface, the subjects decreased their dependence on the unreliable somatosensory inputs and therefore relied more on visual and vestibular information \cite{Peterka2002}. The mechanism of reweighting redundant sensory information improves the accuracy of the estimation of the current orientation of the body in space in the presence of noise in the sensory system. 


Sensory information is processed by the central nervous system to generate motor commands. Several studies suggested that sensory information is integrated based on an internal model of the musculoskeletal system to estimate the current orientation of the body in space (i.e. state estimation). This internal model represents the relationship between motor commands and their effect on the limbs movements. The internal model therefore does not only describe the kinematics of the musculoskeletal system, but also considers the inertial properties of each segment. Discrepancies between the desired and estimated state induce efferent signals to the muscles to control balance.


A model describing the different subcomponents and their interactions can be used to gain insights in the control of balance (Figure \ref{fig:Intro_FBModel}). Reactive control of balance is often described as a delayed feedback control system in which noisy sensory information from vestibular, somatosensory and visual systems is integrated to estimate the state of the internal model. Motor commands are then generated in the task-level controller as differences between the desired and estimated state of the internal model. The task-level controller induces reactive muscle activity to control task-level variables such as effort and instability. These motor commands are subjected to signal-dependent noise due to the size principle (i.e. larger commands results in less accurate control of muscle force due to the recruitment of larger motor units). The resulting motor command is not a simple mono-synaptic reflex but relies on integration of sensory information from different systems. Therefore, we will refer to the motor command as an automatic response, which can be interpreted as a long latency reflex (i.e. time delay between 80-120ms). These automatic respones, also referred to as balance-correcting responses, then serve as input to the musculoskeletal system.





