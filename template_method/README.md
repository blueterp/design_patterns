Main Components
Superclass - defines skeleton of Algorithm and possible hooks. Many of the subtasks in the algorithm must be abstract so that the subclasses can implement then. Some subtasks are defined as concrete with default implementations that can be overriden if neeed.
Clients - subclasses implement abstract methods and override optional methods if neccessary.
