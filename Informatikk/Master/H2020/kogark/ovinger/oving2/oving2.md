# TDT4137 (Cognitive Architectures) Assignment Sheet 2

## 1 Building blocks of Cognitive Architectures

### 1.1 Symbolic vs. sub-symbolic representations

#### 1.1.1 General questions

> **Task 1.1**: Why do we separate methods in symbolic methods and sub-symbolic methods? Explain the difference. Why is it customary to use the term 'sub-symbolic' and not 'non-symbolic'?

We separate the methods because they operate with different types of data. Symbolic approaches operate with strings of characters that represent real-world entities or concepts. They take the symbols, applies rules and spit out an output. Sub-symbolic methods can work with numerical patterns and/or probabilistic data, a more distributed representation, such as a neural network or CDs.

We use the term "sub-symbolic" and not "non-symbolic" because even though the system is sub-symbolic, it does operate with symbols. Non-symbolic suggests that there are no symbols used at all.

> **Task 1.2**: What is the main difference between cognitivistic and emergent approaches?

The main difference between cognitivistic and emergent approaches is that a cognitivistic process is a symbolic system, whereas emergent systems are sub-symbolic. A cognitivistic approach is more like "if-then" rules. Like the previous question - it applies rules to symbols and spits out an output. Emergent systems are more dynamic. It can learn and adapt, by building massively parallel models, such as neural networks, where information is, like in neurons, propagation of signals from input nodes.

> **Task 1.3**: If a system shows intelligent behaviour through emergent approaches, what does this mean?

This means that the emergent system is thinking rationally and are _learning_ from the problems it is solving.

#### 1.1.2 Hybrid architectures

> **Task 1.4**: What are some key benefits of creating hybrid architectures? Why do people create this type of architecture?

The benefits of creating hybrid systems are that we get "the best of both worlds". We do not, for instance, have to explicitly program all knowledge, like in a cognivistic system, because emergent systems are more dynamic and can adapt and learn. This makes the system able to understand the external world.

> **Task 1.5**: When combining symbolic and sub-symbolic systems to create a hybrid architecture, what is included from each?

From sub-symbolic systems, at least one module for sensory processing are included, and the rest of the knowledge and processing are included from symbolic systems.

### 1.2 Perception and sensing

> **Task 1.6**: Why is cognitive architecture research very often centred around vision?

Regardless of what an intelligent system is meant to do, it will need perception - that is, input from the outside world to produce behaviour. _Vision_ is the dominating way of perceiving the 'outside world' and are therefore extremely central in cognitive architecture.

> **Task 1.7**: Explain the three stages of vision as proposed by David Marr.

Marr proposed visual processing as three stages, **Early Vision**, **Intermediate vision** and **Late stage vision**.

In the Early vision stage, the system is perceiving simple elements such as colour, luminance, shape and motion. In the intermediate stage, these simple elements are grouped into regions, which in the late stage are recognized as objects and assigned meaning based on the knowledge the system already has on the environment.

> **Task 1.8**: What applications is audition used for in cognitive architectures?

Audition is mostly used when the system has to precept sound. This is widely used when a system wants to be a text-to-speech (or speech-to-text) system, such as, for example, google translate or a Google home/Alexa.

### 1.3 Attention

> **Task 1.9**: Explain the three classes of information reduction mechanisms and how they relate to each other

Attention is closely related to perception. It is what you do after you have perceived.

The three classes of information reduction mechanisms are **selection**, **restriction** and **suppression**.

**Selection** focuses on choosing one from many. That is - deciding what object/event to focus on or what region/feature/time/object, etc.. are of interest.

**Restriction** restricts the amount of information you have. I.e. choose some from many to focus on. Another way to put it is that it prunes the search space. This is done by preparing the visual system for input based on task demands, the domain knowledge, external stimuli, restrict attention to objects relevant for the task and limit the field of view. Restriction uses the goal of the task to restrict the search space to only relevant information, based on the system's knowledge.

**Suppression** suppresses some from many. This means that there is much noise that is not relevant to the current goal, such as a TV playing in the background or other irrelevant sound.

> **Task 1.10**: Explain the difference between data-driven and task-driven attention. Use at least one example.

Data-driven tries to identify the most noticeable or interesting regions in an image. For example, in a picture of a snowy field and a req glove, the region containing the glove would be identified, rather than the rest of the image, because of it's colour and shape. A task-driven approach would also focus this glove but in a different manner. It would have been told that it is looking for a glove or a red object.

### 1.4 Action selection

> **Task 1.11**: What are the two major approaches to action selection, and how does this relate to symbolic vs. non-symbolic architectures?

Action selection determines "what to do next?". This is done in two major approaches, **Planning** and **Dynamic**. In the planning approach, the system plan all the steps it will do in front. In the dynamic approach, each step is calculated "in the moment" - the best action is chosen among the alternatives based on the available knowledge.

This can be related to symbolic and non-symbolic architectures in the sense that symbolic arcitechtures are parsing symbols, and planning action selection is a predefined set of actions that are waiting to be parsed, wheras dynamic action selection are "on the go", such as non-symbolic systems are "on the go" - like a self moving car.

### 1.5 Memory

> **Task 1.12**: Explain the multi-store concept of memory.

The multi-store concept is a structural model proposed by Atkinson and Shiffrin in 1968. It says that memory consists of three stores: a sensory register, short-term memory and long-term memory.

> **Task 1.13**: It is common to distinguish between short-term and long-term memory. From which research discipline does this separation come from?

This discipline comes from the study of psychology.

> **Task 1.15**: Mention some key differences in how knowledge is represented in symbolic vs. non-symbolic architectures.

Knowledge is represented in lots of different ways. In symbolic architectures, the most common representation of knowledge is "if-then" statements. These are often represented as graphs (or flow charts). In emergent systems and non-symbolic architectures, however, the most common representation is by a set of neural networks or state/action pairs, who holds input/output values.

## 2 Soar

> **Task 1.16**: Explain the following phases: Input phase, Operator selection, and Operator application.

In the _input phase_, Working memory elements, such as goals, problem spaces, states and operators, are created that reflects changes in perception. The _operator selection_ are concerned with choosing a preferred operator and putting it into the WM. Following these two phases, the _operator application_ applies the new operation. This is done by applying rules which match the operator chosen and make changes to the WM.
