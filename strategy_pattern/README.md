Main Components
Context - Class that uses various strategies
Strategy Interface - Sets API for family of algorithms
Concrete Strategies - Individual algorithms of specific strategy. Example NavigateWalk, NavigateDrive, NavigatePublicTransport, etc
client - Code that calls the contexts and assigns the strategy to use
