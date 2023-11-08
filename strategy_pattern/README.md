Main Components
Context - Class that uses various strategies
Strategy Interface - Sets API for family of algorithms
Concrete Strategies - Individual algorithms of specific strategy. Example NavigateWalk, NavigateDrive, NavigatePublicTransport, etc
client - Code that calls the contexts and assigns the strategy to use

One of the main ideas is that the client has the ability to change the strategy depending on what it needs during run time, which is why the context usually has a setter.
